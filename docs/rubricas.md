# 📋 Rúbricas de Evaluación del Curso

**Autor**: Luis J. Raigoso V. (LJRV) - [@lraigosov](https://github.com/lraigosov)

---

## 🎯 Propósito de este documento

Desde su diseño original (ver [`docs/DISENO_ORIGINAL.md`](DISENO_ORIGINAL.md)), el curso contempla una **"Evaluación corta (quiz o mini-proyecto automatizado)"** al cierre de cada módulo. En la práctica, lo único que existe hoy son los checklists narrativos de **"Objetivos de Aprendizaje"** (✅) en [`docs/roadmap.md`](roadmap.md) — que confirman que un tema fue *cubierto en el contenido*, no que un estudiante lo *domina*.

Este documento formaliza esos checklists en **criterios evaluables con peso y niveles de desempeño**, uno por nivel del curso (Junior, Mid, Senior, GenAI). No reemplaza los Objetivos de Aprendizaje — los traduce en algo calificable: qué se evalúa, cuánto pesa, qué distingue un desempeño insuficiente de uno sobresaliente, y qué evidencia concreta debe entregar el estudiante (o revisar el instructor/mentor) para calificar cada criterio.

> ⚠️ El módulo **Negocio LATAM** no tiene proyectos integradores (ver [`README.md`](../README.md)) y por tanto no se incluye una rúbrica formal; sus notebooks son de aplicación conceptual y estudio de casos sectoriales, no de entrega evaluable.

---

## 📘 Nivel Junior - Fundamentos

### 🎯 Objetivo del nivel

Formar la base de un Data Engineer: programar en Python para manipular datos, consultar bases relacionales con SQL, limpiar y visualizar datasets, usar Git en equipo, y construir un primer pipeline ETL funcional de extremo a extremo.

### 📐 Criterios de evaluación

| Criterio | Peso (%) | Insuficiente | Competente | Sobresaliente |
|---|---|---|---|---|
| Python para datos (estructuras, comprensiones, manejo de errores) | 15% | Código con errores no controlados, uso incorrecto de estructuras de datos básicas | Resuelve ejercicios con estructuras y manejo de excepciones correctos | Código idiomático, reutilizable, con manejo robusto de casos borde |
| Pandas y NumPy | 15% | Operaciones básicas fallan o producen resultados incorrectos | Lee, transforma y combina DataFrames correctamente | Usa vectorización, `groupby`/`merge` avanzados y optimiza operaciones costosas |
| SQL básico e intermedio (SELECT, JOIN, GROUP BY, subconsultas) | 15% | Consultas simples con errores de sintaxis o lógica | Escribe JOINs, agregaciones y subconsultas correctas sobre SQLite | Usa CTEs, subconsultas anidadas y diseña un modelo de datos coherente |
| Limpieza, calidad y visualización de datos | 10% | No detecta nulos/duplicados ni produce gráficos legibles | Aplica limpieza estándar (nulos, tipos, duplicados) y grafica hallazgos clave | Justifica decisiones de limpieza con evidencia y comunica insights con storytelling visual |
| Control de versiones con Git | 10% | Commits ausentes, mensajes vacíos o todo en un solo commit | Historial de commits atómicos con mensajes descriptivos y uso de `.gitignore` | Usa branches, resuelve conflictos y sigue un flujo de colaboración (PR/merge) |
| APIs y web scraping | 10% | No maneja errores HTTP ni rate limiting | Consume APIs REST y extrae datos con BeautifulSoup respetando buenas prácticas | Implementa reintentos, autenticación y scraping ético con validación de datos extraídos |
| Proyecto Integrador 1 (ETL completo: API → Pandas → SQLite) | 12.5% | Falta alguna etapa del ETL o el pipeline no ejecuta de inicio a fin | Extrae, transforma y carga datos correctamente con validaciones básicas | Pipeline modular, con logging, manejo de errores y datos validados contra reglas de calidad |
| Proyecto Integrador 2 (pipeline multi-fuente con scheduler) | 12.5% | Pipeline no integra todas las fuentes o no es reproducible | Combina múltiples fuentes, limpia, almacena y genera reporting básico | Incluye scheduling real, manejo de fallos y visualizaciones que respaldan una decisión de negocio |

### ✅ Umbral de aprobación

**70% ponderado**, con al menos nivel **"Competente" en ambos proyectos integradores** (no promedian por debajo de ese nivel aunque el resto del puntaje lo compense).

### 📁 Evidencia requerida

- Notebooks **ejecutados de principio a fin**, con outputs, tablas y gráficos visibles en las celdas (el contenido escrito sin ejecutar no cuenta como evaluado — ver la nota del `README.md` sobre "contenido escrito" vs. "ejecución verificada").
- Repositorio Git del estudiante con historial de commits real (no un único commit de "subida final").
- Carpeta/repositorio de los dos proyectos integradores, incluyendo el dataset de salida generado por el pipeline.

---

## 🔧 Nivel Mid - Pipelines y Automatización

### 🎯 Objetivo del nivel

Diseñar, orquestar y desplegar pipelines de datos productivos: orquestación con Airflow, streaming con Kafka, integración con servicios cloud multi-proveedor, bases de datos SQL/NoSQL, prácticas de DataOps/CI-CD, y exposición de datos vía APIs.

### 📐 Criterios de evaluación

| Criterio | Peso (%) | Insuficiente | Competente | Sobresaliente |
|---|---|---|---|---|
| Orquestación con Apache Airflow (DAGs, tasks, dependencias) | 15% | DAG no ejecuta o tareas sin dependencias correctas | DAG funcional con tasks, dependencias y monitoreo básico en la UI | Incluye retries, sensores, Deadline Alerts y alertas ante fallos |
| Streaming con Kafka | 12% | Productor/consumidor no procesa mensajes de forma confiable | Implementa productores/consumidores con esquema y manejo de errores | Aplica particionado, reintentos y patrones de consumo idempotente |
| Servicios cloud multi-proveedor (AWS/GCP/Azure) | 13% | Solo describe servicios sin ejecutar ejemplos prácticos | Ejecuta casos prácticos en al menos un proveedor (S3/Glue/Athena, BigQuery/Dataflow o ADLS/Synapse) | Compara trade-offs entre proveedores y justifica elección según caso de uso |
| Bases de datos relacionales y NoSQL (PostgreSQL/MongoDB) | 10% | Modelado incorrecto o consultas ineficientes | Modela y consulta correctamente en SQL y documental, con índices básicos | Diseña estrategias de carga (upsert, idempotencia) y optimiza índices |
| DataOps: testing y CI/CD | 10% | Sin pruebas de datos ni pipeline de CI | Usa Great Expectations/Pandera y pre-commit hooks básicos | Integra tests de datos y calidad dentro de un pipeline de GitHub Actions funcional |
| Conectores avanzados y servicios de datos (REST/GraphQL/SFTP, FastAPI) | 10% | Conectores sin manejo de paginación/errores | Implementa conectores robustos con backoff y valida payloads | Expone datos vía FastAPI con validación Pydantic y maneja múltiples protocolos de origen |
| Optimización SQL y particionado | 10% | No usa `EXPLAIN`/`ANALYZE` ni particiona datos | Analiza planes de consulta y aplica particionado razonable | Justifica estrategia de particionado e índices con métricas de mejora medibles |
| Proyecto Integrador 1 (API → validación → DB → Parquet, orquestado con Airflow) | 10% | Pipeline incompleto o no orquestado | Pipeline completo orquestado con Airflow y validaciones básicas | Incluye alertas, monitoreo y manejo de fallos ante fuentes no disponibles |
| Proyecto Integrador 2 (streaming Kafka → lake con idempotencia) | 10% | Sin garantía de idempotencia o pipeline no reproducible | Pipeline streaming funcional con checkpoints e idempotencia | Incluye métricas de throughput/latencia y simulación de fallos recuperables |

### ✅ Umbral de aprobación

**70% ponderado**, con al menos nivel **"Competente" en ambos proyectos integradores**.

### 📁 Evidencia requerida

- Notebooks ejecutados con outputs visibles (logs de Airflow, mensajes de Kafka consumidos, resultados de queries).
- Capturas de pantalla o logs de ejecución de la UI de Airflow (DAG runs) y de la CI de GitHub Actions, cuando aplique.
- Repositorio del proyecto integrador con código, tests (`tests/unit`, `tests/integration`) y evidencia de que los tests pasan.
- No se acepta un DAG o script sin evidencia de al menos una corrida real (el contenido escrito sin ejecutar no cuenta como evaluado).

---

## 🚀 Nivel Senior - Arquitectura y Gobernanza

### 🎯 Objetivo del nivel

Diseñar y operar arquitecturas de datos modernas (lakehouse, Lambda/Kappa/Data Mesh) con gobernanza, calidad, seguridad, FinOps y observabilidad de nivel enterprise, integrando pipelines de ML y feature stores.

### 📐 Criterios de evaluación

| Criterio | Peso (%) | Insuficiente | Competente | Sobresaliente |
|---|---|---|---|---|
| Data Governance y calidad (DAMA-DMBOK, linaje) | 12% | No aplica dimensiones de calidad ni documenta linaje | Implementa validaciones automáticas y documenta linaje básico | Diseña un marco de gobernanza con stewardship y métricas de calidad medibles |
| Data Lakehouse (Delta/Iceberg, catálogos) | 12% | No distingue lakehouse de un data lake tradicional | Implementa Parquet particionado con catálogo (Hive/Glue) funcional | Justifica elección Delta vs. Iceberg y diseña esquema de evolución de tablas |
| Spark Streaming avanzado | 10% | Streaming sin manejo de estado ni ventanas | Implementa ventanas temporales, watermarks y agregaciones incrementales | Integra con catálogo y optimiza rendimiento bajo carga sostenida |
| Arquitecturas modernas (Lambda, Kappa, Data Mesh) | 12% | Describe arquitecturas sin poder justificar cuándo usar cada una | Compara Lambda/Kappa/Data Mesh y elige una con justificación razonable | Diseña una arquitectura híbrida y argumenta trade-offs de costo, latencia y gobernanza |
| ML Pipelines y Feature Stores (MLOps) | 10% | Pipeline de features no reproducible ni versionado | Implementa pipeline ETL → features → training con feature store básico | Incluye versionado, monitoreo de drift y reentrenamiento automatizado |
| FinOps y optimización de costos cloud | 8% | No identifica costos ni propone optimizaciones | Aplica al menos dos estrategias de optimización (compute/storage) con métricas | Presenta análisis costo-beneficio con alertas de presupuesto y accountability por equipo |
| Seguridad y compliance | 8% | No aplica IAM ni cifrado | Aplica IAM de mínimo privilegio y cifrado at-rest/in-transit | Diseña controles de auditoría alineados a un marco (GDPR/HIPAA/SOC2) con evidencia de logging |
| Observabilidad y linaje de datos | 8% | Sin métricas ni trazabilidad del pipeline | Implementa logs estructurados, métricas y linaje básico (OpenLineage) | Define SLOs, dashboards y trazas distribuidas end-to-end |
| Proyecto Integrador 1 (plataforma de datos completa) | 10% | Faltan componentes críticos del checklist de la plataforma | Integra governance, lakehouse, orquestación y observabilidad de forma funcional | Cumple el checklist completo de componentes con evidencia de cada uno funcionando |
| Proyecto Integrador 2 (Data Mesh multi-dominio con feature store) | 10% | Dominios no desacoplados o sin gobernanza federada | Implementa arquitectura descentralizada con al menos dos dominios y feature store | Incluye contratos de datos entre dominios y ML training con features cross-domain |

### ✅ Umbral de aprobación

**70% ponderado**, con al menos nivel **"Competente" en ambos proyectos integradores**.

### 📁 Evidencia requerida

- Notebooks ejecutados con outputs visibles, incluyendo métricas, tablas de catálogo y resultados de validaciones de calidad.
- Diagramas de arquitectura (aunque sea conceptual/manual) que respalden las decisiones tomadas en cada proyecto integrador.
- Evidencia de configuración (IaC, YAML, scripts CLI) usada para reproducir la plataforma, no solo su descripción narrativa.
- Checklist de componentes del Proyecto Integrador 1 marcado con evidencia (captura, log o test) por cada ítem, no solo marcado como completo de palabra.

---

## 🤖 Nivel GenAI - IA Generativa para Ingeniería de Datos

### 🎯 Objetivo del nivel

Aplicar LLMs a tareas propias de ingeniería de datos: generación de SQL y código ETL desde lenguaje natural, RAG sobre documentación técnica, búsqueda semántica con embeddings, agentes autónomos, validación de calidad y generación de datos sintéticos — con criterio sobre costos y riesgos de producción.

### 📐 Criterios de evaluación

| Criterio | Peso (%) | Insuficiente | Competente | Sobresaliente |
|---|---|---|---|---|
| Fundamentos de LLMs e instrucciones | 12% | Instrucciones ambiguas sin estructura ni ejemplos | Aplica ejemplos, salidas estructuradas y criterios verificables | Diseña instrucciones robustas ante variaciones y documenta limitaciones del modelo |
| Generación SQL (NL2SQL) | 12% | Queries generadas sin validar ni sanitizar | Genera SQL desde lenguaje natural y valida sintaxis/semántica antes de ejecutar | Maneja esquemas complejos y previene inyección o queries destructivas |
| Generación automática de código ETL | 10% | Código generado no se ejecuta o requiere reescritura total | Genera pipelines ETL funcionales a partir de descripciones en lenguaje natural | Valida el código generado con tests y lo integra en un template reutilizable |
| RAG y vector stores | 12% | Recuperación de contexto irrelevante o respuestas alucinadas | Implementa RAG funcional con ChromaDB/FAISS sobre documentación real | Optimiza chunking/retrieval y mide calidad de respuestas frente a un baseline |
| Embeddings y búsqueda semántica | 10% | No distingue similitud semántica de coincidencia exacta | Implementa búsqueda por similitud y deduplicación básica | Aplica clustering/clasificación con embeddings y justifica métricas de distancia usadas |
| Agentes autónomos (LangGraph) | 10% | Agente sin control de loops ni herramientas definidas | Implementa agente con tools personalizadas y lógica de decisión básica | Agrega memoria, límites de iteración y manejo de fallos de herramientas |
| Validación de calidad con LLMs | 8% | No detecta anomalías semánticas más allá de reglas fijas | Usa LLMs para detectar anomalías e integrarlas con Great Expectations | Combina reglas determinísticas y LLM con criterio explícito de cuándo usar cada una |
| Síntesis y aumento de datos | 6% | Datos sintéticos no preservan distribución ni anonimizan PII | Genera datos sintéticos que preservan distribuciones estadísticas clave | Aplica anonimización inteligente y valida fidelidad estadística frente a datos reales |
| Proyecto Integrador 1 (chatbot con RAG + Text-to-SQL) | 10% | Falta integración entre RAG y generación SQL, o respuestas no confiables | Chatbot funcional que combina RAG y Text-to-SQL con interfaz operativa | Incluye manejo de errores, límites de alcance claros y medición de calidad de respuesta |
| Proyecto Integrador 2 (plataforma self-service con GenAI) | 10% | Generación de pipelines/documentación no reproducible | Plataforma genera pipelines y documentación automáticamente de forma funcional | Incluye agentes de mantenimiento/alertas y control de costos de API |

### ✅ Umbral de aprobación

**70% ponderado**, con al menos nivel **"Competente" en ambos proyectos integradores**.

### 📁 Evidencia requerida

- Dado que los notebooks de `nivel_genai/` requieren credenciales de API externas y **no corren en el pipeline de CI** (ver `README.md` y `.github/workflows/ci.yml`), la evidencia de ejecución debe incluirse explícitamente como capturas de pantalla, logs de la API o outputs guardados en el propio notebook — no basta con el código sin evidencia de haberse ejecutado.
- Notebooks con las respuestas/generaciones reales del modelo visibles (no placeholders ni celdas vacías).
- Registro de costos aproximados de uso de API por proyecto integrador (tokens/llamadas), acorde al objetivo de aprendizaje sobre "costos y optimización de APIs de IA".
- Repositorio del proyecto integrador con el código de agentes, prompts usados y configuración del vector store.

---

## 🔭 Alcance y evolución (v1)

Esta es la **versión 1** de las rúbricas: un estándar de calificación manual, pensado para que un instructor o mentor lo aplique directamente sobre las entregas del estudiante. Formaliza los checklists de "Objetivos de Aprendizaje" existentes en `docs/roadmap.md`, pero **no implementa automatización** — no hay quiz interactivo, no hay corrector automático de notebooks, no hay emisión de certificados.

Ese es precisamente el hueco que ya estaba anticipado en dos lugares del proyecto:

- La idea de una **"Evaluación corta (quiz o mini-proyecto automatizado)"** al final de cada módulo, planteada en `docs/DISENO_ORIGINAL.md` como parte de la metodología didáctica.
- El **"Sistema de evaluación automática y certificados"** listado como ítem futuro (v2.0.0) en `CHANGELOG.md`.

Esta rúbrica está diseñada para ser la base sobre la cual esa automatización se construya más adelante: los criterios y umbrales aquí definidos son el contrato que un corrector automático (o un quiz por módulo) debería replicar y verificar programáticamente, en lugar de depender exclusivamente de revisión humana. Hasta que esa automatización exista, esta es la referencia oficial para calificar el desempeño de un estudiante en el curso.
