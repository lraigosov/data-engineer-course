# Changelog

Todos los cambios notables en este proyecto serán documentados en este archivo.

El formato está basado en [Keep a Changelog](https://keepachangelog.com/es-ES/1.0.0/),
y este proyecto adhiere a [Semantic Versioning](https://semver.org/lang/es/).

## [1.0.0] - 2024-10-30

### Añadido
- Estructura inicial del proyecto
- Configuración base (settings.yaml, credentials.example)
- Documentación completa:
  - README.md principal
  - Guía de instalación
  - Roadmap del curso
  - Referencias y recursos
  - Guía de contribución
- Notebooks nivel Junior:
  - 01_introduccion_ingenieria_datos.ipynb
  - 02_python_manipulacion_datos.ipynb
- Notebooks nivel Mid:
  - 01_apache_airflow_fundamentos.ipynb
- Notebooks nivel Senior:
  - 01_data_governance_calidad.ipynb
- Scripts de utilidad:
  - simple_etl.py
  - data_transformations.py
- Archivos de configuración:
  - requirements.txt
  - .gitignore
  - LICENSE (MIT)
- README por nivel de curso

### Estructura de Carpetas
```
curso_ingenieria_datos/
├── config/
├── notebooks/
│   ├── nivel_junior/
│   ├── nivel_mid/
│   └── nivel_senior/
├── datasets/
│   ├── raw/
│   ├── processed/
│   └── external/
├── scripts/
│   ├── etl/
│   ├── transformaciones/
│   └── pipelines/
├── tests/
│   ├── unit/
│   └── integration/
└── docs/
```

## [Próximas Versiones]

### [1.1.0] - Planificado
- Notebooks adicionales nivel Junior (3-10)
- Datasets de ejemplo
- Tests automatizados
- CI/CD con GitHub Actions

### [1.2.0] - Planificado
- Notebooks adicionales nivel Mid (2-10)
- Integración con Docker
- Ejemplos de DAGs de Airflow completos

### [1.3.0] - Planificado
- Notebooks adicionales nivel Senior (2-10)
- Proyectos finales por nivel
- Sistema de evaluación automatizada

### [2.0.0] - Futuro
- Plataforma interactiva online
- Videos explicativos
- Foro de comunidad
- Certificados digitales

---

## Tipos de Cambios
- **Añadido** para funcionalidades nuevas
- **Cambiado** para cambios en funcionalidad existente
- **Obsoleto** para funcionalidades que pronto se eliminarán
- **Eliminado** para funcionalidades eliminadas
- **Corregido** para corrección de errores
- **Seguridad** en caso de vulnerabilidades