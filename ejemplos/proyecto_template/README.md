# Plantilla de proyecto de ingeniería de datos

Esta carpeta es un ejemplo de estructura; no es un servicio desplegado ni usa
automáticamente el entorno raíz del curso.

## Estructura propuesta

```text
.
├── config/       # Configuración sin secretos
├── data/
│   ├── raw/      # Datos fuente inmutables
│   └── processed/# Datos derivados reproducibles
├── docs/         # Decisiones y operación
├── notebooks/    # Exploración y prototipos
├── src/          # Paquete y pipelines reutilizables
├── tests/        # Pruebas unitarias e integración
├── .gitignore
├── pyproject.toml
└── README.md
```

Adapta la estructura al tamaño del proyecto. No crees directorios vacíos o
capas que no tengan una responsabilidad clara.

## Inicio

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e .
pytest -q
```

En PowerShell, activa el entorno con `.\.venv\Scripts\Activate.ps1`. Define en
el `pyproject.toml` del proyecto su versión mínima de Python, dependencias y
configuración de pruebas; no copies versiones del curso sin validarlas.

## Criterios mínimos

- configuración por entorno y secretos fuera de Git;
- pipelines idempotentes con logs y errores accionables;
- validación de entradas y outputs;
- pruebas deterministas y una integración continua reproducible;
- documentación de operación, ownership y recuperación.
