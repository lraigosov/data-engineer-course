# 📘 Curso Modular de Ingeniería de Datos

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebooks-orange)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen)

## 📑 Tabla de Contenidos

- [📘 Curso Modular de Ingeniería de Datos](#-curso-modular-de-ingeniería-de-datos)
  - [📑 Tabla de Contenidos](#-tabla-de-contenidos)
  - [🎯 Descripción](#-descripción)
  - [⚠️ Importante - Sobre el Uso de Notebooks](#️-importante---sobre-el-uso-de-notebooks)
  - [🏗️ Estructura del Curso](#️-estructura-del-curso)
    - [📊 Nivel Junior - Fundamentos](#-nivel-junior---fundamentos)
    - [🔧 Nivel Mid - Pipelines y Automatización](#-nivel-mid---pipelines-y-automatización)
    - [🚀 Nivel Senior - Arquitectura y Gobernanza](#-nivel-senior---arquitectura-y-gobernanza)
    - [🤖 Nivel GenAI - IA Generativa para Ingeniería de Datos](#-nivel-genai---ia-generativa-para-ingeniería-de-datos)
    - [📈 Negocio LATAM - Estrategia y Sectores](#-negocio-latam---estrategia-y-sectores)
  - [📁 Estructura del Proyecto](#-estructura-del-proyecto)
  - [🚀 Inicio Rápido](#-inicio-rápido)
    - [Prerrequisitos](#prerrequisitos)
    - [Instalación](#instalación)
  - [🧭 Guía de Uso](#-guía-de-uso)
    - [Para Estudiantes](#para-estudiantes)
    - [Para Instructores](#para-instructores)
  - [📊 Estado del Proyecto](#-estado-del-proyecto)
    - [📝 Notebooks Creados](#-notebooks-creados)
      - [Nivel Junior (10/10 - ✅ 100% Completo)](#nivel-junior-1010----100-completo)
      - [Nivel Mid (12/12 - ✅ 100% Completo)](#nivel-mid-1212----100-completo)
      - [Nivel Senior (10/10 - ✅ 100% Completo)](#nivel-senior-1010----100-completo)
      - [Nivel GenAI (11/11 - ✅ 100% Completo)](#nivel-genai-1111----100-completo)
      - [Negocio LATAM (10/10 - ✅ 100% Completo)](#negocio-latam-1010----100-completo)
    - [📦 Datasets Disponibles](#-datasets-disponibles)
    - [🔧 Scripts Implementados](#-scripts-implementados)
    - [🧪 Tests Disponibles](#-tests-disponibles)
    - [📚 Documentación](#-documentación)
  - [📊 Progreso por Nivel](#-progreso-por-nivel)
  - [🔧 Tecnologías y Librerías Incluidas](#-tecnologías-y-librerías-incluidas)
    - [🐍 Core Python Libraries](#-core-python-libraries)
    - [🗄️ Bases de Datos y Conectividad](#️-bases-de-datos-y-conectividad)
    - [🔄 Orquestación y Workflows](#-orquestación-y-workflows)
    - [☁️ Cloud y Almacenamiento](#️-cloud-y-almacenamiento)
    - [🚀 Procesamiento Distribuido](#-procesamiento-distribuido)
    - [📊 Calidad y Validación](#-calidad-y-validación)
    - [🌐 APIs y Web](#-apis-y-web)
    - [🤖 IA Generativa y ML](#-ia-generativa-y-ml)
    - [📈 Visualización](#-visualización)
    - [🧪 Testing y Calidad](#-testing-y-calidad)
  - [🤝 Contribuciones](#-contribuciones)
  - [📚 Recursos Adicionales](#-recursos-adicionales)
  - [📄 Licencia](#-licencia)
  - [👥 Autor Original](#-autor-original)
  - [📞 Contacto y Soporte](#-contacto-y-soporte)
  - [🙏 Agradecimientos](#-agradecimientos)
  - [📝 Copyright y Reconocimiento](#-copyright-y-reconocimiento)

---

## 🎯 Descripción

Curso completo y estructurado para formar **Ingenieros de Datos** desde nivel principiante hasta avanzado, organizado en cuatro niveles progresivos: **Junior**, **Mid**, **Senior** y **GenAI**. El curso combina teoría sólida con práctica intensiva mediante **Notebooks interactivos**, casos de uso reales y proyectos aplicados.

**Autor Original:** LuisRai (Luis J. Raigoso V.)  
**Repositorio:** https://github.com/lraigosov/data-engineer-course

## ⚠️ Importante - Sobre el Uso de Notebooks

> **⚠️ IMPORTANTE - SOBRE EL USO DE NOTEBOOKS:**
> 
> Este curso utiliza **Jupyter Notebooks con fines exclusivamente educativos** para facilitar el aprendizaje interactivo y la comprensión de cada concepto.
> 
> **🚨 EN PRODUCCIÓN, EL USO DE NOTEBOOKS NO ES UNA PRÁCTICA RECOMENDABLE** 
> 
> En entornos de producción se deben utilizar:
> - ✅ Scripts Python modulares (`.py`)
> - ✅ Paquetes estructurados con proper testing
> - ✅ CI/CD pipelines
> - ✅ Orquestadores (Airflow, Prefect, Dagster)
> - ✅ Contenedores (Docker) y despliegues automatizados
> 
> Los notebooks son excelentes para **exploración, prototipado y enseñanza**, pero NO para sistemas en producción que requieren escalabilidad, mantenibilidad y robustez.

## 🏗️ Estructura del Curso

### 📊 Nivel Junior - Fundamentos
- [Introducción a la Ingeniería de Datos](notebooks/nivel_junior/01_introduccion_ingenieria_datos.ipynb)
- [Programación en Python para datos](notebooks/nivel_junior/02_python_manipulacion_datos.ipynb)
- [Manipulación de datos (Pandas, NumPy)](notebooks/nivel_junior/03_pandas_fundamentos.ipynb)
- [SQL básico e intermedio](notebooks/nivel_junior/04_sql_basico.ipynb)
- [Limpieza y preparación de datos](notebooks/nivel_junior/05_limpieza_datos.ipynb)
- [Visualización de datos](notebooks/nivel_junior/06_visualizacion_datos.ipynb)
- [Control de versiones con Git](notebooks/nivel_junior/07_git_control_versiones.ipynb)
- [APIs y Web Scraping](notebooks/nivel_junior/08_apis_web_scraping.ipynb)
- [Proyecto Integrador 1](notebooks/nivel_junior/09_proyecto_integrador_1.ipynb)
- [Proyecto Integrador 2](notebooks/nivel_junior/10_proyecto_integrador_2.ipynb)

### 🔧 Nivel Mid - Pipelines y Automatización
- [Apache Airflow: Fundamentos](notebooks/nivel_mid/01_apache_airflow_fundamentos.ipynb)
- [Streaming con Kafka](notebooks/nivel_mid/02_streaming_kafka.ipynb)
- [Cloud AWS: S3, Glue, Athena, Lambda](notebooks/nivel_mid/03_cloud_aws.ipynb)
- [Cloud GCP: BigQuery, Dataflow, Cloud Run](notebooks/nivel_mid/03b_cloud_gcp.ipynb)
- [Cloud Azure: ADLS, Synapse, ADF, Databricks](notebooks/nivel_mid/03c_cloud_azure.ipynb)
- [Bases de datos: PostgreSQL y MongoDB](notebooks/nivel_mid/04_bases_datos_postgresql_mongodb.ipynb)
- [DataOps y CI/CD](notebooks/nivel_mid/05_dataops_cicd.ipynb)
- [Conectores avanzados: REST, GraphQL, SFTP](notebooks/nivel_mid/06_conectores_avanzados_rest_graphql_sftp.ipynb)
- [Optimización SQL y particionado](notebooks/nivel_mid/07_optimizacion_sql_particionado.ipynb)
- [FastAPI y servicios de datos](notebooks/nivel_mid/08_fastapi_servicios_datos.ipynb)
- [Proyecto Integrador 1](notebooks/nivel_mid/09_proyecto_integrador_1.ipynb)
- [Proyecto Integrador 2](notebooks/nivel_mid/10_proyecto_integrador_2.ipynb)

### 🚀 Nivel Senior - Arquitectura y Gobernanza
- [Gobernanza y calidad de datos](notebooks/nivel_senior/01_data_governance_calidad.ipynb)
- [Data Lakehouse: Delta y Iceberg](notebooks/nivel_senior/02_lakehouse_delta_iceberg.ipynb)
- [Spark Streaming avanzado](notebooks/nivel_senior/03_spark_streaming.ipynb)
- [Arquitecturas modernas: Lambda, Kappa, Data Mesh](notebooks/nivel_senior/04_arquitecturas_modernas.ipynb)
- [ML Pipelines y Feature Stores](notebooks/nivel_senior/05_ml_pipelines_feature_stores.ipynb)
- [FinOps y optimización de costos cloud](notebooks/nivel_senior/06_cost_optimization_finops.ipynb)
- [Seguridad y Compliance](notebooks/nivel_senior/07_seguridad_compliance.ipynb)
- [Observabilidad y linaje de datos](notebooks/nivel_senior/08_observabilidad_linaje.ipynb)
- [Proyecto Integrador 1](notebooks/nivel_senior/09_proyecto_integrador_1.ipynb)
- [Proyecto Integrador 2](notebooks/nivel_senior/10_proyecto_integrador_2.ipynb)

### 🤖 Nivel GenAI - IA Generativa para Ingeniería de Datos
- [Comparación OpenAI vs Google Gemini](notebooks/nivel_genai/00_comparacion_openai_gemini.ipynb)
- [Fundamentos de LLMs y prompting](notebooks/nivel_genai/01_fundamentos_llms_prompting.ipynb)
- [Generación SQL: NL2SQL](notebooks/nivel_genai/02_generacion_sql_nl2sql.ipynb)
- [Generación automática de código ETL](notebooks/nivel_genai/03_generacion_codigo_etl.ipynb)
- [RAG: Documentación de datos](notebooks/nivel_genai/04_rag_documentacion_datos.ipynb)
- [Embeddings y similitud de datos](notebooks/nivel_genai/05_embeddings_similitud_datos.ipynb)
- [Agentes y automatización](notebooks/nivel_genai/06_agentes_automatizacion.ipynb)
- [Validación y calidad con LLMs](notebooks/nivel_genai/07_calidad_validacion_llm.ipynb)
- [Síntesis y aumento de datos](notebooks/nivel_genai/08_sintesis_aumento_datos.ipynb)
- [Proyecto Integrador 1: Chatbot con RAG](notebooks/nivel_genai/09_proyecto_integrador_1.ipynb)
- [Proyecto Integrador 2: Plataforma self-service con GenAI](notebooks/nivel_genai/10_proyecto_integrador_2.ipynb)

### 📈 Negocio LATAM - Estrategia y Sectores
**Módulo final del curso:** Aplicación práctica de la Ingeniería de Datos como habilitador estratégico del negocio en contexto latinoamericano.

- [Estrategia de datos LATAM: Marco conceptual](notebooks/negocios_latam/01_estrategia_datos_latam.ipynb)
- [Retail y consumo masivo](notebooks/negocios_latam/02_retail_consumo_masivo.ipynb)
- [Finanzas y banca](notebooks/negocios_latam/03_finanzas_banca.ipynb)
- [Salud y farmacéutico](notebooks/negocios_latam/04_salud_farmaceutico.ipynb)
- [Energía y recursos naturales](notebooks/negocios_latam/05_energia_recursos_naturales.ipynb)
- [Telecomunicaciones](notebooks/negocios_latam/06_telecomunicaciones.ipynb)
- [Industria y manufactura](notebooks/negocios_latam/07_industria_manufactura.ipynb)
- [Logística y transporte](notebooks/negocios_latam/08_logistica_transporte.ipynb)
- [Agro y alimentos](notebooks/negocios_latam/09_agro_alimentos.ipynb)
- [Sector público y gobierno](notebooks/negocios_latam/10_sector_publico_gobierno.ipynb)

## 📁 Estructura del Proyecto

```
curso_ingenieria_datos/
│
├── config/                    # Configuraciones globales
│   ├── settings.yaml         # Parámetros del proyecto
│   └── credentials.example   # Plantilla de credenciales
│
├── notebooks/                # Notebooks organizados por nivel
│   ├── nivel_junior/         # 10 notebooks fundamentales
│   ├── nivel_mid/           # 10 notebooks intermedios
│   ├── nivel_senior/        # 10 notebooks avanzados
│   ├── nivel_genai/         # 10 notebooks de IA Generativa
│   └── negocios_latam/      # 11 notebooks: estrategia + 10 sectores
│
├── datasets/                 # Datos para ejercicios
│   ├── raw/                 # Datos sin procesar
│   ├── processed/           # Datos procesados
│   └── external/            # Datasets externos
│
├── scripts/                  # Scripts auxiliares
│   ├── etl/                 # Scripts ETL
│   ├── transformaciones/    # Transformaciones de datos
│   └── pipelines/           # Pipelines completos (retail, manufactura)
│
├── tests/                    # Pruebas automatizadas
│   ├── unit/                # Pruebas unitarias
│   └── integration/         # Pruebas de integración
│
└── docs/                     # Documentación
    ├── guia_instalacion.md  # Guía de setup
    ├── roadmap.md           # Roadmap del curso
    └── referencias.md       # Referencias y recursos
```

## 🚀 Inicio Rápido

### Prerrequisitos

- Python 3.8 o superior
- Git instalado
- 4GB RAM mínimo
- 2GB espacio libre en disco

### Instalación

1. **Clona el repositorio:**
```bash
git clone <url-del-repositorio>
cd curso_ingenieria_datos
```

2. **Crea un entorno virtual:**
```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

3. **Instala las dependencias:**
```bash
pip install -r requirements.txt
```

4. **Configura las credenciales:**
```bash
cp config/credentials.example config/credentials.yaml
# Edita credentials.yaml con tus datos
```

5. **Inicia Jupyter:**
```bash
jupyter notebook
```

## 🧭 Guía de Uso

### Para Estudiantes

1. **Comienza por el Nivel Junior** si eres principiante
2. **Ejecuta los notebooks en orden** numerado
3. **Completa todos los ejercicios** antes de avanzar
4. **Usa los datasets proporcionados** para las prácticas
5. **Consulta la documentación** en caso de dudas

### Para Instructores

1. **Revisa el roadmap** para planificar el curso
2. **Adapta los ejercicios** según tu audiencia
3. **Usa los tests** para validar el progreso
4. **Consulta las referencias** para ampliar contenido

## 📊 Estado del Proyecto

### 📝 Notebooks Creados

#### Nivel Junior (10/10 - ✅ 100% Completo)
- ✅ `01_introduccion_ingenieria_datos.ipynb` - Introducción y primer ETL
- ✅ `02_python_manipulacion_datos.ipynb` - Fundamentos de Python
- ✅ `03_pandas_fundamentos.ipynb` - Manipulación con Pandas
- ✅ `04_sql_basico.ipynb` - SQL con SQLite
- ✅ `05_limpieza_datos.ipynb` - Calidad y limpieza de datos
- ✅ `06_visualizacion_datos.ipynb` - Matplotlib, Seaborn, Plotly
- ✅ `07_git_control_versiones.ipynb` - Git y GitHub workflows
- ✅ `08_apis_web_scraping.ipynb` - REST APIs y web scraping
- ✅ `09_proyecto_integrador_1.ipynb` - ETL completo con validaciones
- ✅ `10_proyecto_integrador_2.ipynb` - Pipeline near real-time con scheduler

#### Nivel Mid (12/12 - ✅ 100% Completo)
- ✅ `01_apache_airflow_fundamentos.ipynb` - Orquestación con Airflow
- ✅ `02_streaming_kafka.ipynb` - Streaming con Kafka
- ✅ `03_cloud_aws.ipynb` - AWS: S3, Glue, Athena, Lambda
- ✅ `03b_cloud_gcp.ipynb` - GCP: Cloud Storage, BigQuery, Dataflow, Cloud Run
- ✅ `03c_cloud_azure.ipynb` - Azure: ADLS Gen2, Synapse, ADF, Databricks, ACI
- ✅ `04_bases_datos_postgresql_mongodb.ipynb` - SQL y NoSQL
- ✅ `05_dataops_cicd.ipynb` - DataOps, tests y CI/CD
- ✅ `06_conectores_avanzados_rest_graphql_sftp.ipynb` - Conectores robustos
- ✅ `07_optimizacion_sql_particionado.ipynb` - Optimización y particionado
- ✅ `08_fastapi_servicios_datos.ipynb` - APIs de datos con FastAPI
- ✅ `09_proyecto_integrador_1.ipynb` - API → DB → Parquet con Airflow
- ✅ `10_proyecto_integrador_2.ipynb` - Kafka streaming → lake con idempotencia

#### Nivel Senior (10/10 - ✅ 100% Completo)
- ✅ `01_data_governance_calidad.ipynb` - DAMA-DMBOK y linaje
- ✅ `02_lakehouse_delta_iceberg.ipynb` - Data Lakehouse con Delta/Iceberg
- ✅ `03_spark_streaming.ipynb` - Spark Structured Streaming avanzado
- ✅ `04_arquitecturas_modernas.ipynb` - Lambda, Kappa, Delta, Data Mesh
- ✅ `05_ml_pipelines_feature_stores.ipynb` - MLOps y feature stores
- ✅ `06_cost_optimization_finops.ipynb` - FinOps y optimización cloud
- ✅ `07_seguridad_compliance.ipynb` - Seguridad, GDPR, auditoría
- ✅ `08_observabilidad_linaje.ipynb` - Observabilidad y OpenLineage
- ✅ `09_proyecto_integrador_1.ipynb` - Plataforma de datos completa
- ✅ `10_proyecto_integrador_2.ipynb` - Data Mesh con feature store

#### Nivel GenAI (11/11 - ✅ 100% Completo)
- ✅ `00_comparacion_openai_gemini.ipynb` - Comparación OpenAI vs Google Gemini
- ✅ `01_fundamentos_llms_prompting.ipynb` - Fundamentos de LLMs y prompting
- ✅ `02_generacion_sql_nl2sql.ipynb` - Text-to-SQL con seguridad
- ✅ `03_generacion_codigo_etl.ipynb` - Generación de pipelines ETL
- ✅ `04_rag_documentacion_datos.ipynb` - RAG para documentación técnica
- ✅ `05_embeddings_similitud_datos.ipynb` - Embeddings y búsqueda semántica
- ✅ `06_agentes_automatizacion.ipynb` - Agentes con LangGraph/AutoGen
- ✅ `07_calidad_validacion_llm.ipynb` - Validación de datos con LLMs
- ✅ `08_sintesis_aumento_datos.ipynb` - Generación de datos sintéticos
- ✅ `09_proyecto_integrador_1.ipynb` - Chatbot de consulta con RAG
- ✅ `10_proyecto_integrador_2.ipynb` - Plataforma self-service con GenAI

#### Negocio LATAM (10/10 - ✅ 100% Completo)
- ✅ `01_estrategia_datos_latam.ipynb` - Marco conceptual estratégico
- ✅ `02_retail_consumo_masivo.ipynb` - OSA, calidad datos, $1.8M ahorro
- ✅ `03_finanzas_banca.ipynb` - Fraude streaming, $3.2M ahorro
- ✅ `04_salud_farmaceutico.ipynb` - Interoperabilidad HL7/FHIR, $800k ahorro
- ✅ `05_energia_recursos_naturales.ipynb` - IoT predictivo, OEE, $4.5M ahorro
- ✅ `06_telecomunicaciones.ipynb` - Churn reduction, $6.8M LTV salvado
- ✅ `07_industria_manufactura.ipynb` - SPC + visión, $6.2M ahorro
- ✅ `08_logistica_transporte.ipynb` - Routing optimization, $3.2M ahorro
- ✅ `09_agro_alimentos.ipynb` - Agricultura precisión, yield +12.5%
- ✅ `10_sector_publico_gobierno.ipynb` - Interoperabilidad gobierno, -65% tiempo

### 📦 Datasets Disponibles
- ✅ `productos.csv` - 30 productos con categorías y precios
- ✅ `clientes.csv` - 30 registros de clientes
- ✅ `ventas.csv` - 50 transacciones de ventas
- ✅ `logs_actividad.json` - 25 eventos de usuario

### 🔧 Scripts Implementados
- ✅ `scripts/etl/simple_etl.py` - Pipeline ETL básico
- ✅ `scripts/transformaciones/data_transformations.py` - Utilidades de transformación
- ✅ `scripts/pipelines/data_ingestion_pipeline.py` - Pipeline de ingesta multi-fuente
- ✅ `scripts/pipelines/batch_processing.py` - Procesamiento en lotes con paralelización
- ✅ `scripts/pipelines/retail/pipeline_retail.py` - Pipeline KPIs retail (OSA) con CLI
- ✅ `scripts/pipelines/manufactura/pipeline_manufactura.py` - Pipeline OEE manufactura con CLI

### 🧪 Tests Disponibles
- ✅ `tests/unit/test_transformations.py` - 16 pruebas unitarias
- ✅ `tests/unit/test_pipeline_retail.py` - Tests pipeline retail
- ✅ `tests/unit/test_pipeline_manufactura.py` - Tests pipeline manufactura
- ✅ `tests/integration/test_pipelines.py` - 15+ pruebas de integración
- ✅ **Suite completa: 18 tests passing**

### 📚 Documentación
- ✅ Guía de instalación completa
- ✅ Roadmap del curso
- ✅ Referencias y recursos
- ✅ Guía de contribución
- ✅ Changelog

**Progreso General: ✅ 100% completo** (53/53 notebooks + infraestructura completa)

## 📊 Progreso por Nivel

| Nivel         | Duración  | Notebooks | Completados | Proyectos | Estado      |
|---------------|-----------|-----------|-------------|-----------|-------------|
| Junior        | 6-8 sem   | 10        | 10 ✅       | 2 ✅      | ✅ Completo |
| Mid           | 8-10 sem  | 12        | 12 ✅       | 2 ✅      | ✅ Completo |
| Senior        | 10-12 sem | 10        | 10 ✅       | 2 ✅      | ✅ Completo |
| GenAI         | 4-6 sem   | 11        | 11 ✅       | 2 ✅      | ✅ Completo |
| Negocio LATAM | 4-6 sem   | 10        | 10 ✅       | 0         | ✅ Completo |

## 🔧 Tecnologías y Librerías Incluidas

### 🐍 Core Python Libraries
- **pandas** - Manipulación y análisis de datos tabulares
- **numpy** - Computación numérica y álgebra lineal
- **polars** - DataFrame library de alto rendimiento (alternativa a Pandas)
- **dask** - Procesamiento paralelo y distribuido de datos

### 🗄️ Bases de Datos y Conectividad
- **sqlalchemy** - ORM y toolkit SQL para Python
- **psycopg2** - Driver PostgreSQL
- **pymongo** - Driver MongoDB
- **duckdb** - Base de datos analítica in-process
- **pyarrow** - Interface Python para Apache Arrow (datos columnares)

### 🔄 Orquestación y Workflows
- **apache-airflow** - Plataforma de orquestación de workflows
- **prefect** - Framework moderno de orquestación
- **dagster** - Data orchestrator para ML, analytics, y ETL

### ☁️ Cloud y Almacenamiento
- **boto3** - SDK de AWS para Python
- **google-cloud-storage** - SDK de Google Cloud Storage
- **azure-storage-blob** - SDK de Azure Blob Storage
- **s3fs** - Interface filesystem para S3

### 🚀 Procesamiento Distribuido
- **pyspark** - Interface Python para Apache Spark
- **delta-spark** - Delta Lake para Spark
- **kafka-python** - Cliente Kafka para Python

### 📊 Calidad y Validación
- **great-expectations** - Framework de validación de datos
- **pandera** - Validación de DataFrames
- **pydantic** - Validación de datos con type hints

### 🌐 APIs y Web
- **requests** - HTTP library
- **fastapi** - Framework web moderno y rápido
- **uvicorn** - ASGI server
- **beautifulsoup4** - Web scraping
- **httpx** - Cliente HTTP async

### 🤖 IA Generativa y ML
- **openai** - API de OpenAI (GPT-4, embeddings)
- **langchain** - Framework para aplicaciones LLM
- **langgraph** - Construcción de agentes con grafos
- **chromadb** - Vector database
- **sentence-transformers** - Modelos de embeddings

### 📈 Visualización
- **matplotlib** - Biblioteca de visualización base
- **seaborn** - Visualizaciones estadísticas
- **plotly** - Gráficos interactivos
- **streamlit** - Framework para dashboards

### 🧪 Testing y Calidad
- **pytest** - Framework de testing
- **pytest-cov** - Coverage para pytest
- **black** - Code formatter
- **flake8** - Linter
- **mypy** - Type checker

Para instalar todas las dependencias:
```bash
pip install -r requirements.txt
```

## 🤝 Contribuciones

¡Las contribuciones son bienvenidas! Por favor:

1. Haz fork del proyecto
2. Crea una rama para tu feature (`git checkout -b feature/nueva-funcionalidad`)
3. Haz commit de tus cambios (`git commit -m 'Agrega nueva funcionalidad'`)
4. Push a la rama (`git push origin feature/nueva-funcionalidad`)
5. Abre un Pull Request

Consulta `CONTRIBUTING.md` para más detalles.

## 📚 Recursos Adicionales

- [Guía de Instalación Detallada](docs/guia_instalacion.md)
- [Roadmap del Curso](docs/roadmap.md)
- [Referencias y Bibliografía](docs/referencias.md)
- [FAQ - Preguntas Frecuentes](docs/faq.md)

## 📄 Licencia

Este proyecto está bajo la Licencia MIT con requisito de atribución.

**⚠️ RECONOCIMIENTO OBLIGATORIO DE CRÉDITOS:**

Cualquier replicación, modificación, distribución o trabajo derivado de este material **DEBE** incluir atribución prominente al autor original:

**"LuisRai" (Luis J. Raigoso V.)**

La atribución debe aparecer en:
- Documentación del proyecto
- Headers de archivos de código
- Interfaces de usuario
- Materiales de presentación
- Cualquier publicación derivada

Ver archivo `LICENSE` para detalles completos.

## 👥 Autor Original

**LuisRai - Luis J. Raigoso V. (LJRV)**  
*Creador y desarrollador del curso completo*

- GitHub: [@lraigosov](https://github.com/lraigosov)
- LinkedIn: [lraigosov](https://www.linkedin.com/in/lraigosov/)
- Repositorio: https://github.com/lraigosov/data-engineer-course

**Todos los notebooks, scripts y materiales fueron creados por LuisRai (2024-2025)**

## 📞 Contacto y Soporte

- **GitHub Issues**: Para bugs y feature requests
- **GitHub Discussions**: Para preguntas generales y discusiones
- **Email**: A través de [GitHub Issues](https://github.com/lraigosov/data-engineer-course/issues)
- **Comunidad**: A través de [GitHub Issues](https://github.com/lraigosov/data-engineer-course/issues)

## 🙏 Agradecimientos

- Comunidad de Python y Jupyter
- Contribuidores de bibliotecas open source
- Estudiantes y beta testers del curso
- Comunidad de Ingeniería de Datos

## 📝 Copyright y Reconocimiento

© 2024-2025 **LuisRai** - Luis J. Raigoso V. (lraigosov)

**Este material educativo fue creado íntegramente por LuisRai.**

Cualquier uso, modificación o redistribución debe mantener visible el reconocimiento al autor original.

---

⭐ **¡Dale una estrella si este proyecto te ayuda!** ⭐

**Si utilizas este material, por favor reconoce a LuisRai como autor original.**
