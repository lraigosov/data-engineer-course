# Guía de instalación

Esta guía describe los entornos que el repositorio declara y valida. La fuente
de verdad para versiones compatibles es `pyproject.toml`; los archivos de
`locks/` fijan instalaciones reproducibles.

## Requisitos

- Git.
- Python 3.11, 3.12 o 3.13 de 64 bits.
- `pip` actualizado; los grupos de dependencias requieren `pip` 25.1 o posterior.
- Docker Desktop o Docker Engine, solo si se usará el entorno aislado.

No se admite Python 3.10 o anterior. Tampoco se ha declarado compatibilidad con
Python 3.14.

## Instalación local reproducible

Clona el repositorio y crea un entorno virtual llamado `.venv`:

```bash
git clone https://github.com/lraigosov/data-engineer-course.git
cd data-engineer-course
python -m venv .venv
```

Actívalo en Linux o macOS:

```bash
source .venv/bin/activate
```

En PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Actualiza `pip` y selecciona el lock que coincide con el intérprete:

```bash
python -m pip install --upgrade pip
python -m pip install -r locks/py3.11.txt
```

Sustituye el archivo por `locks/py3.12.txt` o `locks/py3.13.txt` cuando
corresponda. Esos locks contienen el entorno mínimo de desarrollo y CI.

Para JupyterLab y las dependencias educativas completas se mantiene un lock
validado con Python 3.11:

```bash
python -m pip install -r locks/docker-py3.11.txt
jupyter lab
```

## Perfiles opcionales

Los grupos se declaran en `pyproject.toml` y no se instalan por defecto.

| Grupo | Propósito |
| --- | --- |
| `dev` | Pruebas, lint y herramientas de notebooks |
| `notebooks` | JupyterLab, visualización, calidad y APIs locales |
| `cloud-aws` | SDK de AWS |
| `cloud-gcp` | BigQuery y Cloud Storage |
| `cloud-azure` | Identidad, Blob Storage y Data Lake Storage |
| `databases` | DuckDB, PostgreSQL, MongoDB y Redis |
| `airflow` | Apache Airflow 3.3 |
| `spark` | PySpark y Delta Lake 4 |
| `genai` | SDK y herramientas GenAI usadas por el curso |
| `all` | Todos los anteriores salvo Airflow |

Ejemplo:

```bash
python -m pip install --group genai
```

No mezcles el grupo Airflow con `all`: se mantiene separado para reducir
conflictos y permitir un entorno dedicado.

## Docker

Construye y valida la imagen sin instalar Python en el host:

```bash
docker build -t data-engineer-course .
docker run --rm data-engineer-course
```

Para abrir JupyterLab con el repositorio montado:

```bash
docker compose up jupyter
```

Revisa `docker-compose.yml` antes de exponer puertos en una red compartida. Las
credenciales no forman parte de la imagen y no deben copiarse al repositorio.

## Verificación

Dentro del entorno activo, o con el mismo entorno Docker usado por CI:

```bash
python scripts/validate_notebook_code.py
python scripts/normalize_notebook_metadata.py --check
pytest -q
python scripts/execute_notebooks.py --config config/notebooks-ci.txt
```

El estado documentado al 26 de agosto de 2026 es: 53 notebooks estructuralmente
válidos, 17 pruebas automatizadas y un notebook local en la allowlist de
ejecución. La validación estructural no sustituye la ejecución de notebooks que
dependen de nube, bases externas o APIs pagas.

## Solución de problemas

- Confirma `python --version`; debe estar entre 3.11 y 3.13.
- Confirma que `python -m pip --version` apunta a `.venv`.
- Si un lock no coincide con tu versión, no fuerces la instalación: usa el lock
  correcto o el contenedor.
- Si una celda requiere un servicio externo, consulta el README del nivel y usa
  credenciales de desarrollo con privilegios mínimos.
- Si Jupyter usa otro intérprete, selecciona el kernel de `.venv`.

Consulta también la [arquitectura del repositorio](arquitectura.md) y las
[preguntas frecuentes](faq.md).
