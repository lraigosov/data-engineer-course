# 🗺️ Roadmap del Curso - Ingeniería de Datos

**Autor**: Luis J. Raigoso V. (LJRV) - [@lraigosov](https://github.com/lraigosov)

---

## 📊 Visión General

Este roadmap detalla la progresión completa del curso, desde fundamentos hasta nivel Senior, incluyendo habilidades técnicas, proyectos prácticos y certificaciones por nivel.

---

## 🎯 Nivel Junior - Fundamentos (6-8 semanas)

### **Semana 1-2: Introducción y Setup**
#### Objetivos de Aprendizaje
- [ ] Comprender qué es la Ingeniería de Datos
- [ ] Configurar entorno de desarrollo
- [ ] Dominar Jupyter Notebooks
- [ ] Fundamentos de Git y GitHub

#### Notebooks y Contenido
1. **01_introduccion_ingenieria_datos.ipynb**
   - Rol del Data Engineer vs Data Scientist vs Data Analyst
   - Pipeline de datos conceptual
   - Casos de uso reales
   
2. **02_setup_entorno_desarrollo.ipynb**
   - Configuración de Python y bibliotecas
   - Virtual environments
   - Jupyter Lab y extensiones

3. **03_git_version_control.ipynb**
   - Git básico para proyectos de datos
   - Buenas prácticas de commits
   - Colaboración en equipo

#### Proyecto Práctico
- **Setup Personal:** Configurar entorno completo de desarrollo

---

### **Semana 3-4: Python para Datos**
#### Objetivos de Aprendizaje
- [ ] Dominar estructuras de datos en Python
- [ ] Manipulación de archivos y formatos
- [ ] Manejo de errores y logging
- [ ] Funciones y programación funcional

#### Notebooks y Contenido
4. **04_python_estructuras_datos.ipynb**
   - Listas, diccionarios, sets, tuplas
   - Comprehensions y generadores
   - Manejo de memoria eficiente

5. **05_archivos_formatos_datos.ipynb**
   - CSV, JSON, XML, Parquet
   - Lectura/escritura optimizada
   - Encoding y caracteres especiales

6. **06_funciones_modularidad.ipynb**
   - Funciones puras y side effects
   - Decoradores para logging
   - Módulos y paquetes

#### Proyecto Práctico
- **ETL Básico:** Extraer datos de CSV/JSON, transformar y guardar

---

### **Semana 5-6: Pandas y NumPy**
#### Objetivos de Aprendizaje
- [ ] Dominar DataFrames y Series
- [ ] Operaciones de limpieza de datos
- [ ] Agregaciones y transformaciones
- [ ] Visualización básica

#### Notebooks y Contenido
7. **07_pandas_fundamentos.ipynb**
   - DataFrames, Series, Index
   - Lectura de múltiples fuentes
   - Inspección y exploración

8. **08_limpieza_transformacion_datos.ipynb**
   - Valores nulos y duplicados
   - Tipos de datos y conversiones
   - Texto y expresiones regulares

9. **09_agregaciones_visualizacion.ipynb**
   - GroupBy y pivot tables
   - Matplotlib y Seaborn básico
   - Estadísticas descriptivas

#### Proyecto Práctico
- **Análisis Exploratorio:** Dataset real con limpieza completa

---

### **Semana 7-8: SQL y Bases de Datos**
#### Objetivos de Aprendizaje
- [ ] SQL básico e intermedio
- [ ] Conexiones desde Python
- [ ] Normalización de datos
- [ ] Optimización básica

#### Notebooks y Contenido
10. **10_sql_fundamentos.ipynb**
    - SELECT, WHERE, JOIN, GROUP BY
    - Subconsultas y CTEs
    - Funciones de ventana básicas

#### Proyecto Final Junior
- **Mini Data Warehouse:** Diseñar esquema y poblar con datos reales
- **Dashboard Básico:** Visualizaciones desde base de datos

---

## 🔧 Nivel Mid - Pipelines y Automatización (8-10 semanas)

### **Semana 9-10: Arquitecturas de Datos**
#### Objetivos de Aprendizaje
- [ ] Patrones de arquitectura (Batch, Streaming, Lambda)
- [ ] Data Lakes vs Data Warehouses
- [ ] Principios de diseño escalable
- [ ] Introducción a microservicios

#### Notebooks y Contenido
11. **11_arquitecturas_datos_modernas.ipynb**
    - Batch vs Streaming processing
    - Data Lake architecture
    - CAP theorem aplicado

12. **12_patrones_diseno_escalabilidad.ipynb**
    - Horizontal vs vertical scaling
    - Particionado y sharding
    - Caching strategies

#### Proyecto Práctico
- **Diseño de Arquitectura:** Propuesta para caso real de empresa

---

### **Semana 11-12: APIs y Conectores**
#### Objetivos de Aprendizaje
- [ ] APIs REST y GraphQL
- [ ] Autenticación y rate limiting
- [ ] Webhooks y eventos
- [ ] Protocolos de transferencia (SFTP, S3, etc.)

#### Notebooks y Contenido
13. **13_apis_rest_graphql.ipynb**
    - Requests y autenticación
    - Paginación y rate limiting
    - Error handling y retries

14. **14_conectores_protocolos.ipynb**
    - SFTP, FTP, S3 transfers
    - Message queues (RabbitMQ, Kafka basics)
    - Schedulers y cron jobs

#### Proyecto Práctico
- **API Integration:** Pipeline desde múltiples APIs públicas

---

### **Semana 13-14: Orquestación con Airflow**
#### Objetivos de Aprendizaje
- [ ] Conceptos de DAGs y tareas
- [ ] Operators y sensores
- [ ] Templating y variables
- [ ] Monitoring y alertas

#### Notebooks y Contenido
15. **15_apache_airflow_fundamentos.ipynb**
    - Instalación y configuración
    - Primer DAG simple
    - Web UI y CLI

16. **16_airflow_operadores_sensores.ipynb**
    - PythonOperator, BashOperator
    - SqlOperator, EmailOperator
    - Custom operators

17. **17_airflow_templating_variables.ipynb**
    - Jinja templating
    - Variables y connections
    - XCom para comunicación

#### Proyecto Práctico
- **Pipeline Automatizado:** ETL completo orquestado con Airflow

---

### **Semana 15-16: Bases de Datos NoSQL**
#### Objetivos de Aprendizaje
- [ ] MongoDB, Cassandra, Redis
- [ ] Modelado de datos NoSQL
- [ ] Casos de uso específicos
- [ ] Integración con pipelines

#### Notebooks y Contenido
18. **18_mongodb_documentos.ipynb**
    - PyMongo y operaciones CRUD
    - Agregación pipeline
    - Índices y performance

19. **19_redis_cache_sesiones.ipynb**
    - Redis como cache
    - Pub/Sub patterns
    - Integración con aplicaciones

#### Proyecto Práctico
- **Sistema Híbrido:** Pipeline con SQL + NoSQL + Cache

---

### **Semana 17-18: Cloud Computing Basics**
#### Objetivos de Aprendizaje
- [ ] AWS/GCP/Azure fundamentos
- [ ] Storage services (S3, GCS, Blob)
- [ ] Compute services básicos
- [ ] Networking y security

#### Notebooks y Contenido
20. **20_aws_fundamentos_data_engineering.ipynb**
    - S3, EC2, RDS basics
    - IAM y security groups
    - boto3 y automatización

#### Proyecto Final Mid
- **Pipeline Cloud:** Migrar proyecto local a cloud provider
- **Monitoreo:** Implementar alertas y dashboards

---

## 🚀 Nivel Senior - Arquitectura y Gobernanza (10-12 semanas)

### **Semana 19-20: Data Lakehouse y Arquitecturas Modernas**
#### Objetivos de Aprendizaje
- [ ] Delta Lake, Apache Iceberg
- [ ] Data Mesh concepts
- [ ] Event-driven architectures
- [ ] Real-time analytics

#### Notebooks y Contenido
21. **21_delta_lake_lakehouse.ipynb**
    - ACID transactions en data lakes
    - Time travel y versioning
    - Schema evolution

22. **22_data_mesh_descentralizado.ipynb**
    - Domain-driven data architecture
    - Data products
    - Self-serve data infrastructure

#### Proyecto Práctico
- **Modern Architecture:** Implementar lakehouse con governance

---

### **Semana 21-22: Stream Processing**
#### Objetivos de Aprendizaje
- [ ] Apache Kafka deep dive
- [ ] Stream processing con Apache Spark
- [ ] Real-time analytics
- [ ] Event sourcing patterns

#### Notebooks y Contenido
23. **23_apache_kafka_streaming.ipynb**
    - Kafka producers y consumers
    - Topics, partitions, replicas
    - Kafka Connect y Stream

24. **24_spark_streaming_analytics.ipynb**
    - Structured streaming
    - Window operations
    - Watermarks y late data

#### Proyecto Práctico
- **Real-time Pipeline:** Sistema de streaming end-to-end

---

### **Semana 23-24: Data Governance y Calidad**
#### Objetivos de Aprendizaje
- [ ] DAMA-DMBOK framework
- [ ] Data lineage y cataloging
- [ ] Data quality frameworks
- [ ] Compliance (GDPR, CCPA)

#### Notebooks y Contenido
25. **25_data_governance_catalogo.ipynb**
    - Apache Atlas o equivalente
    - Metadata management
    - Data lineage tracking

26. **26_calidad_validacion_datos.ipynb**
    - Great Expectations
    - Data profiling
    - Automated testing

#### Proyecto Práctico
- **Governance Implementation:** Sistema completo de gobernanza

---

### **Semana 25-26: Machine Learning Pipelines**
#### Objetivos de Aprendizaje
- [ ] MLOps fundamentals
- [ ] Feature stores
- [ ] Model serving
- [ ] A/B testing for ML

#### Notebooks y Contenido
27. **27_mlops_feature_stores.ipynb**
    - Feature engineering pipelines
    - Model training automation
    - Model deployment

28. **28_ab_testing_ml_systems.ipynb**
    - Experimental design
    - Statistical significance
    - Monitoring model performance

#### Proyecto Práctico
- **ML Pipeline:** End-to-end ML system con monitoreo

---

### **Semana 27-28: Cost Optimization y FinOps**
#### Objetivos de Aprendizaje
- [ ] Cloud cost optimization
- [ ] Resource rightsizing
- [ ] Reserved instances vs spot
- [ ] Cost allocation y chargeback

#### Notebooks y Contenido
29. **29_cloud_cost_optimization.ipynb**
    - Cost monitoring tools
    - Resource optimization
    - Automated scaling

30. **30_finops_data_engineering.ipynb**
    - Cost allocation models
    - ROI measurement
    - Budget alerts y governance

#### Proyecto Final Senior
- **Enterprise Architecture:** Diseño completo de plataforma de datos
- **Business Case:** Justificación económica y técnica

---

## 📋 Evaluación y Certificación

### Nivel Junior
- **Examen Teórico:** 40 preguntas (70% mínimo)
- **Proyecto Práctico:** ETL pipeline documentado
- **Presentación:** 10 minutos explicando solución

### Nivel Mid
- **Examen Teórico:** 50 preguntas (75% mínimo)
- **Proyecto Práctico:** Pipeline orquestado en cloud
- **Code Review:** Revisión de código por pares

### Nivel Senior
- **Caso de Estudio:** Propuesta de arquitectura completa
- **Presentación Ejecutiva:** 20 minutos ante panel
- **Mentoría:** Guiar a estudiante Junior

---

## 🎓 Habilidades por Nivel

### Junior (6-8 meses experiencia)
- Python intermedio
- SQL básico-intermedio
- Pandas, NumPy proficiency
- Git/GitHub workflows
- Jupyter notebooks
- ETL concepts
- Basic cloud awareness

### Mid (1-3 años experiencia)
- Pipeline orchestration
- API integrations
- NoSQL databases
- Cloud services (AWS/GCP/Azure)
- Performance optimization
- DataOps practices
- Monitoring y alerting

### Senior (3+ años experiencia)
- Architecture design
- Data governance
- Cost optimization
- Team leadership
- Strategic planning
- Vendor evaluation
- Cross-functional collaboration

---

## 🛠️ Herramientas por Nivel

### Nivel Junior
- Python, Pandas, NumPy
- Jupyter, VS Code
- Git, GitHub
- PostgreSQL
- Basic Linux

### Nivel Mid
- Apache Airflow
- Docker básico
- AWS/GCP services
- MongoDB, Redis
- API development
- CI/CD basics

### Nivel Senior
- Kubernetes
- Terraform
- Apache Spark
- Kafka, streaming
- Data governance tools
- Business intelligence
- Enterprise architecture

---

Este roadmap es una guía flexible. Los tiempos pueden variar según experiencia previa y dedicación del estudiante. ¡El objetivo es formar Data Engineers completos y preparados para el mercado actual! 🚀