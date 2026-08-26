# Preguntas frecuentes

## ¿Qué versiones de Python son compatibles?

Python 3.11, 3.12 y 3.13. `pyproject.toml` declara `>=3.11,<3.14` y CI prueba las
tres versiones. Python 3.8 dejó de ser el baseline del proyecto.

## ¿Qué archivo de dependencias debo usar?

Para contribuir o ejecutar CI localmente, instala el lock correspondiente a tu
versión: `locks/py3.11.txt`, `locks/py3.12.txt` o `locks/py3.13.txt`. Para el
entorno educativo completo con Jupyter usa Python 3.11 y
`locks/docker-py3.11.txt`. `requirements.txt` es una entrada compatible y no la
fuente de reproducibilidad.

## ¿Por qué hay grupos en `pyproject.toml`?

Evitan instalar simultáneamente dependencias grandes o incompatibles. Con
`pip` 25.1 o posterior puedes instalar, por ejemplo,
`python -m pip install --group cloud-gcp`. Airflow se mantiene en un grupo
separado incluso del grupo `all`.

## ¿Todos los notebooks se ejecutan en CI?

No. CI valida la estructura y sintaxis de los 53 notebooks, pero solo ejecuta
los archivos locales enumerados en `config/notebooks-ci.txt`. Los ejercicios que
requieren nube, Kafka, bases de datos o APIs externas necesitan infraestructura
y credenciales fuera de CI.

## ¿Cómo ejecuto las verificaciones del repositorio?

```bash
ruff check scripts tests
python scripts/validate_notebook_code.py
python scripts/normalize_notebook_metadata.py --check
pytest -q
python scripts/execute_notebooks.py --config config/notebooks-ci.txt
```

La comprobación de metadata exige IDs de celda únicos y válidos conforme a
nbformat 4.5. El normalizador solo modifica archivos cuando se invoca sin
`--check`.

## ¿Qué significa que el contenido esté completo?

Significa que existen los 53 notebooks planificados. No significa que cada
integración externa haya sido ejecutada en CI. Las rúbricas exigen evidencia
adicional cuando una actividad depende de servicios externos.

## ¿Necesito cuentas cloud o claves GenAI?

No para leer el material ni para las validaciones locales. Sí para las celdas
que llamen explícitamente a esos servicios. Usa cuentas de desarrollo,
privilegios mínimos, cuotas y límites de gasto. Nunca confirmes archivos `.env`
ni credenciales reales.

## ¿Los notebooks son una forma de despliegue a producción?

No en este repositorio. Se usan para aprendizaje y experimentación. Los
componentes reutilizables viven en `scripts/`, con pruebas en `tests/`; un
despliegue real requiere empaquetado, secretos, observabilidad y controles de
operación acordes al entorno.

## ¿Cómo valido un diagrama Mermaid?

GitHub renderiza bloques cercados con el identificador `mermaid`. Para una
validación local reproducible de la arquitectura:

```bash
npx --yes @mermaid-js/mermaid-cli@11.16.0 --input docs/arquitectura.md --output arquitectura-rendered.md
```

El archivo renderizado es temporal y no debe confirmarse. Los diagramas fuente
están en `docs/arquitectura.md` y contienen título y descripción accesibles.

## ¿Dónde está la documentación vigente?

El [índice documental](README.md) señala la audiencia y fuente de verdad de cada
documento. `DISENO_ORIGINAL.md` conserva el planteamiento histórico y no debe
usarse como guía de instalación actual.
