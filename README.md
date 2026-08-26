# 📘 Curso Modular de Ingeniería de Datos

![Python](https://img.shields.io/badge/Python-3.11%2B-blue)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebooks-orange)
![License](https://img.shields.io/badge/Code-MIT-green)
![Content License](https://img.shields.io/badge/Content-CC%20BY%204.0-lightgrey)
![CI](https://github.com/lraigosov/data-engineer-course/actions/workflows/ci.yml/badge.svg)
![Status](https://img.shields.io/badge/Content-53%2F53%20written-brightgreen)

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
  - [🧱 Arquitectura y calidad](#-arquitectura-y-calidad)
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
  - [🔧 Tecnologías y librerías declaradas](#-tecnologías-y-librerías-declaradas)
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
**Repositorio:** [github.com/lraigosov/data-engineer-course](https://github.com/lraigosov/data-engineer-course)

## ⚠️ Importante - Sobre el Uso de Notebooks

> Los notebooks son adecuados para enseñanza, exploración y prototipos. Antes
> de operar una solución, extrae la lógica reutilizable a módulos probados y
> añade configuración, secretos, CI, observabilidad y recuperación. Consulta la
> [guía de uso responsable](notebooks/⚠️_IMPORTANTE_LEER_PRIMERO.md).

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

> **Nota de alcance:** este nivel trata el diseño y gobernanza de arquitecturas
> de datos (lakehouse, Lambda/Kappa/Data Mesh, FinOps, seguridad) como
> competencia de un Data Engineer senior — es decir, "cómo implementar y operar
> bajo estas arquitecturas". Un curso especializado de **Arquitectura de Datos**
> profundizaría en cambio en "cómo decidir y justificar" esos trade-offs a nivel
> organizacional. Ambos enfoques son complementarios, no redundantes.

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

```text
data-engineer-course/
│
├── config/                    # Configuraciones globales
│   ├── settings.yaml         # Parámetros del proyecto
│   └── credentials.example   # Plantilla de credenciales
│
├── notebooks/                # Notebooks organizados por nivel
│   ├── nivel_junior/         # 10 notebooks fundamentales
│   ├── nivel_mid/           # 12 notebooks intermedios
│   ├── nivel_senior/        # 10 notebooks avanzados
│   ├── nivel_genai/         # 11 notebooks de IA Generativa
│   └── negocios_latam/      # 10 notebooks sectoriales
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
├── locks/                    # Dependencias exactas por entorno/Python
├── requirements/             # Entradas para generar locks
├── .github/                  # CI, Dependabot y dependency review
└── docs/                     # Índice, arquitectura y guías
```

## 🧱 Arquitectura y calidad

La [guía de arquitectura](docs/arquitectura.md) documenta las relaciones entre
contenido, scripts, dependencias, Docker y los cuatro jobs actuales de CI. El
[índice documental](docs/README.md) identifica la audiencia y fuente de verdad
de cada guía.

Estado local verificado el 26 de agosto de 2026:

| Control | Resultado |
| --- | ---: |
| Notebooks escritos | 53 |
| Celdas de código con sintaxis válida | 479 |
| Celdas totales con ID nbformat | 1.505 |
| Pruebas automatizadas | 17 |
| Notebooks ejecutados por la allowlist de CI | 1 |

## 🚀 Inicio Rápido

### Prerrequisitos

- Python 3.11, 3.12 o 3.13
- Git instalado
- Recursos suficientes para las dependencias y datos del laboratorio elegido

### Instalación

1. **Clona el repositorio:**

```bash
git clone https://github.com/lraigosov/data-engineer-course.git
cd data-engineer-course
```

1. **Crea un entorno virtual:**

```bash
python -m venv .venv
source .venv/bin/activate  # En PowerShell: .\.venv\Scripts\Activate.ps1
```

1. **Instala el entorno Jupyter reproducible (Python 3.11):**

```bash
python -m pip install --upgrade pip
python -m pip install -r locks/docker-py3.11.txt
```

Los locks `locks/py3.11.txt`, `locks/py3.12.txt` y `locks/py3.13.txt`
corresponden al entorno mínimo de desarrollo/CI. Las dependencias opcionales
por tecnología se declaran como grupos en `pyproject.toml`.

1. **Configura las credenciales:**

```bash
cp config/credentials.example config/credentials.yaml
# Edita credentials.yaml con tus datos
```

1. **Inicia JupyterLab:**

```bash
jupyter lab
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
- ✅ `06_agentes_automatizacion.ipynb` - Agentes con LangGraph
- ✅ `07_calidad_validacion_llm.ipynb` - Validación de datos con LLMs
- ✅ `08_sintesis_aumento_datos.ipynb` - Generación de datos sintéticos
- ✅ `09_proyecto_integrador_1.ipynb` - Chatbot de consulta con RAG
- ✅ `10_proyecto_integrador_2.ipynb` - Plataforma self-service con GenAI

#### Negocio LATAM (10/10 - ✅ 100% Completo)

> ⚠️ **Nota de rigor:** las cifras de ahorro, % de mejora y ROI listadas abajo
> son escenarios didácticos, no datos de clientes reales ni benchmarks
> auditados. En una propuesta real, reemplázalas por métricas internas,
> supuestos documentados y fuentes verificables (ver también `docs/faq.md`
> y la nota equivalente en cada notebook de `negocios_latam/`).

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

- ✅ `tests/unit/test_transformations.py` - 9 pruebas unitarias de transformaciones reales
- ✅ Pipelines retail y manufactura - 2 pruebas unitarias
- ✅ `tests/integration/test_pipelines.py` - 3 flujos de integración ETL/ingesta
- ✅ Herramientas de validación/metadata de notebooks - 3 pruebas unitarias
- ✅ **Suite completa: 17 pruebas automatizadas**

### 📚 Documentación

- [Índice documental](docs/README.md)
- [Guía de instalación](docs/guia_instalacion.md)
- [Arquitectura y diagramas](docs/arquitectura.md)
- [Roadmap](docs/roadmap.md)
- [Rúbricas](docs/rubricas.md)
- [Referencias técnicas](docs/referencias.md)
- [Guía de contribución](CONTRIBUTING.md)
- [Changelog](CHANGELOG.md)

**Progreso General: ✅ 53/53 notebooks escritos** (100% del contenido planificado).

> ⚠️ "Completo" se refiere al contenido escrito, no a ejecución verificada en CI.
> Los notebooks de `nivel_genai/` en particular requieren credenciales de API
> externas y aún no corren en el pipeline automatizado — ver [CI](.github/workflows/ci.yml)
> y la sección de ejecución de notebooks más abajo.

## 📊 Progreso por Nivel

| Nivel         | Duración  | Notebooks | Completados | Proyectos | Estado      |
|---------------|-----------|-----------|-------------|-----------|-------------|
| Junior        | 6-8 sem   | 10        | 10 ✅       | 2 ✅      | ✅ Completo |
| Mid           | 8-10 sem  | 12        | 12 ✅       | 2 ✅      | ✅ Completo |
| Senior        | 10-12 sem | 10        | 10 ✅       | 2 ✅      | ✅ Completo |
| GenAI         | 4-6 sem   | 11        | 11 ✅       | 2 ✅      | ✅ Completo |
| Negocio LATAM | 4-6 sem   | 10        | 10 ✅       | 0         | ✅ Completo |

## 🔧 Tecnologías y librerías declaradas

La fuente de verdad es `pyproject.toml`. Las tecnologías que solo aparecen en
explicaciones o comparaciones no se consideran instaladas por defecto.

| Grupo | Dependencias representativas | Alcance |
| --- | --- | --- |
| Core | pandas, NumPy, SQLAlchemy, Requests, PyYAML, Click | Scripts y pipelines locales |
| Notebooks | JupyterLab, Matplotlib, Plotly, Pandera, Great Expectations, scikit-learn | Laboratorios interactivos |
| Cloud | boto3, Google Cloud Storage/BigQuery, Azure Identity/Storage | Prácticas opcionales por proveedor |
| Databases | DuckDB, PostgreSQL, MongoDB, Redis | Conectividad opcional |
| Airflow | Apache Airflow 3.3.x | Orquestación opcional |
| Spark | PySpark 4.x, Delta Lake 4.x | Procesamiento distribuido opcional |
| GenAI | OpenAI, Google GenAI, LangChain, LangGraph, ChromaDB, FAISS | Laboratorios con APIs/modelos opcionales |
| Desarrollo | pytest, Ruff, Black, mypy, nbclient, nbformat | Calidad y contribución |

Para instalar juntos los grupos opcionales compatibles (puede requerir
dependencias de sistema adicionales):

```bash
python -m pip install --group all
```

Airflow queda fuera de `all` y debe instalarse en un entorno dedicado con
`python -m pip install --group airflow`.

Para desarrollo reproducible usa el lock de tu versión de Python; para el curso
completo con Jupyter usa Python 3.11 y `locks/docker-py3.11.txt`.

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

Este proyecto usa dos licencias, según el tipo de contenido:

- **Código** (`scripts/`, `ingest/`, `tests/`, `config/`, CI): **MIT License** estándar — ver [`LICENSE`](LICENSE).
- **Contenido educativo** (notebooks, `docs/`, `articles/`, `datasets/`): **[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)** — ver [`LICENSE-CONTENT.md`](LICENSE-CONTENT.md). CC BY 4.0 exige atribución al reusar o adaptar el material, indicando al autor original **"LuisRai" (Luis J. Raigoso V.)** y un enlace al repositorio.

Esta separación reemplaza la cláusula de atribución no estándar que antes formaba parte del archivo `LICENSE` (que lo hacía incompatible con MIT tal como se anunciaba en el badge). El código ahora es MIT sin condiciones adicionales; la obligación de atribución se mantiene, pero bajo una licencia de contenido reconocida (CC BY 4.0) en vez de un texto "MIT" modificado.

## 👥 Autor Original

**LuisRai - Luis J. Raigoso V. (LJRV)**  
*Creador y desarrollador del curso completo*

- GitHub: [@lraigosov](https://github.com/lraigosov)
- LinkedIn: [lraigosov](https://www.linkedin.com/in/lraigosov/)
- Repositorio: [github.com/lraigosov/data-engineer-course](https://github.com/lraigosov/data-engineer-course)

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
