# Nivel Mid: pipelines y automatización

Este directorio contiene doce notebooks intermedios sobre orquestación,
streaming, nube, bases de datos, DataOps y servicios de datos.

## Contenido

| Notebook | Tema principal |
| --- | --- |
| `01_apache_airflow_fundamentos.ipynb` | DAGs, tareas y operación básica con Airflow 3 |
| `02_streaming_kafka.ipynb` | Productores, consumidores y patrones de Kafka |
| `03_cloud_aws.ipynb` | S3, Glue, Athena y Lambda |
| `03b_cloud_gcp.ipynb` | Cloud Storage, BigQuery, Dataflow y Cloud Run |
| `03c_cloud_azure.ipynb` | ADLS, Synapse, Data Factory y Databricks |
| `04_bases_datos_postgresql_mongodb.ipynb` | PostgreSQL y MongoDB |
| `05_dataops_cicd.ipynb` | Pruebas, controles de calidad y CI/CD |
| `06_conectores_avanzados_rest_graphql_sftp.ipynb` | REST, GraphQL y SFTP |
| `07_optimizacion_sql_particionado.ipynb` | Planes de consulta, índices y particionado |
| `08_fastapi_servicios_datos.ipynb` | API de datos con FastAPI y Pydantic |
| `09_proyecto_integrador_1.ipynb` | API, validación, base de datos y Parquet |
| `10_proyecto_integrador_2.ipynb` | Kafka, enriquecimiento e idempotencia |

## Prerrequisitos

- Nivel Junior o conocimientos equivalentes de Python y SQL.
- Python 3.11, 3.12 o 3.13.
- Docker y cuentas cloud solo para los ejercicios que los indiquen.

Instala primero el entorno base según la
[guía de instalación](../../docs/guia_instalacion.md). Los servicios externos y
los grupos opcionales no son necesarios para leer todos los notebooks.

## Apache Airflow 3

Airflow se mantiene aislado del entorno base porque tiene un árbol de
dependencias amplio. Con `pip` 25.1 o posterior:

```bash
python -m pip install --group airflow
airflow db migrate
```

Para una instancia local de desarrollo, inicia en terminales separadas los
componentes que necesites:

```bash
airflow api-server --port 8080
airflow scheduler
airflow dag-processor
```

`airflow db init` y `airflow webserver` pertenecen al flujo anterior a
Airflow 3 y no deben usarse en esta guía. Consulta la
[guía oficial de actualización a Airflow 3](https://airflow.apache.org/docs/apache-airflow/stable/installation/upgrading_to_airflow3.html)
antes de migrar una instalación existente.

## Alcance de los ejemplos

Los notebooks cloud y Kafka incluyen ejercicios que pueden funcionar como
simulación local. Una cuenta, un clúster o credenciales reales solo se requieren
cuando la propia actividad lo indique. No uses credenciales de producción.
