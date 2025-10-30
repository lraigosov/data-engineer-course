# 🛠️ Guía de Instalación - Curso de Ingeniería de Datos

## Requisitos del Sistema

### Requisitos Mínimos
- **SO:** Windows 10+, macOS 10.14+, o Ubuntu 18.04+
- **Python:** 3.8 o superior
- **RAM:** 4GB mínimo (8GB recomendado)
- **Almacenamiento:** 2GB espacio libre
- **Conexión:** Internet estable para descargas

### Requisitos Recomendados
- **RAM:** 8GB o más
- **Almacenamiento:** 5GB espacio libre
- **Procesador:** Quad-core o superior
- **GPU:** Opcional para notebooks de ML

## Instalación Paso a Paso

### 1. Instalación de Python

#### Windows
```powershell
# Opción 1: Descargar de python.org
# Visita https://python.org/downloads/ y descarga Python 3.8+

# Opción 2: Usando Chocolatey
choco install python

# Opción 3: Usando Microsoft Store
# Busca "Python 3.9" en Microsoft Store
```

#### macOS
```bash
# Opción 1: Usando Homebrew (recomendado)
brew install python@3.9

# Opción 2: Descargar de python.org
# Visita https://python.org/downloads/
```

#### Linux (Ubuntu/Debian)
```bash
sudo apt update
sudo apt install python3.9 python3.9-pip python3.9-venv
```

### 2. Verificación de Python
```bash
python --version  # Debe mostrar 3.8 o superior
pip --version      # Debe estar instalado
```

### 3. Clonación del Repositorio
```bash
# Clona el repositorio
git clone <url-del-repositorio>
cd curso_ingenieria_datos

# O descarga el ZIP desde GitHub
```

### 4. Creación del Entorno Virtual

#### Windows (CMD/PowerShell)
```cmd
python -m venv venv
venv\Scripts\activate
```

#### Windows (Git Bash)
```bash
python -m venv venv
source venv/Scripts/activate
```

#### macOS/Linux
```bash
python3 -m venv venv
source venv/bin/activate
```

### 5. Instalación de Dependencias
```bash
# Actualizar pip
pip install --upgrade pip

# Instalar dependencias del curso
pip install -r requirements.txt

# Verificar instalación
pip list
```

### 6. Configuración de Variables de Entorno

#### Crear archivo de credenciales
```bash
# Copia el archivo de ejemplo
cp config/credentials.example config/credentials.yaml

# Edita con tus credenciales (opcional para empezar)
```

#### Variables de entorno (opcional)
```bash
# Windows
set PYTHONPATH=%cd%
set CURSO_ENV=development

# macOS/Linux
export PYTHONPATH=$(pwd)
export CURSO_ENV=development
```

### 7. Instalación de Jupyter

#### Jupyter Notebook (básico)
```bash
pip install jupyter
jupyter notebook
```

#### JupyterLab (recomendado)
```bash
pip install jupyterlab
jupyter lab
```

#### Extensiones útiles
```bash
# Extensiones para JupyterLab
pip install jupyterlab-git
pip install jupyterlab_code_formatter
pip install jupyterlab-lsp
jupyter labextension install @jupyterlab/toc
```

### 8. Configuración de Base de Datos (Opcional)

#### PostgreSQL Local
```bash
# Windows (usando Chocolatey)
choco install postgresql

# macOS (usando Homebrew)
brew install postgresql
brew services start postgresql

# Ubuntu/Debian
sudo apt install postgresql postgresql-contrib
sudo systemctl start postgresql
```

#### Configuración inicial
```sql
-- Conectar como superusuario
sudo -u postgres psql

-- Crear base de datos y usuario
CREATE DATABASE curso_data_engineering;
CREATE USER estudiante WITH PASSWORD 'tu_password';
GRANT ALL PRIVILEGES ON DATABASE curso_data_engineering TO estudiante;
```

## Verificación de la Instalación

### 1. Prueba de Python y Jupyter
```bash
# Activar entorno virtual
source venv/bin/activate  # Linux/Mac
# o
venv\Scripts\activate     # Windows

# Test rápido
python -c "import pandas, numpy, matplotlib; print('¡Todo funciona!')"

# Iniciar Jupyter
jupyter lab
```

### 2. Ejecutar Notebook de Prueba
```bash
# Navegar a la carpeta de notebooks
cd notebooks/nivel_junior

# Abrir el primer notebook
jupyter notebook 01_introduccion_ingenieria_datos.ipynb
```

### 3. Validar Conexiones (Opcional)
```python
# En un notebook, ejecutar:
import psycopg2
import requests

# Test conexión a DB (si configuraste PostgreSQL)
try:
    conn = psycopg2.connect(
        host="localhost",
        database="curso_data_engineering",
        user="estudiante",
        password="tu_password"
    )
    print("✅ Base de datos conectada")
    conn.close()
except:
    print("❌ Error de conexión a DB (opcional)")

# Test conexión a internet
try:
    response = requests.get("https://api.github.com")
    print("✅ Conexión a internet OK")
except:
    print("❌ Error de conexión a internet")
```

## Solución de Problemas Comunes

### Error: "python no se reconoce como comando"
```bash
# Windows: Agregar Python al PATH
# 1. Buscar "Variables de entorno" en el menú inicio
# 2. Agregar la ruta de Python a PATH
# Ejemplo: C:\Python39\Scripts\;C:\Python39\
```

### Error: "pip install falla"
```bash
# Actualizar pip
python -m pip install --upgrade pip

# Usar cache limpio
pip install --no-cache-dir -r requirements.txt

# Si falla, instalar uno por uno
pip install pandas numpy matplotlib jupyter
```

### Error: "Jupyter no inicia"
```bash
# Regenerar configuración
jupyter --config-dir
jupyter notebook --generate-config

# Limpiar cache
jupyter lab clean
jupyter lab build
```

### Error: "ModuleNotFoundError"
```bash
# Verificar entorno virtual activo
which python  # Debe apuntar a tu venv

# Reinstalar en el entorno correcto
pip install -r requirements.txt
```

### Problemas de Memoria
```bash
# Aumentar memoria para Jupyter
export JUPYTER_MEMORY_LIMIT=2G

# Configurar swap en Linux
sudo fallocate -l 2G /swapfile
sudo chmod 600 /swapfile
sudo mkswap /swapfile
sudo swapon /swapfile
```

## Configuración Avanzada (Opcional)

### Docker (Para entorno consistente)
```bash
# Construir imagen
docker build -t curso-data-engineering .

# Ejecutar contenedor
docker run -p 8888:8888 -v $(pwd):/workspace curso-data-engineering
```

### Configuración de IDE

#### VS Code
```bash
# Instalar extensiones recomendadas
code --install-extension ms-python.python
code --install-extension ms-toolsai.jupyter
code --install-extension ms-vscode.vscode-json
```

#### PyCharm
- Configurar intérprete: Archivo > Configuraciones > Python Interpreter
- Seleccionar el venv creado
- Habilitar soporte para Jupyter

### Scripts de Automatización
```bash
# Crear script de setup (setup.sh)
#!/bin/bash
python -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
cp config/credentials.example config/credentials.yaml
echo "¡Setup completado!"
```

## Soporte Técnico

### Recursos de Ayuda
- **Documentación oficial:** docs/
- **Issues de GitHub:** Reportar problemas técnicos
- **FAQ:** docs/faq.md
- **Comunidad:** Foro de discusión del proyecto

### Contacto
- **Email técnico:** soporte@curso-data-engineering.com
- **GitHub Issues:** Para bugs y mejoras
- **Discord/Slack:** Canal de la comunidad

---

¡Listo para comenzar tu viaje en Ingeniería de Datos! 🚀