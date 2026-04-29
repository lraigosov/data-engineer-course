# 🗺️ Roadmap del Curso - Ingeniería de Datos

**Autor**: Luis J. Raigoso V. (LJRV) - [@lraigosov](https://github.com/lraigosov)

---

## 📊 Visión General

Este roadmap detalla la progresión completa del curso, desde fundamentos hasta nivel Senior, GenAI y aplicación sectorial en LATAM. El curso consta de **53 notebooks completados (100%)**, organizados en 5 módulos de especialización.

---

## 🎯 Estructura del Curso

| Nivel         | Notebooks | Estado | Duración Estimada |
|---------------|-----------|--------|-------------------|
| **Junior**    | 10        | ✅ 100% | 8-10 semanas      |
| **Mid**       | 12        | ✅ 100% | 10-12 semanas     |
| **Senior**    | 10        | ✅ 100% | 10-12 semanas     |
| **GenAI**     | 11        | ✅ 100% | 6-8 semanas       |
| **Negocio LATAM** | 10    | ✅ 100% | 4-6 semanas       |
| **TOTAL**     | **53**    | **✅ 100%** | **42-52 semanas** |

---

## 📘 Nivel Junior - Fundamentos (8-10 semanas)

### Notebooks Completados (10/10)

1. **01_introduccion_ingenieria_datos.ipynb** ✅
   - Rol del Data Engineer vs Data Scientist vs Data Analyst
   - Ecosistema de herramientas y tecnologías
   - Primer pipeline conceptual
   
2. **02_python_manipulacion_datos.ipynb** ✅
   - Estructuras de datos en Python (listas, diccionarios, sets)
   - Manejo de archivos CSV, JSON, XML
   - Comprensiones y generadores
   - Manejo de errores y excepciones

3. **03_pandas_fundamentos.ipynb** ✅
   - DataFrames y Series
   - Lectura y escritura de múltiples formatos
   - Indexación y selección de datos
   - Operaciones básicas de manipulación

4. **04_sql_basico.ipynb** ✅
   - SELECT, WHERE, JOIN, GROUP BY
   - Subconsultas y CTEs
   - SQLite y conexión desde Python
   - Modelado básico de datos

5. **05_limpieza_datos.ipynb** ✅
   - Detección y manejo de valores nulos
   - Identificación de duplicados
   - Conversión de tipos de datos
   - Normalización y estandarización

6. **06_visualizacion_datos.ipynb** ✅
   - Matplotlib para gráficos básicos
   - Seaborn para visualizaciones estadísticas
   - Tipos de gráficos apropiados por caso de uso
   - Storytelling con datos

7. **07_git_control_versiones.ipynb** ✅
   - Git básico: init, add, commit, push, pull
   - Branches y merge workflows
   - .gitignore para proyectos de datos
   - Colaboración en equipo con GitHub

8. **08_apis_web_scraping.ipynb** ✅
   - Consumo de APIs REST con requests
   - Autenticación y rate limiting
   - Web scraping ético con BeautifulSoup
   - Manejo de datos JSON y XML

9. **09_proyecto_integrador_1.ipynb** ✅
   - ETL completo: Extraer desde API
   - Transformar con Pandas
   - Cargar a SQLite

10. **10_proyecto_integrador_2.ipynb** ✅
    - Pipeline end-to-end con múltiples fuentes
    - Limpieza, validación y almacenamiento
    - Visualizaciones y reporting

### Objetivos de Aprendizaje Junior
- ✅ Comprender el rol y ecosistema del Data Engineer
- ✅ Dominar Python para manipulación de datos
- ✅ Trabajar eficientemente con Pandas y NumPy
- ✅ Fundamentos de SQL y bases de datos relacionales
- ✅ Control de versiones con Git y GitHub
- ✅ Construir pipelines ETL básicos
- ✅ Visualización de datos para insights

---

## 🔧 Nivel Mid - Pipelines y Cloud (10-12 semanas)

### Notebooks Completados (12/12)

1. **01_apache_airflow_fundamentos.ipynb** ✅
   - Conceptos de DAGs, Tasks, Operators
   - Instalación y configuración local
   - Primer DAG simple con dependencies
   - Web UI y monitoreo

2. **02_streaming_kafka.ipynb** ✅
   - Fundamentos de Kafka (topics, partitions, brokers)
   - Productores y consumidores con Python
   - Esquemas y serialización (Avro/JSON)
   - Patrones de consumo y reintentos

3. **03_cloud_aws.ipynb** ✅
   - S3 como data lake
   - AWS Glue (PySpark) para transformaciones
   - Athena para consultas SQL sobre S3
   - Lambda y EventBridge para triggers

3b. **03b_cloud_gcp.ipynb** ✅ 🆕
   - Cloud Storage con lifecycle management
   - BigQuery (serverless + optimización)
   - Dataflow con Apache Beam
   - Cloud Composer (Airflow managed)
   - Cloud Functions event-driven

3c. **03c_cloud_azure.ipynb** ✅ 🆕
   - ADLS Gen2 (hierarchical namespaces + ACLs POSIX)
   - Azure Synapse Analytics (dedicated + serverless SQL + Spark)
   - Azure Data Factory (ETL/ELT orchestration)
   - Azure Databricks (Delta Lake + Photon engine)
   - Azure Functions (múltiples triggers)

4. **04_bases_datos_postgresql_mongodb.ipynb** ✅
   - Conexión con SQLAlchemy (PostgreSQL) y PyMongo
   - Modelado relacional vs documental
   - Índices y optimización de queries
   - Estrategias de carga (batch, upsert, idempotencia)

5. **05_dataops_cicd.ipynb** ✅
   - Pruebas de datos con Great Expectations y Pandera
   - Pre-commit hooks (black, isort, flake8, pytest)
   - GitHub Actions para CI/CD
   - Data quality en pipelines

6. **06_conectores_avanzados_rest_graphql_sftp.ipynb** ✅
   - REST API con paginación, backoff y validación
   - GraphQL para consultas flexibles
   - SFTP con Paramiko (opcional)
   - Patrones de retry y error handling

7. **07_optimizacion_sql_particionado.ipynb** ✅
   - EXPLAIN/ANALYZE para análisis de queries
   - Índices y selectividad
   - Particionado (PostgreSQL y data lakes)
   - Pruning y almacenamiento columnar

8. **08_fastapi_servicios_datos.ipynb** ✅
   - FastAPI + Pydantic para CRUD de datos
   - Endpoints RESTful para ventas
   - Caché con Redis (opcional)
   - Testing con requests

9. **09_proyecto_integrador_1.ipynb** ✅
   - Pipeline: API → validación → DB → Parquet
   - Orquestación con Airflow (DAG completo)
   - Alertas y monitoreo básico

10. **10_proyecto_integrador_2.ipynb** ✅
    - Pipeline streaming: Kafka → validación → enriquecimiento → Parquet
    - Idempotencia con checkpoints
    - Métricas y consumidor/productor con simulación

### Objetivos de Aprendizaje Mid
- ✅ Orquestación de pipelines con Apache Airflow
- ✅ Procesamiento de streaming con Kafka
- ✅ **Cloud multi-proveedor (AWS, GCP, Azure) con notebooks prácticos**
- ✅ Bases de datos relacionales (PostgreSQL) y NoSQL (MongoDB)
- ✅ DataOps: testing, CI/CD, calidad de datos
- ✅ Conectores avanzados (REST, GraphQL, SFTP)
- ✅ Optimización de SQL y particionado
- ✅ Servicios de datos con FastAPI
- ✅ Proyectos integradores end-to-end

---

## 🚀 Nivel Senior - Arquitectura y Gobernanza (10-12 semanas)

### Notebooks Completados (10/10)

1. **01_data_governance_calidad.ipynb** ✅
   - Framework DAMA-DMBOK
   - Dimensiones de calidad de datos (exactitud, completitud, etc.)
   - Data Lineage y trazabilidad
   - Implementación de validaciones automáticas

2. **02_lakehouse_delta_iceberg.ipynb** ✅
   - Principios de Data Lakehouse
   - Catálogos de datos (Hive, Glue, Unity)
   - Práctica con Parquet particionado
   - Referencia a Delta Lake e Iceberg

3. **03_spark_streaming.ipynb** ✅
   - Structured Streaming con PySpark
   - Ventanas temporales y watermarks
   - Estado y agregaciones incrementales
   - Integración con catálogos

4. **04_arquitecturas_modernas.ipynb** ✅
   - Arquitectura Lambda (batch + stream)
   - Arquitectura Kappa (solo stream)
   - Arquitectura Delta (lakehouse)
   - Data Mesh: paradigma organizacional
   - Comparación y casos de uso

5. **05_ml_pipelines_feature_stores.ipynb** ✅
   - Pipelines de datos para ML (ETL → features → training)
   - Feature stores (Feast, Tecton)
   - MLOps: versionado, reentrenamiento, monitoreo
   - Integración con Airflow y Spark

6. **06_cost_optimization_finops.ipynb** ✅
   - FinOps: visibilidad, accountability, optimización
   - Estrategias de optimización (compute, storage, networking)
   - Métricas clave (USD/TB, utilización)
   - Alertas de presupuesto

7. **07_seguridad_compliance.ipynb** ✅
   - IAM y principio de mínimo privilegio
   - Cifrado at-rest e in-transit
   - Compliance (GDPR, HIPAA, SOC2)
   - Auditoría y logging de seguridad

8. **08_observabilidad_linaje.ipynb** ✅
   - Logs estructurados y centralización
   - Métricas (Prometheus, CloudWatch)
   - Trazas distribuidas
   - Linaje de datos (OpenLineage, DataHub)
   - SLOs y dashboards

9. **09_proyecto_integrador_1.ipynb** ✅
   - Plataforma completa: governance + lakehouse + orquestación
   - Streaming + batch con observabilidad
   - Compliance y seguridad integrados
   - Checklist de 18 componentes

10. **10_proyecto_integrador_2.ipynb** ✅
    - Data Mesh multi-dominio con feature store
    - Gobernanza federada y data products
    - ML training con features cross-domain
    - Arquitectura descentralizada

### Objetivos de Aprendizaje Senior
- ✅ Arquitecturas modernas (Lambda, Kappa, Delta, Data Mesh)
- ✅ Data Governance completo (DAMA-DMBOK)
- ✅ Data Lakehouse con Delta Lake e Iceberg
- ✅ Stream processing avanzado con Spark Streaming
- ✅ ML Pipelines y Feature Stores (MLOps)
- ✅ Cost Optimization y FinOps en cloud
- ✅ Seguridad y compliance (GDPR, HIPAA, SOC2)
- ✅ Observabilidad y linaje de datos
- ✅ Liderazgo técnico y diseño de plataformas enterprise

---

## 🤖 Nivel GenAI - IA Generativa para Datos (6-8 semanas)

### Notebooks Completados (11/11)

0. **00_comparacion_openai_gemini.ipynb** ✅
   - Comparación detallada OpenAI vs Google Gemini
   - Pricing, capacidades, límites
   - Casos de uso específicos para datos
   - Setup y configuración de ambas APIs

1. **01_fundamentos_llms_prompting.ipynb** ✅
   - Fundamentos de Large Language Models
   - Prompt engineering para tareas de datos
   - Few-shot learning y chain-of-thought
   - Best practices y limitaciones

2. **02_generacion_sql_nl2sql.ipynb** ✅
   - Text-to-SQL con LLMs
   - Validación y sanitización de queries
   - Manejo de esquemas complejos
   - Errores comunes y correcciones

3. **03_generacion_codigo_etl.ipynb** ✅
   - Generación automática de código ETL
   - Templates y patrones reutilizables
   - Validación de código generado
   - De descripción en lenguaje natural a pipeline ejecutable

4. **04_rag_documentacion_datos.ipynb** ✅
   - Retrieval-Augmented Generation (RAG)
   - Chatbot sobre documentación técnica
   - Vector stores (ChromaDB, FAISS)
   - Búsqueda semántica en catálogos de datos

5. **05_embeddings_similitud_datos.ipynb** ✅
   - Embeddings para representación de datos
   - Búsqueda por similitud semántica
   - Deduplicación inteligente de registros
   - Clustering y clasificación con embeddings

6. **06_agentes_automatizacion.ipynb** ✅
   - LangGraph para agentes autónomos
   - Agentes para automatización de tareas de datos
   - Herramientas (tools) personalizadas
   - Loops de decisión y memoria

7. **07_calidad_validacion_llm.ipynb** ✅
   - Validación de calidad de datos con LLMs
   - Detección de anomalías semánticas
   - Sugerencias de limpieza automática
   - Integración con Great Expectations

8. **08_sintesis_aumento_datos.ipynb** ✅
   - Generación de datos sintéticos con LLMs
   - Data augmentation para ML
   - Preservación de distribuciones estadísticas
   - Anonimización inteligente

9. **09_proyecto_integrador_1.ipynb** ✅
   - Chatbot empresarial sobre datos
   - RAG + Text-to-SQL integrados
   - Dashboard conversacional
   - Interface con Gradio/Streamlit

10. **10_proyecto_integrador_2.ipynb** ✅
    - Plataforma self-service con GenAI
    - Generación automática de pipelines
    - Documentación auto-generada
    - Agentes de mantenimiento y alertas inteligentes

### Objetivos de Aprendizaje GenAI
- ✅ Fundamentos de LLMs y prompt engineering
- ✅ Text-to-SQL para consultas en lenguaje natural
- ✅ Generación automática de código ETL
- ✅ RAG para chatbots sobre documentación
- ✅ Embeddings para búsqueda semántica
- ✅ Agentes autónomos con LangGraph
- ✅ Validación de calidad con LLMs
- ✅ Generación de datos sintéticos
- ✅ Integración LLMs en pipelines de producción
- ✅ Costos y optimización de APIs de IA


---

## 📈 Nivel Negocio LATAM - Estrategia y Sectores (4-6 semanas)

### Notebooks Completados (10/10)

1. **01_estrategia_datos_latam.ipynb** ✅
   - Marco conceptual: Rol de ingeniería de datos en estrategia corporativa
   - Características estructurales (confiabilidad, escalabilidad, gobernanza)
   - Ventajas estratégicas (velocidad decisión, calidad, reducción riesgo)
   - Resultados medibles (ciclos reporte, detección temprana, auditorías)
   - Diagnóstico de madurez con visualización

2. **02_retail_consumo_masivo.ipynb** ✅
   - Caso de uso: Pipeline OSA (On-Shelf Availability)
   - Impacto: 92%→96% OSA, detección 48h→2h, ahorro $1.8M/año
   - Ejercicio: Validación calidad datos (nulls, negativos, cobertura)
   - Visualización Plotly: Top 5 SKUs

3. **03_finanzas_banca.ipynb** ✅
   - Caso de uso: Detección fraude streaming (Kafka + feature store)
   - Impacto: 24h→<200ms latencia, 65%→89% detección, ahorro $3.2M/año
   - Ejercicio: Feature engineering para riesgo (horas nocturnas, montos altos)
   - Visualización: Distribución ECL (Expected Credit Loss)

4. **04_salud_farmaceutico.ipynb** ✅
   - Caso de uso: Interoperabilidad HL7/FHIR en emergencias
   - Impacto: 45→28 min espera, ahorro $800k/año
   - Ejercicio: Pseudonymización con SHA256 para PII
   - Visualización: Box plot tiempos espera

5. **05_energia_recursos_naturales.ipynb** ✅
   - Caso de uso: Mantenimiento predictivo IoT/SCADA
   - Impacto: OEE 0.82→0.91, stops 12→2/año, ahorro $4.5M/año
   - Ejercicio: Detección anomalías con rolling mean + 3-sigma
   - Visualización: Time-series con umbral temperatura

6. **06_telecomunicaciones.ipynb** ✅
   - Caso de uso: Churn reduction con CDR streaming
   - Impacto: Churn 2.5%→1.4%, reacción 24h→15min, LTV salvado $6.8M
   - Ejercicio: Pipeline features churn (uso bajo, quejas altas)
   - Visualización: Probabilidad churn por segmento

7. **07_industria_manufactura.ipynb** ✅
   - Caso de uso: SPC (Statistical Process Control) + visión computacional
   - Impacto: Scrap 8%→2.8%, OEE 0.78→0.88, ahorro $6.2M/año
   - Ejercicio: Cálculo límites control 3-sigma, detección out-of-control
   - Visualización: OEE por turno

8. **08_logistica_transporte.ipynb** ✅
   - Caso de uso: Routing optimization con telemetría GPS
   - Impacto: OTIF 88%→96.5%, costo $45→$38/entrega, ahorro $3.2M/año
   - Ejercicio: Cálculo OTIF y costos logísticos
   - Visualización: Histograma ETA vs real

9. **09_agro_alimentos.ipynb** ✅
   - Caso de uso: Agricultura precisión con satélite Sentinel-2
   - Impacto: Yield 3.2→3.6 ton/ha (+12.5%), pérdidas 15%→7%, revenue +$1.8M
   - Ejercicio: Análisis variabilidad intra-lote con NDVI
   - Visualización: Scatter NDVI vs yield con OLS

10. **10_sector_publico_gobierno.ipynb** ✅
    - Caso de uso: Interoperabilidad entre sistemas gubernamentales
    - Impacto: Trámites 12→4.2 días, satisfacción 38%→74%, fraude +120% detección
    - Ejercicio: Simulación interoperabilidad padron/impuestos
    - Visualización: Box plot tiempos procedimientos

### Componentes Técnicos
- ✅ **Pipelines de producción**:
  - `scripts/pipelines/retail/pipeline_retail.py` (CLI con Click)
  - `scripts/pipelines/manufactura/pipeline_manufactura.py` (CLI con Click)
- ✅ **Tests unitarios**: 18 passing (`test_pipeline_retail.py`, `test_pipeline_manufactura.py`)
- ✅ **Visualizaciones**: 10 gráficos interactivos Plotly
- ✅ **Contratos de datos**: SLOs, ownership, ROI por sector

### Objetivos de Aprendizaje Negocio LATAM
- ✅ Comprender rol estratégico de ingeniería de datos en corporaciones
- ✅ Mapear OKRs de negocio a capacidades técnicas de datos
- ✅ Cuantificar impacto económico de decisiones de ingeniería
- ✅ Diseñar pipelines con métricas de negocio (OSA, OEE, OTIF, churn)
- ✅ Implementar validación y calidad alineada a SLOs
- ✅ Aplicar patrones sectoriales (retail, finanzas, salud, energía, telco, manufactura, logística, agro, gobierno)
- ✅ Construir contratos de datos con propietarios y responsabilidades
- ✅ Traducir requerimientos de negocio a arquitecturas de datos

---

## 📊 Resumen Ejecutivo del Curso

### Estadísticas Generales
- **Total notebooks**: 53 ✅ (100% completados)
- **Líneas de código**: ~20,000+ (estimado)
- **Tecnologías cubiertas**: 50+ herramientas y frameworks
- **Proyectos integradores**: 8 (2 por nivel técnico)
- **Duración total**: 42-52 semanas (10-13 meses a tiempo parcial)

### Cobertura Tecnológica

**Lenguajes y Core:**
- Python (avanzado), SQL (intermedio-avanzado), Bash

**Data Processing:**
- pandas, numpy, polars, dask, PySpark

**Bases de Datos:**
- PostgreSQL, SQLite, MongoDB, Redis, DuckDB

**Orquestación:**
- Apache Airflow, Prefect, Dagster

**Streaming:**
- Apache Kafka, Spark Streaming

**Cloud (Multi-Cloud):**
- **AWS**: S3, Glue, Athena, Lambda, EMR, Redshift
- **GCP**: Cloud Storage, BigQuery, Dataflow, Composer, Cloud Functions
- **Azure**: ADLS Gen2, Synapse, Data Factory, Databricks, Azure Functions

**Data Quality:**
- Great Expectations, Pandera, Pydantic

**GenAI:**
- OpenAI, Google Gemini, Anthropic Claude y modelos locales
- LangChain, LangGraph, ChromaDB
- RAG, embeddings, agentes autónomos

**MLOps:**
- Feast, Tecton (feature stores), MLflow

**Observability:**
- Prometheus, OpenLineage, DataHub

---

## 🎓 Certificaciones Recomendadas Post-Curso

### Cloud Certifications
- **AWS**: AWS Certified Data Analytics - Specialty
- **GCP**: Google Cloud Professional Data Engineer
- **Azure**: Microsoft Certified: Azure Data Engineer Associate (DP-203)

### Vendor-Specific
- **Databricks**: Databricks Certified Data Engineer Associate/Professional
- **Snowflake**: SnowPro Core Certification
- **Apache**: Airflow Fundamentals (Astronomer)

### General
- **DAMA**: CDMP (Certified Data Management Professional)

---

## 🚀 Siguientes Pasos Después del Curso

1. **Construir Portfolio**:
   - Subir proyectos a GitHub con documentación
   - Blog posts explicando soluciones técnicas
   - Contribuir a proyectos open source

2. **Networking**:
   - Participar en meetups de data engineering
   - Conferencias: Data Council, Kafka Summit, Spark Summit
   - LinkedIn: conectar con profesionales del área

3. **Especialización**:
   - Elegir un nicho (streaming, ML, cloud, governance)
   - Certificaciones específicas
   - Profundizar en tecnologías clave

4. **Buscar Empleo**:
   - Actualizar CV con proyectos del curso
   - Preparar para entrevistas técnicas
   - Target empresas con stack similar al aprendido

---

Este roadmap refleja el estado **100% completo** del curso de Ingeniería de Datos. ¡Felicitaciones por embarcarte en este viaje! 🎉
