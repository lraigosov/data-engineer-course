#!/usr/bin/env python3
"""
Script para mostrar solo los errores de sintaxis reales en los notebooks.
"""

import json
from pathlib import Path
import ast

notebooks_dir = Path('notebooks')
levels = ['nivel_junior', 'nivel_mid', 'nivel_senior', 'nivel_genai', 'negocios_latam']

print('❌ ERRORES DE SINTAXIS ENCONTRADOS:\n')

total_errors = 0

for level in levels:
    level_dir = notebooks_dir / level
    if not level_dir.exists():
        continue
    
    errors_in_level = []
    
    for nb_file in sorted(level_dir.glob('*.ipynb')):
        try:
            with open(nb_file, 'r', encoding='utf-8') as f:
                nb = json.load(f)
        except:
            continue
        
        for cell_idx, cell in enumerate(nb.get('cells', []), 1):
            if cell['cell_type'] == 'code':
                source = cell.get('source', [])
                code = ''.join(source) if isinstance(source, list) else source
                
                # Ignorar celdas que contienen solo comandos shell/magic
                if code.strip():
                    try:
                        ast.parse(code)
                    except UnicodeEncodeError:
                        # Ignorar errores de encoding
                        continue
                    except SyntaxError as e:
                        # Si el error es por ! o %, es un comando shell/magic, ignorar
                        error_line = code.split('\n')[e.lineno - 1] if e.lineno else ''
                        if error_line.strip().startswith('!') or error_line.strip().startswith('%'):
                            continue
                        errors_in_level.append({
                            'notebook': nb_file.name,
                            'cell': cell_idx,
                            'line': e.lineno,
                            'msg': e.msg,
                            'code_preview': code.split('\n')[e.lineno - 1] if e.lineno else ''
                        })
    
    if errors_in_level:
        print(f'📂 {level.upper()}: {len(errors_in_level)} errores')
        for err in errors_in_level:
            print(f"  📓 {err['notebook']}")
            print(f"     Celda {err['cell']}, Línea {err['line']}: {err['msg']}")
            if err['code_preview']:
                print(f"     > {err['code_preview'][:80]}")
        print()
        total_errors += len(errors_in_level)

print(f'📊 Total de errores: {total_errors}')
