# Guía de contribución

Gracias por mejorar el curso. Esta guía define el mínimo necesario para que un
cambio sea verificable y consistente con el repositorio.

## Preparar el entorno

Se admiten Python 3.11, 3.12 y 3.13. Crea `.venv` y usa el lock correspondiente:

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r locks/py3.11.txt
```

En PowerShell, la activación es `.\.venv\Scripts\Activate.ps1`. Consulta la
[guía de instalación](docs/guia_instalacion.md) para Jupyter, Docker y perfiles
opcionales.

## Alcance de una contribución

- Mantén cada cambio enfocado y explica el problema que resuelve.
- No incluyas credenciales, `.env`, datos personales ni resultados de clientes.
- Distingue ejemplos simulados, resultados medidos y afirmaciones respaldadas.
- Añade o actualiza pruebas cuando cambie comportamiento ejecutable.
- Actualiza README, arquitectura, referencias y changelog cuando el cambio los
  afecte.

## Notebooks

- Conserva un ID nbformat válido y único en cada celda.
- Asegura que el código tenga sintaxis válida como archivo Python.
- Evita dependencias implícitas del estado de ejecución.
- Limpia secretos y datos sensibles de inputs, outputs y metadata.
- No afirmes que un notebook fue ejecutado si solo pasó validación estática.
- Si requiere servicios externos, documenta prerrequisitos, costos variables y
  una alternativa local cuando exista.

## Código Python

- Escribe funciones pequeñas, con nombres claros y errores accionables.
- Usa type hints y docstrings donde aclaren contratos públicos.
- No captures excepciones genéricas sin conservar contexto.
- Haz deterministas las pruebas; simula red, tiempo y servicios externos cuando
  no sean el objetivo de una prueba de integración explícita.

## Documentación

- Usa español claro, enlaces relativos para archivos del repositorio y fuentes
  primarias para afirmaciones técnicas.
- No copies precios, límites o versiones externas sin fecha y contexto.
- Usa tablas para comparaciones homogéneas, no para prosa extensa.
- Añade lenguaje al bloque cercado, por ejemplo `bash`, `python` o `text`.
- Mantén un único encabezado H1 por documento y una jerarquía sin saltos.

Los diagramas deben usar bloques `mermaid`, reflejar únicamente componentes
existentes e incluir `accTitle` y `accDescr`. Valida el documento de arquitectura
con una versión fijada de Mermaid CLI:

```bash
npx --yes @mermaid-js/mermaid-cli@11.16.0 --input docs/arquitectura.md --output arquitectura-rendered.md
```

El resultado renderizado es temporal y no se añade al repositorio.

## Validación local

Ejecuta dentro del entorno virtual del proyecto:

```bash
python -m compileall -q scripts tests
ruff check scripts tests --select E9,F63,F7,F82
python scripts/validate_notebook_code.py
python scripts/normalize_notebook_metadata.py --check
pytest -q
python scripts/execute_notebooks.py --config config/notebooks-ci.txt
```

Para Markdown, el repositorio incluye `.markdownlint-cli2.yaml`:

```bash
npx --yes markdownlint-cli2@0.23.0 "**/*.md"
```

Verifica también que cada enlace local exista y que GitHub pueda renderizar los
diagramas Mermaid. CI ejecuta cuatro controles independientes; consulta el
[diagrama de CI](docs/arquitectura.md#pipeline-de-calidad).

## Propuesta y revisión

En la descripción del cambio incluye:

- problema y alcance;
- archivos o notebooks afectados;
- comandos de validación y resultados;
- dependencias o infraestructura externa utilizada;
- capturas o logs cuando la evidencia no pueda reproducirse en CI.

Una revisión debe comprobar funcionalidad, evidencia, seguridad, compatibilidad
con Python soportado y coherencia documental. Los criterios educativos están en
las [rúbricas](docs/rubricas.md).

## Licencias

Al contribuir aceptas que el código se publique bajo MIT y el contenido
educativo bajo CC BY 4.0, según `LICENSE` y `LICENSE-CONTENT.md`. Solo incorpora
material que puedas licenciar y atribuye las fuentes cuando corresponda.
