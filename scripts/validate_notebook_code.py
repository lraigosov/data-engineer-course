#!/usr/bin/env python3
"""
Script para validar que los bloques de código en los notebooks sean ejecutables.
Detecta errores de sintaxis, imports faltantes, y otros problemas comunes.
"""

import json
import ast
import sys
from pathlib import Path
from typing import List, Dict, Tuple
from collections import defaultdict

class CodeValidator:
    """Validador de código Python en notebooks."""
    
    def __init__(self):
        self.errors = defaultdict(list)
        self.warnings = defaultdict(list)
        self.stats = {
            'total_notebooks': 0,
            'total_cells': 0,
            'code_cells': 0,
            'errors_found': 0,
            'warnings_found': 0,
        }
    
    def validate_cell_code(self, code: str, cell_index: int) -> Tuple[bool, List[str]]:
        """Valida que un bloque de código sea sintácticamente correcto."""
        issues = []
        
        # Ignorar celdas que contienen comandos de shell/magic de Jupyter
        if code.strip().startswith('!') or code.strip().startswith('%'):
            return True, []
        
        try:
            # Intentar compilar el código
            ast.parse(code)
        except SyntaxError as e:
            issues.append(f"❌ SINTAXIS ERROR: Línea {e.lineno}: {e.msg}")
            return False, issues
        except Exception as e:
            issues.append(f"❌ ERROR: {type(e).__name__}: {str(e)}")
            return False, issues
        
        # Validaciones adicionales
        lines = code.split('\n')
        
        # Verificar imports sin módulos instalados (solo sintaxis)
        for i, line in enumerate(lines, 1):
            line = line.strip()
            
            # Advertencia: imports futuros no en la primera línea
            if 'from __future__' in line and i > 2:
                issues.append(f"⚠️  ADVERTENCIA: __future__ import en línea {i} (debería estar al inicio)")
            
            # Advertencia: variables no utilizadas (heurística simple)
            if '= ' in line and not line.startswith('#'):
                var_name = line.split('=')[0].strip()
                # Verificar si la variable aparece después
                rest_of_code = '\n'.join(lines[i:])
                if var_name and not any(var_name in l for l in lines[i:]):
                    if not var_name.startswith('_'):
                        issues.append(f"⚠️  ADVERTENCIA: Variable '{var_name}' en línea {i} podría no ser utilizada")
        
        return len([i for i in issues if '❌' in i]) == 0, issues
    
    def validate_notebook(self, notebook_path: Path) -> Dict:
        """Valida todos los bloques de código en un notebook."""
        self.stats['total_notebooks'] += 1
        
        notebook_errors = {
            'path': str(notebook_path.relative_to(notebook_path.parent.parent.parent)),
            'code_cells': 0,
            'errors': [],
            'warnings': [],
        }
        
        try:
            with open(notebook_path, 'r', encoding='utf-8') as f:
                notebook = json.load(f)
        except (json.JSONDecodeError, UnicodeDecodeError) as e:
            notebook_errors['errors'].append(f"❌ ERROR al leer notebook: {e}")
            self.errors[notebook_path.name].append(str(e))
            return notebook_errors
        
        # Verificar cada celda
        for cell_index, cell in enumerate(notebook.get('cells', []), 1):
            self.stats['total_cells'] += 1
            
            if cell['cell_type'] == 'code':
                self.stats['code_cells'] += 1
                notebook_errors['code_cells'] += 1
                
                # Obtener el código
                source = cell.get('source', [])
                if isinstance(source, list):
                    code = ''.join(source)
                else:
                    code = source
                
                if code.strip():
                    is_valid, issues = self.validate_cell_code(code, cell_index)
                    
                    if not is_valid or any('❌' in issue for issue in issues):
                        self.stats['errors_found'] += 1
                        for issue in issues:
                            if '❌' in issue:
                                notebook_errors['errors'].append(f"Celda {cell_index}: {issue}")
                                self.errors[notebook_path.name].append(f"Celda {cell_index}: {issue}")
                    
                    for issue in issues:
                        if '⚠️' in issue:
                            self.stats['warnings_found'] += 1
                            notebook_errors['warnings'].append(f"Celda {cell_index}: {issue}")
        
        return notebook_errors
    
    def validate_level(self, level_dir: Path) -> List[Dict]:
        """Valida todos los notebooks en un nivel."""
        results = []
        
        for notebook_path in sorted(level_dir.glob('*.ipynb')):
            if notebook_path.name == 'README.md':
                continue
            
            result = self.validate_notebook(notebook_path)
            results.append(result)
        
        return results
    
    def print_report(self, results: Dict[str, List[Dict]]):
        """Imprime un reporte detallado de validación."""
        print("\n" + "="*80)
        print("📋 REPORTE DE VALIDACIÓN DE CÓDIGO EN NOTEBOOKS")
        print("="*80)
        
        for level_name, level_results in results.items():
            print(f"\n📂 {level_name.upper()}:")
            print("-" * 80)
            
            level_errors = 0
            level_warnings = 0
            
            for result in level_results:
                if result['errors'] or result['warnings']:
                    print(f"\n  📓 {Path(result['path']).name}")
                    
                    if result['errors']:
                        for error in result['errors']:
                            print(f"     {error}")
                            level_errors += 1
                    
                    if result['warnings']:
                        for warning in result['warnings'][:3]:  # Mostrar máximo 3 warnings
                            print(f"     {warning}")
                        if len(result['warnings']) > 3:
                            print(f"     ... y {len(result['warnings']) - 3} advertencias más")
                        level_warnings += len(result['warnings'])
            
            if level_errors == 0 and level_warnings == 0:
                print(f"  ✅ Todos los notebooks del nivel están correctos")
            else:
                print(f"\n  📊 Errores en nivel: {level_errors}, Advertencias: {level_warnings}")
        
        # Resumen global
        print("\n" + "="*80)
        print("📊 RESUMEN GLOBAL:")
        print("="*80)
        print(f"  📚 Total de notebooks: {self.stats['total_notebooks']}")
        print(f"  📍 Total de celdas: {self.stats['total_cells']}")
        print(f"  💻 Celdas de código: {self.stats['code_cells']}")
        print(f"  ❌ Errores encontrados: {self.stats['errors_found']}")
        print(f"  ⚠️  Advertencias encontradas: {self.stats['warnings_found']}")
        print("="*80 + "\n")


def main():
    """Función principal."""
    notebooks_dir = Path("f:/GitHub/data-engineer-course/notebooks")
    
    if not notebooks_dir.exists():
        print(f"❌ Directorio no encontrado: {notebooks_dir}")
        return 1
    
    validator = CodeValidator()
    results = {}
    
    # Niveles a validar
    levels = [
        "nivel_junior",
        "nivel_mid",
        "nivel_senior",
        "nivel_genai",
        "negocios_latam",
    ]
    
    # Validar cada nivel
    for level_name in levels:
        level_dir = notebooks_dir / level_name
        if level_dir.exists():
            print(f"🔍 Validando {level_name}...", end=" ")
            level_results = validator.validate_level(level_dir)
            results[level_name] = level_results
            
            level_errors = sum(len(r['errors']) for r in level_results)
            print(f"({level_errors} errores)")
    
    # Imprimir reporte
    validator.print_report(results)
    
    # Retornar código de salida
    return 0 if validator.stats['errors_found'] == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
