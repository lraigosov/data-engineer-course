import os
import json
import glob
import re
import sys

# Constantes
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NOTEBOOKS_DIR = os.path.join(BASE_DIR, 'notebooks')

LEVELS = {
    'nivel_junior': 'Nivel Junior',
    'nivel_mid': 'Nivel Mid',
    'nivel_senior': 'Nivel Senior',
    'nivel_genai': 'Nivel GenAI',
    'negocios_latam': 'Negocio LATAM'
}

LEVEL_ORDER = [
    'nivel_junior',
    'nivel_mid',
    'nivel_senior',
    'nivel_genai',
    'negocios_latam'
]

def get_notebook_title(notebook_path):
    """Lee el notebook y extrae el título del primer H1."""
    try:
        with open(notebook_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            
        for cell in data['cells']:
            if cell['cell_type'] == 'markdown':
                source = ''.join(cell['source'])
                match = re.search(r'^#\s+(.+)', source, re.MULTILINE)
                if match:
                    # Limpiar emojis y prefijos comunes para el índice
                    title = match.group(1).strip()
                    # Remover prefijos como "Junior - 01. ", "01. ", etc si se desea un índice más limpio
                    # Pero por ahora mantenemos el título completo o lo limpiamos un poco
                    return title
    except Exception as e:
        print(f"Error leyendo título de {notebook_path}: {e}")
    
    # Fallback al nombre de archivo
    return os.path.basename(notebook_path).replace('.ipynb', '').replace('_', ' ').title()

def create_navigation_cell(current_filename, notebooks_list, current_level_key):
    """Crea el contenido de la celda de navegación."""
    
    level_name = LEVELS[current_level_key]
    
    # Encontrar índice actual
    try:
        curr_idx = [n['filename'] for n in notebooks_list].index(current_filename)
    except ValueError:
        return None

    prev_notebook = notebooks_list[curr_idx - 1] if curr_idx > 0 else None
    next_notebook = notebooks_list[curr_idx + 1] if curr_idx < len(notebooks_list) - 1 else None

    # Construir Markdown
    lines = []
    lines.append("---\n")
    lines.append("\n")
    lines.append("## 🧭 Navegación\n")
    lines.append("\n")
    
    # Links Anterior / Siguiente
    prev_link = f"[{prev_notebook['title']}]({prev_notebook['filename']})" if prev_notebook else "[← README del Curso](../../README.md)"
    next_link = f"[{next_notebook['title']} →]({next_notebook['filename']})" if next_notebook else "Final del Nivel 🎉"
    
    lines.append(f"**← Anterior:** {prev_link}\n")
    lines.append("\n")
    lines.append(f"**Siguiente →:** {next_link}\n")
    lines.append("\n")
    
    # Índice del Nivel
    lines.append(f"**📚 Índice de {level_name}:**\n")
    for nb in notebooks_list:
        if nb['filename'] == current_filename:
            lines.append(f"- [{nb['title']}]({nb['filename']}) ← 🔵 Estás aquí\n")
        else:
            lines.append(f"- [{nb['title']}]({nb['filename']})\n")
    
    lines.append("\n")
    
    # Links a otros niveles
    lines.append("**🎓 Otros Niveles:**\n")
    for key in LEVEL_ORDER:
        name = LEVELS[key]
        lines.append(f"- [{name}](../{key}/README.md)\n")
        
    return {
        "cell_type": "markdown",
        "metadata": {},
        "source": lines
    }

def process_level(level_key):
    folder_path = os.path.join(NOTEBOOKS_DIR, level_key)
    if not os.path.exists(folder_path):
        print(f"Directorio no encontrado: {folder_path}")
        return

    # Obtener notebooks ordenados
    files = sorted([f for f in os.listdir(folder_path) if f.endswith('.ipynb')])
    
    notebooks_info = []
    for f in files:
        path = os.path.join(folder_path, f)
        title = get_notebook_title(path)
        # Limpieza básica de título para el menú (opcional)
        clean_title = re.sub(r'^[#\s]*|^\d+\.\s*', '', title) # Quitamos markers de markdown o números iniciales duplicados si existen
        # Mejor usar el título extraído tal cual o limpiarlo un poco
        clean_title = title.split('\n')[0].strip() # Primera línea
        
        # Quitamos emojis del inicio para orden visual si se quiere, o dejamos
        # Vamos a limpiar un poco "Junior - 01. Titulo" -> "Titulo" si es muy largo?
        # Por ahora lo dejamos tal cual, se ve bien.
        
        notebooks_info.append({
            'filename': f,
            'title': clean_title
        })

    # Procesar cada notebook
    for nb_info in notebooks_info:
        filename = nb_info['filename']
        file_path = os.path.join(folder_path, filename)
        
        try:
            # Safe print for Windows consoles
            print(f"Procesando {level_key}/{filename}...")
        except UnicodeEncodeError:
            print(f"Procesando {level_key}/[Nombre con caracteres especiales]...")
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                
            cells = data['cells']
            
            # Generar nueva celda de navegación
            nav_cell = create_navigation_cell(filename, notebooks_info, level_key)
            if not nav_cell:
                print(f"  Skipping {filename} (not found in list)")
                continue
            
            # Eliminar celdas de navegación antiguas (al final)
            new_cells = []
            for cell in cells:
                keep = True
                if cell['cell_type'] == 'markdown':
                    content = ''.join(cell['source'])
                    # Detectar celdas de navegación por contenido
                    if "## 🧭 Navegación" in content or "**📚 Índice de" in content or "Navegación" in content and "Anterior" in content:
                        keep = False
                if keep:
                    new_cells.append(cell)
            
            # Asegurar que appendemos al final
            new_cells.append(nav_cell)
            
            data['cells'] = new_cells
            
            # Guardar usando escritura atómica (temp file + rename) para evitar corrupción
            temp_file_path = file_path + '.tmp'
            try:
                with open(temp_file_path, 'w', encoding='utf-8') as f:
                    # ensure_ascii=True escapa caracteres no ASCII, evitando errores de encoding
                    # y asegurando comparibilidad máxima.
                    json.dump(data, f, indent=1, ensure_ascii=True)
                    f.write('\n')
                
                # Si todo salió bien, reemplazar archivo original
                os.replace(temp_file_path, file_path)
                
            except Exception as write_error:
                print(f"❌ Error escribiendo {filename}: {write_error}")
                if os.path.exists(temp_file_path):
                    os.remove(temp_file_path)
                
        except Exception as e:
            print(f"❌ Error procesando {filename}: {e}")

def main():
    # Force stdin/stdout to utf-8 just in case
    if hasattr(sys, 'stdout') and hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8')
        
    print("Iniciando estandarización de notebooks...")
    for level in LEVEL_ORDER:
        try:
            process_level(level)
        except Exception as e:
            print(f"Error procesando nivel {level}: {e}")
    print("¡Proceso completado!")

if __name__ == '__main__':
    main()
