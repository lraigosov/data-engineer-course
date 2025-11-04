# Changelog

Todos los cambios notables en este proyecto serán documentados en este archivo.

El formato está basado en [Keep a Changelog](https://keepachangelog.com/es-ES/1.0.0/),
y este proyecto adhiere a [Semantic Versioning](https://semver.org/lang/es/).

---

**Autor**: Luis J. Raigoso V. (LJRV) - [@lraigosov](https://github.com/lraigosov)

---

## [1.0.0] - 2024-10-30

### Añadido
- ✅ **Estructura completa del proyecto** con 40 notebooks
- ✅ **Nivel Junior** (10/10 notebooks completos)
  - 01_introduccion_ingenieria_datos.ipynb
  - 02_python_manipulacion_datos.ipynb
  - 03_pandas_fundamentos.ipynb
  - 04_sql_basico.ipynb
  - 05_limpieza_datos.ipynb
  - 06_visualizacion_datos.ipynb
  - 07_git_control_versiones.ipynb
  - 08_apis_web_scraping.ipynb
  - 09_proyecto_integrador_1.ipynb
  - 10_proyecto_integrador_2.ipynb

- ✅ **Nivel Mid** (10/10 notebooks completos)
  - 01_apache_airflow_fundamentos.ipynb
  - 02_streaming_kafka.ipynb
  - 03_cloud_aws.ipynb
  - 04_bases_datos_postgresql_mongodb.ipynb
  - 05_dataops_cicd.ipynb
  - 06_conectores_avanzados_rest_graphql_sftp.ipynb
  - 07_optimizacion_sql_particionado.ipynb
  - 08_fastapi_servicios_datos.ipynb
  - 09_proyecto_integrador_1.ipynb
  - 10_proyecto_integrador_2.ipynb

- ✅ **Nivel Senior** (10/10 notebooks completos)
  - 01_data_governance_calidad.ipynb
  - 02_lakehouse_delta_iceberg.ipynb
  - 03_spark_streaming.ipynb
  - 04_arquitecturas_modernas.ipynb
  - 05_ml_pipelines_feature_stores.ipynb
  - 06_cost_optimization_finops.ipynb
  - 07_seguridad_compliance.ipynb
  - 08_observabilidad_linaje.ipynb
  - 09_proyecto_integrador_1.ipynb
  - 10_proyecto_integrador_2.ipynb

- ✅ **Nivel GenAI** (10/10 notebooks completos)
  - 00_comparacion_openai_gemini.ipynb
  - 01_fundamentos_llms_prompting.ipynb
  - 02_generacion_sql_nl2sql.ipynb
  - 03_generacion_codigo_etl.ipynb
  - 04_rag_documentacion_datos.ipynb
  - 05_embeddings_similitud_datos.ipynb
  - 06_agentes_automatizacion.ipynb
  - 07_calidad_validacion_llm.ipynb
  - 08_sintesis_aumento_datos.ipynb
  - 09_proyecto_integrador_1.ipynb
  - 10_proyecto_integrador_2.ipynb

- ✅ **Documentación completa**:
  - README.md principal con información del curso
  - CONTRIBUTING.md con guías de contribución
  - docs/guia_instalacion.md
  - docs/roadmap.md
  - docs/referencias.md

- ✅ **Scripts de utilidad**:
  - scripts/etl/simple_etl.py
  - scripts/transformaciones/data_transformations.py
  - scripts/pipelines/data_ingestion_pipeline.py
  - scripts/pipelines/batch_processing.py

- ✅ **Tests automatizados**:
  - tests/unit/test_transformations.py (16 pruebas)
  - tests/integration/test_pipelines.py (15+ pruebas)

- ✅ **Datasets de ejemplo**:
  - productos.csv (30 productos)
  - clientes.csv (30 clientes)
  - ventas.csv (50 transacciones)
  - logs_actividad.json (25 eventos)

- ✅ **Configuración del proyecto**:
  - requirements.txt con todas las dependencias
  - .env.example con plantillas de configuración
  - .gitignore configurado
  - LICENSE (MIT)

### Cambiado
- 📝 Actualizada información del autor en todos los documentos
- 📝 Mejorados notebooks 01-05 con celdas explicativas detalladas
- 📝 Reorganizada estructura de documentación

## [1.1.0] - 2025-10-30

### Añadido
- 📚 **Celdas explicativas didácticas** agregadas a notebooks Junior:
  - 01_introduccion_ingenieria_datos.ipynb (7 explicaciones)
  - 02_python_manipulacion_datos.ipynb (12 explicaciones)
  - 03_pandas_fundamentos.ipynb (12 explicaciones)
  - 04_sql_basico.ipynb (13 explicaciones)
  - 05_limpieza_datos.ipynb (1 explicación)

## [1.2.0] - 2025-10-31

### Añadido
- 🔒 **Protección de autoría**: Requisito obligatorio de atribución a LuisRai en LICENSE
- 📚 **Guía educativa**: Nuevo archivo `notebooks/⚠️_IMPORTANTE_LEER_PRIMERO.md` (300+ líneas)
  - Cuándo usar notebooks vs código de producción
  - Workflow de migración: exploración → prototipo → producción
  - Ejemplos prácticos de conversión notebook → script → DAG
- ⚠️ **Advertencias de producción**: Celdas de advertencia en notebooks de entrada:
  - nivel_junior/01_introduccion_ingenieria_datos.ipynb
  - nivel_mid/01_apache_airflow_fundamentos.ipynb
  - nivel_senior/01_data_governance_calidad.ipynb
  - nivel_genai/01_fundamentos_llms_prompting.ipynb
- 📦 **Documentación de tecnologías**: Sección expandida en README.md (~40 librerías Python)
  - Core: pandas, numpy, polars, dask
  - Databases: sqlalchemy, psycopg2, pymongo, duckdb
  - Orchestration: apache-airflow, prefect, dagster
  - Distributed: pyspark, delta-spark, kafka-python
  - GenAI: openai, langchain, langgraph, chromadb

### Cambiado
- 📝 README.md actualizado con advertencias prominentes y stack tecnológico completo
- 📝 LICENSE con cláusula de atribución obligatoria al autor

### Corregido
- 🐛 Formato de markdown en nivel_mid/05_dataops_cicd.ipynb (espaciado en tablas y código)

## [1.3.0] - 2025-10-31

### Añadido
- ☁️ **Cobertura multi-cloud completa**:
  - `notebooks/nivel_mid/03b_cloud_gcp.ipynb` (~1,490 líneas)
    * Cloud Storage con lifecycle policies
    * BigQuery (serverless + optimización)
    * Dataflow con Apache Beam
    * Cloud Composer (Airflow managed)
    * Cloud Functions event-driven
    * **Cloud Run**: Serverless containers para ETL >9 minutos
  - `notebooks/nivel_mid/03c_cloud_azure.ipynb` (~1,505 líneas)
    * ADLS Gen2 con hierarchical namespaces y ACLs
    * Azure Synapse Analytics (dedicated + serverless)
    * Azure Data Factory con pipelines visuales
    * Azure Databricks con Delta Lake y Photon
    * Azure Functions con triggers múltiples
    * **Azure Container Instances**: Batch jobs con managed identity
    * **Azure Web Apps**: PaaS para APIs de datos
  - Tablas comparativas entre AWS/GCP/Azure en ambos notebooks
  - Ejercicios prácticos y certificaciones (GCP Professional Data Engineer, Azure DP-203)

### Cambiado
- 📊 Cobertura cloud ampliada de 33% a 100% del mercado
- 📚 +2,995 líneas de contenido educativo cloud práctico
- ☁️ Agregado serverless compute (Lambda, Cloud Run, Functions) a cada notebook cloud

## [1.4.0] - 2025-10-31

### Corregido
- 🐛 **Fix**: Completadas celdas vacías en `notebooks/nivel_junior/10_proyecto_integrador_2.ipynb`
  - Eliminados 13 celdas vacías después de sección de retry logic
  - Agregada **Sección 6**: Scheduler Simple con Polling
    * Función `scan_and_process()` con polling loop
    * Explicación de polling vs watchdog/Airflow/Kafka
  - Agregada **Sección 7**: Ejecución y Testing
    * Generador de archivos de prueba con datos sintéticos
    * Ejecución del pipeline con scheduler
    * Consultas SQL para verificación de datos
    * Estadísticas por producto (revenue, unidades)
  - Agregada **Sección 8**: Métricas y Auditoría
    * Revisión de checkpoints con estados
    * Métricas de procesamiento
    * Verificación de archivos movidos
  - Agregada **Sección 9**: Conclusión y Siguientes Pasos
    * Resumen de componentes construidos
    * Diagrama de flujo del pipeline
    * Conceptos aplicados (ETL, data quality, resiliencia)
    * Mejoras futuras por nivel (Mid: Airflow, Senior: Kafka/Streaming)
    * Habilidades desarrolladas y recursos adicionales
  - **+395 líneas** de código funcional y documentación

### Cambiado
- 📝 **requirements.txt** completamente reorganizado y actualizado:
  - Versiones actualizadas de todas las dependencias
  - Organizado por categorías (Core, Database, Cloud, Orchestration, GenAI, etc.)
  - Documentación inline de cada biblioteca
  - Notas de instalación específicas por nivel
  - Dependencias cloud actualizadas (AWS, GCP, Azure)
  - Stack completo GenAI documentado
  - Instrucciones especiales para Airflow, Spark, Feast

---

## [1.5.0] - 2025-11-04

### Añadido
- 📈 **Módulo Negocio LATAM** (11 notebooks completos):
  - `01_estrategia_datos_latam.ipynb` - Marco conceptual: rol de ingeniería de datos en estrategia corporativa
  - `02_retail_consumo_masivo.ipynb` - Caso OSA, validación calidad, impacto $1.8M
  - `03_finanzas_banca.ipynb` - Detección fraude streaming, feature engineering, ahorro $3.2M
  - `04_salud_farmaceutico.ipynb` - Interoperabilidad HL7/FHIR, pseudonymización, $800k ahorro
  - `05_energia_recursos_naturales.ipynb` - IoT/SCADA predictivo, OEE 0.82→0.91, $4.5M ahorro
  - `06_telecomunicaciones.ipynb` - Churn reduction, CDR/GIS, feature store, $6.8M LTV salvado
  - `07_industria_manufactura.ipynb` - SPC + visión, scrap 8%→2.8%, $6.2M ahorro
  - `08_logistica_transporte.ipynb` - Routing optimization, OTIF 88%→96.5%, $3.2M ahorro
  - `09_agro_alimentos.ipynb` - Agricultura precisión, NDVI, yield +12.5%, $1.8M revenue
  - `10_sector_publico_gobierno.ipynb` - Interoperabilidad, tramites 12→4.2 días, satisfaction 38%→74%
  
- 🔧 **Pipelines de producción**:
  - `scripts/pipelines/retail/pipeline_retail.py` - KPIs OSA con CLI (Click)
  - `scripts/pipelines/manufactura/pipeline_manufactura.py` - OEE por turno con CLI (Click)
  
- ✅ **Tests unitarios**:
  - `tests/unit/test_pipeline_retail.py` (funciones puras, sin IO)
  - `tests/unit/test_pipeline_manufactura.py` (funciones puras, sin IO)
  - 18 tests passing en suite completa
  
- 📊 **Contenido educativo**:
  - 10 visualizaciones interactivas Plotly
  - 9 casos de uso sectoriales con impacto cuantificado ($1.8M-$6.8M)
  - 9 ejercicios prácticos: validación calidad, feature engineering, pseudonymización, anomalías (3-sigma), SPC, OTIF, NDVI, interoperabilidad
  - Secciones "Puente Estrategia ↔ Ingeniería de Datos" con mapeo OKR→KPI→Capacidades→Decisión→Impacto
  - Contratos de datos con SLOs, ownership y ROI por sector

### Cambiado
- 📝 README.md actualizado con módulo Negocio LATAM como sección final del curso
- 📝 Estructura del proyecto actualizada con `negocios_latam/` y pipelines nuevos

## [Próximas Versiones]

### [1.6.0] - Planificado
- 🐳 Docker compose para entorno completo (Airflow + Kafka + Spark + Postgres)
- 📊 Dashboards de ejemplo con Streamlit/Gradio
- 🔄 CI/CD con GitHub Actions completo (lint, test, deploy)
- 📝 Actualización de documentación técnica en `docs/`

### [2.0.0] - Futuro
- 🌐 Plataforma web interactiva para navegación de notebooks
- 🏆 Sistema de evaluación automática y certificados
- 💬 Ejercicios interactivos con autoevaluación
- 🎥 Videos complementarios para conceptos complejos
- 🗣️ Versiones en inglés de todos los materiales

---

## Tipos de Cambios
- **✅ Añadido** para funcionalidades nuevas
- **📝 Cambiado** para cambios en funcionalidad existente
- **⚠️ Obsoleto** para funcionalidades que pronto se eliminarán
- **❌ Eliminado** para funcionalidades eliminadas
- **🐛 Corregido** para corrección de errores
- **🔒 Seguridad** en caso de vulnerabilidades

---

© 2024-2025 LJRV - Luis J. Raigoso V.