# Roadmap del curso

Este documento describe la ruta educativa existente y separa contenido escrito
de ejecución verificada. El inventario se comprobó en el repositorio el 26 de
agosto de 2026.

## Estado verificable

| Área | Notebooks escritos | Proyectos integradores |
| --- | ---: | ---: |
| Junior | 10 | 2 |
| Mid | 12 | 2 |
| Senior | 10 | 2 |
| GenAI | 11 | 2 |
| Negocio LATAM | 10 | 0 |
| **Total** | **53** | **8** |

Controles automatizados actuales:

| Control | Cobertura |
| --- | --- |
| Sintaxis y estructura | 53 notebooks, 479 celdas de código |
| Metadata nbformat | 1.505 celdas con IDs únicos y válidos |
| Pruebas Python | 17 pruebas unitarias y de integración |
| Ejecución de notebooks en CI | 1 notebook local en allowlist |

La frase “contenido completo” se refiere a los 53 archivos escritos. La
ejecución integral de laboratorios con nube, Kafka, bases de datos o APIs GenAI
requiere entornos externos y evidencia adicional.

## Ruta recomendada

1. **Junior (6–8 semanas):** Python, pandas, SQL, calidad, visualización, Git,
   APIs y dos proyectos ETL.
2. **Mid (8–10 semanas):** Airflow, Kafka, tres proveedores cloud, bases de
   datos, DataOps, conectores, optimización, FastAPI y dos proyectos.
3. **Senior (10–12 semanas):** gobierno, lakehouse, streaming, arquitecturas,
   ML pipelines, FinOps, seguridad, observabilidad y dos proyectos.
4. **GenAI (4–6 semanas):** LLM, NL2SQL, generación de ETL, RAG, embeddings,
   agentes, calidad, datos sintéticos y dos proyectos.
5. **Negocio LATAM (4–6 semanas):** estrategia y diez contextos sectoriales.

Las duraciones son una propuesta curricular, no una medición de finalización.
Cada estudiante debe adaptar el ritmo y demostrar los resultados según las
[rúbricas](rubricas.md).

## Criterios de avance

- Haber ejecutado las prácticas del nivel con evidencia revisable.
- Alcanzar el umbral definido en `docs/rubricas.md`.
- Separar simulaciones didácticas de resultados obtenidos en infraestructura
  real.
- Documentar supuestos, versiones, fuentes y limitaciones de cada proyecto.

## Evolución pendiente

Las siguientes iniciativas no están implementadas y no deben presentarse como
funcionalidad disponible:

- ampliar de forma segura la allowlist de ejecución de notebooks;
- automatizar parte de las rúbricas y evaluaciones;
- incorporar laboratorios de infraestructura reproducible para integraciones
  externas;
- medir cobertura educativa y accesibilidad con criterios acordados;
- publicar una política formal de versionado del contenido.

La prioridad de estas iniciativas se decide mediante issues y cambios
revisables. El [changelog](../CHANGELOG.md) registra lo que sí fue incorporado.
