# 🔧 Notebooks Nivel Mid

Este directorio contiene los notebooks del nivel Mid (Intermedio) del curso de Ingeniería de Datos.

## 📚 Contenido

### Notebooks Disponibles

1. **01_apache_airflow_fundamentos.ipynb**
   - Conceptos de DAGs
   - Operators y Tasks
   - Orquestación de pipelines
   - Monitoreo y debugging

2. **02_streaming_kafka.ipynb**
   - Fundamentos de Kafka (topics, partitions, brokers)
   - Productores y consumidores (Python)
   - Esquemas y serialización (Avro/JSON)
   - Patrones de consumo y reintentos

3. **03_cloud_aws.ipynb**
   - S3 como data lake
   - Glue (PySpark) para transformación
   - Athena para consultas SQL sobre S3
   - Disparadores con Lambda/EventBridge

3b. **03b_cloud_gcp.ipynb** 🆕
   - Cloud Storage con lifecycle management
   - BigQuery (serverless + optimización)
   - Dataflow con Apache Beam
   - Cloud Composer (Airflow managed)
   - Cloud Functions event-driven

3c. **03c_cloud_azure.ipynb** 🆕
   - ADLS Gen2 (hierarchical namespaces + ACLs)
   - Azure Synapse Analytics (dedicated + serverless)
   - Azure Data Factory (ETL/ELT orchestration)
   - Azure Databricks (Delta Lake + Photon)
   - Azure Functions (triggers múltiples)

4. **04_bases_datos_postgresql_mongodb.ipynb**
   - Conexión con SQLAlchemy (PostgreSQL) y PyMongo
   - Modelado, índices y agregaciones
   - Estrategias de carga (batch, upsert, idempotencia)

5. **05_dataops_cicd.ipynb**
   - Pruebas de datos (Great Expectations, Pandera)
   - Pre-commit (black, isort, flake8, pytest)
   - GitHub Actions (lint + tests)

6. **06_conectores_avanzados_rest_graphql_sftp.ipynb**
   - REST con paginación, backoff y validación
   - GraphQL (consultas y paginación)
   - SFTP con Paramiko (opcional)

7. **07_optimizacion_sql_particionado.ipynb**
   - EXPLAIN/ANALYZE, índices y selectividad
   - Particionado (PostgreSQL y data lakes)
   - Pruning y estrategias de almacenamiento columnar

8. **08_fastapi_servicios_datos.ipynb**
   - FastAPI + Pydantic: CRUD de ventas de ejemplo
   - Caché y pruebas de humo con requests
   - Opcional: Redis y rate limiting

9. **09_proyecto_integrador_1.ipynb**
   - API → validación → DB → Parquet
   - Orquestación con Airflow (DAG ejemplo)
   - Alertas y monitoreo básicos

10. **10_proyecto_integrador_2.ipynb**
   - Kafka → validación → enriquecimiento → Parquet particionado
   - Idempotencia (checkpoint) y métricas básicas
   - Consumidor/productor con modo simulación si no hay Kafka

## 🎯 Objetivos del Nivel Mid

- Arquitecturas de datos (Batch/Streaming)
- Orquestación con Airflow
- Bases de datos NoSQL (MongoDB, Redis)
- APIs y conectores avanzados (REST, GraphQL, SFTP)
- **Cloud computing multi-cloud (AWS, GCP, Azure)**
- DataOps y CI/CD
- Optimización de queries y particionado
- Servicios de datos con FastAPI

## 📋 Prerrequisitos

- Nivel Junior completado
- Experiencia con Python y SQL
- Familiaridad con línea de comandos
- Cuenta en un proveedor cloud (opcional)

## 🚀 Cómo Usar

1. Asegúrate de haber completado el nivel Junior
2. Instala dependencias adicionales (ver requirements.txt)
3. Configura credenciales en `config/credentials.yaml`
4. Ejecuta los notebooks en orden

## ⚙️ Configuración Adicional

### Apache Airflow
```bash
pip install apache-airflow==2.7.0
airflow db init
airflow webserver --port 8080
```

### Docker (Opcional)
Algunos notebooks pueden requerir Docker para ejercicios prácticos.

## 📝 Notas

- Notebooks más complejos y extensos que nivel Junior
- Tiempo estimado: 90-120 minutos por notebook
- Algunos ejercicios requieren servicios externos (cuentas cloud opcionales)
- **Cobertura completa multi-cloud**: AWS (práctico), GCP (práctico), Azure (práctico)
- Los notebooks cloud incluyen tablas comparativas entre proveedores

---

*¿Listo para el siguiente nivel? Continúa con Nivel Senior.*