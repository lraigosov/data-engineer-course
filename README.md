# 📘 Curso Modular de Ingeniería de Datos

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebooks-orange)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-En%20Desarrollo-yellow)

## 🎯 Descripción

Curso completo y estructurado para formar **Ingenieros de Datos** desde nivel principiante hasta avanzado, organizado en tres niveles progresivos: **Junior**, **Mid** y **Senior**. El curso combina teoría sólida con práctica intensiva mediante **Notebooks interactivos**, casos de uso reales y proyectos aplicados.

## 🏗️ Estructura del Curso

### 📊 Nivel Junior - Fundamentos
- Introducción a la Ingeniería de Datos
- Programación en Python para datos
- Manipulación de datos (Pandas, NumPy)
- SQL básico y intermedio
- Formatos de datos (CSV, JSON, Parquet)
- ETL básico con Python
- Control de versiones con Git

### 🔧 Nivel Mid - Pipelines y Automatización
- Arquitecturas de datos (Batch/Streaming)
- Orquestación con Airflow/Prefect
- Bases de datos relacionales y NoSQL
- APIs y conectores de datos
- DataOps y CI/CD para datos
- Introducción a Cloud Computing
- Optimización de consultas

### 🚀 Nivel Senior - Arquitectura y Gobernanza
- Arquitecturas modernas (Data Lakehouse, Data Mesh)
- Gobernanza y calidad de datos
- Optimización de costos (FinOps)
- ML Pipelines y Feature Stores
- Seguridad y cumplimiento
- Observabilidad y monitoreo
- Liderazgo técnico

### 🤖 Nivel GenAI - IA Generativa para Ingeniería de Datos
- LLMs y prompting para ingeniería de datos
- NL2SQL y consultas en lenguaje natural
- Generación automática de código ETL
- RAG para documentación técnica
- Embeddings y búsqueda semántica
- Agentes autónomos para automatización
- Validación y calidad de datos con LLMs
- Generación de datos sintéticos

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
│   └── nivel_genai/         # 10 notebooks de IA Generativa
│
├── datasets/                 # Datos para ejercicios
│   ├── raw/                 # Datos sin procesar
│   ├── processed/           # Datos procesados
│   └── external/            # Datasets externos
│
├── scripts/                  # Scripts auxiliares
│   ├── etl/                 # Scripts ETL
│   ├── transformaciones/    # Transformaciones de datos
│   └── pipelines/           # Pipelines completos
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

#### Nivel Mid (10/10 - ✅ 100% Completo)
- ✅ `01_apache_airflow_fundamentos.ipynb` - Orquestación con Airflow
- ✅ `02_streaming_kafka.ipynb` - Streaming con Kafka
- ✅ `03_cloud_aws.ipynb` - S3, Glue, Athena, Lambda
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

#### Nivel GenAI (10/10 - ✅ 100% Completo)
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

### 🧪 Tests Disponibles
- ✅ `tests/unit/test_transformations.py` - 16 pruebas unitarias
- ✅ `tests/integration/test_pipelines.py` - 15+ pruebas de integración

### 📚 Documentación
- ✅ Guía de instalación completa
- ✅ Roadmap del curso
- ✅ Referencias y recursos
- ✅ Guía de contribución
- ✅ Changelog

**Progreso General: ✅ 100% completo** (40/40 notebooks + infraestructura completa)

## 📊 Progreso por Nivel

| Nivel    | Duración | Notebooks | Completados | Proyectos | Estado        |
|----------|----------|-----------|-------------|-----------|---------------|
| Junior   | 6-8 sem  | 10        | 10 ✅       | 2 ✅      | ✅ Completo   |
| Mid      | 8-10 sem | 10        | 10 ✅       | 2 ✅      | ✅ Completo   |
| Senior   | 10-12 sem| 10        | 10 ✅       | 2 ✅      | ✅ Completo   |
| GenAI    | 4-6 sem  | 10        | 10 ✅       | 2 ✅      | ✅ Completo   |

## 🔧 Tecnologías Incluidas

### Lenguajes y Frameworks
- **Python** (Pandas, NumPy, SQLAlchemy)
- **SQL** (PostgreSQL, BigQuery)
- **YAML/JSON** para configuraciones

### Herramientas de Orquestación
- **Apache Airflow**
- **Prefect**
- **Dagster** (nivel Senior)

### Plataformas Cloud
- **AWS** (S3, Redshift, Lambda, Glue)
- **Google Cloud** (BigQuery, Cloud Functions, Dataflow)
- **Azure** (Synapse, Data Factory, Functions)

### IA Generativa
- **OpenAI** (GPT-4, GPT-3.5, Embeddings)
- **Anthropic Claude**
- **Google Gemini**
- **LangChain / LangGraph**
- **ChromaDB / FAISS**
- **AutoGen** (multi-agentes)

### Almacenamiento
- **PostgreSQL, MySQL**
- **MongoDB, Cassandra**
- **Redis** (caché)
- **Parquet, Delta Lake**

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

Este proyecto está bajo la Licencia MIT. Ver `LICENSE` para más detalles.

## 👥 Autores

- **Tu Nombre** - *Desarrollo inicial* - [Tu GitHub](https://github.com/tu-usuario)

## 🙏 Agradecimientos

- Comunidad de Python y Jupyter
- Contribuidores de bibliotecas open source
- Estudiantes y beta testers del curso

---

⭐ **¡Dale una estrella si este proyecto te ayuda!** ⭐