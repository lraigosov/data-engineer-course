
# Proyecto de Ingeniería de Datos

## Estructura del Proyecto

```
.
├── data/
│   ├── raw/          # Datos crudos sin modificar
│   ├── processed/    # Datos procesados
│   └── external/     # Datos externos
├── notebooks/        # Jupyter notebooks para análisis
├── src/
│   ├── pipelines/    # Scripts de pipelines ETL
│   └── utils/        # Utilidades y funciones auxiliares
├── tests/            # Tests unitarios e integración
├── config/           # Archivos de configuración
├── docs/             # Documentación
├── logs/             # Archivos de log
├── outputs/          # Resultados y reportes
├── .gitignore
├── requirements.txt
└── README.md
```

## Instalación

```bash
# Clonar repositorio
git clone <url>
cd proyecto

# Crear entorno virtual
python -m venv venv
source venv/bin/activate  # Windows: venv\Scriptsctivate

# Instalar dependencias
pip install -r requirements.txt
```

## Uso

```bash
# Ejecutar pipeline principal
python src/pipelines/main_pipeline.py
```

## Contribuir

1. Crear rama: `git checkout -b feature/nueva-funcionalidad`
2. Hacer cambios y commit: `git commit -m "feat: descripción"`
3. Push: `git push origin feature/nueva-funcionalidad`
4. Crear Pull Request
