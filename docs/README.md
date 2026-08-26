# Documentación del curso

Este directorio reúne la documentación operativa, académica y de arquitectura
del repositorio. El estado descrito aquí corresponde al árbol local validado el
26 de agosto de 2026.

## Mapa documental

| Documento | Audiencia | Propósito |
| --- | --- | --- |
| [README principal](../README.md) | Toda la comunidad | Alcance, ruta del curso y comienzo rápido |
| [Guía de instalación](guia_instalacion.md) | Estudiantes y contribuidores | Entornos soportados, instalación y diagnóstico |
| [Arquitectura](arquitectura.md) | Contribuidores y mantenedores | Componentes reales, dependencias y CI |
| [Roadmap](roadmap.md) | Estudiantes e instructores | Secuencia y resultados de aprendizaje |
| [Rúbricas](rubricas.md) | Instructores y estudiantes | Criterios y evidencias de evaluación |
| [Referencias](referencias.md) | Toda la comunidad | Fuentes oficiales y lecturas primarias |
| [Preguntas frecuentes](faq.md) | Toda la comunidad | Respuestas operativas breves |
| [Guía de contribución](../CONTRIBUTING.md) | Contribuidores | Flujo de cambios y controles de calidad |
| [Diseño original](DISENO_ORIGINAL.md) | Mantenedores | Registro histórico; no representa por sí solo el estado actual |

## Estado verificable

| Control | Alcance actual | Comando fuente de verdad |
| --- | ---: | --- |
| Sintaxis de notebooks | 53 notebooks, 479 celdas de código | `python scripts/validate_notebook_code.py` |
| Metadata nbformat | 1.505 celdas con ID | `python scripts/normalize_notebook_metadata.py --check` |
| Ejecución determinista | 1 notebook allowlisted | `python scripts/execute_notebooks.py` |
| Pruebas automatizadas | 17 pruebas | `pytest tests -q` |
| Lint crítico | `scripts/` y `tests/` | `ruff check scripts tests --select E9,F63,F7,F82` |

“Contenido completo” significa que los 53 notebooks planificados están
escritos. No significa que todos puedan ejecutarse sin credenciales, servicios
cloud, bases de datos, Kafka, Spark o APIs externas. La diferencia entre
validación estática y ejecución está descrita en
[Arquitectura y controles](arquitectura.md#controles-de-calidad).

## Convenciones documentales

- Usar enlaces relativos para archivos del repositorio.
- Indicar el lenguaje en todos los bloques de código.
- Mantener una fila de encabezado y separador en cada tabla.
- Reservar Mermaid para relaciones o secuencias que resulten menos claras en
  prosa.
- Añadir `accTitle` y `accDescr` a cada diagrama Mermaid.
- No presentar una tecnología como instalada si no aparece en
  `pyproject.toml`, un archivo de entrada de `requirements/` o un lock.
- Fechar las afirmaciones volátiles sobre modelos, certificaciones o servicios
  y enlazar su documentación oficial.

## Fuentes de verdad

Cuando dos documentos discrepen, prevalecen, en este orden:

1. Código, pruebas y workflows ejecutables.
2. `pyproject.toml`, `requirements/` y `locks/`.
3. Este índice y la guía de arquitectura.
4. README y guías por nivel.
5. `DISENO_ORIGINAL.md`, que se conserva como documento histórico.
