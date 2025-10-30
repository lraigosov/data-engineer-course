# 📘 Guía de Proyecto: Curso Modular para Convertirse en Ingeniero de Datos

> **Nota**: Este documento representa el diseño original y la propuesta inicial del proyecto. El curso ha sido completamente implementado siguiendo estas directrices.

**Autor**: Luis J. Raigoso V. (LJRV) - [@lraigosov](https://github.com/lraigosov)  
**Estado**: ✅ Implementado completamente (40/40 notebooks)

---

## 🎯 Objetivo General

Diseñar y desarrollar un proyecto modular que contenga un curso completo y estructurado para formar a estudiantes desde cero hasta alcanzar los niveles **Junior**, **Mid**, y **Senior** en Ingeniería de Datos. El curso debe combinar teoría validada con práctica aplicada mediante **Notebooks interactivos (Jupyter o Colab)**, fomentando el aprendizaje activo a través de talleres, ejercicios guiados y casos de uso reales.

---

## 🧩 Estructura Modular del Proyecto

El proyecto debe organizarse bajo un enfoque **modular y escalable**, dividido en tres niveles progresivos:

### 1. **Nivel Junior – Fundamentos de Ingeniería de Datos**

* Introducción a la Ingeniería de Datos y su rol en el ecosistema de datos.
* Fundamentos de programación en Python orientado a datos.
* Conceptos básicos de sistemas operativos, redes y cloud computing.
* Manipulación de datos con **Pandas**, **NumPy**, y **SQL básico**.
* Introducción a los formatos de datos (CSV, JSON, Parquet, Avro).
* Primeros pasos con **ETL (Extract, Transform, Load)**.
* Uso básico de **Jupyter Notebooks** y control de versiones con **Git/GitHub**.

🧠 *Producto esperado:* conjunto de notebooks con ejercicios guiados sobre lectura, limpieza y transformación de datasets.

---

### 2. **Nivel Mid – Desarrollo y Automatización de Pipelines de Datos**

* Arquitecturas de datos: batch, streaming y lambda.
* Conectores y APIs (REST, GraphQL, SFTP, etc.).
* Diseño de pipelines con **Airflow**, **Prefect** o **Dagster**.
* Almacenamiento en bases de datos relacionales y no relacionales (PostgreSQL, MongoDB, BigQuery, etc.).
* Principios de **DataOps** y CI/CD para flujos de datos.
* Optimización de consultas SQL y particionado de datos.
* Introducción a la nube (AWS, Azure, GCP): servicios principales y casos prácticos.

🧠 *Producto esperado:* pipelines reproducibles y notebooks explicativos con pruebas funcionales, simulando entornos productivos.

---

### 3. **Nivel Senior – Arquitectura, Gobernanza y Escalabilidad**

* Diseño de arquitecturas de datos modernas (**Data Lakehouse, Data Mesh, Delta/Iceberg, BigLake**).
* Estrategias de orquestación, versionamiento y observabilidad de datos.
* **Data Governance y Calidad de Datos:** DAMA-DMBOK, catalogación, linaje, stewardship.
* **Cost Optimization y FinOps** en plataformas cloud.
* **Machine Learning Pipelines** y feature stores.
* Seguridad, cumplimiento (GDPR, ISO 27001) y auditoría de flujos.
* Buenas prácticas de documentación y estándares técnicos.

🧠 *Producto esperado:* notebooks avanzados con ejemplos de arquitecturas híbridas, simulación de orquestación, validaciones de calidad y monitoreo.

---

## 📁 Estructura de Carpetas Propuesta

```bash
curso_ingenieria_datos/
│
├── config/
│   ├── settings.yaml         # Parámetros de configuración global (paths, entorno, variables)
│   ├── credentials.example   # Ejemplo de credenciales anonimizadas
│
├── notebooks/
│   ├── nivel_junior/
│   ├── nivel_mid/
│   ├── nivel_senior/
│
├── datasets/
│   ├── raw/
│   ├── processed/
│   └── external/
│
├── docs/
│   ├── README.md
│   ├── guia_instalacion.md
│   ├── roadmap.md
│   └── referencias.md
│
├── tests/
│   ├── unit/
│   ├── integration/
│
├── scripts/
│   ├── etl/
│   ├── transformaciones/
│   ├── pipelines/
│
└── requirements.txt
```

---

## 💡 Metodología Didáctica

Cada módulo y lección debe seguir la siguiente estructura:

1. **Introducción teórica breve** (máximo 10 minutos de lectura o video).
2. **Explicación conceptual** con ejemplos y diagramas.
3. **Notebook práctico paso a paso**, donde cada celda explica qué hace y por qué.
4. **Taller o desafío** con un caso de uso real.
5. **Notebook de solución guiada** con explicación de cada paso.
6. **Evaluación corta** (quiz o mini-proyecto automatizado).

---

## 🧱 Requisitos Técnicos y Estándares del Proyecto

* Todos los notebooks deben ser **auto-contenidos** (ejecutables desde 0).
* Las dependencias deben especificarse en `requirements.txt` o `environment.yaml`.
* El código debe seguir **PEP8** y las buenas prácticas de documentación.
* Se usará **GitHub Actions** o **GitLab CI/CD** para validar notebooks y pipelines.
* Uso de **Dockerfile** opcional para entornos reproducibles.
* Incorporar ejemplos de integración con **APIs públicas y datos abiertos**.

---

## 🚀 Roadmap del Proyecto

| Fase   | Descripción                                           | Duración Estimada | Entregable                                         |
| ------ | ----------------------------------------------------- | ----------------- | -------------------------------------------------- |
| Fase 1 | Diseño de la estructura modular y setup base del repo | 2 semanas         | Repositorio inicial con estructura y ejemplos base |
| Fase 2 | Desarrollo del contenido Junior (10 notebooks)        | 4 semanas         | Carpeta `nivel_junior/` completa                   |
| Fase 3 | Desarrollo del contenido Mid (10 notebooks)           | 6 semanas         | Carpeta `nivel_mid/` completa                      |
| Fase 4 | Desarrollo del contenido Senior (10 notebooks)        | 8 semanas         | Carpeta `nivel_senior/` completa                   |
| Fase 5 | Revisión, QA y publicación del curso                  | 2 semanas         | Curso final validado y documentado                 |

---

## 📚 Buenas Prácticas de Documentación

* Cada notebook debe incluir encabezados con:

  * Objetivo de la lección
  * Duración estimada
  * Nivel de dificultad
  * Bibliografía o fuentes de referencia
* El repositorio debe contener un **README principal** con instrucciones de ejecución.
* Se debe incluir un archivo `CONTRIBUTING.md` para orientar futuras contribuciones.

---

## 🔗 Referencias Recomendadas

* *Designing Data-Intensive Applications* — Martin Kleppmann.
* *Data Engineering on Google Cloud Platform Specialization* — Coursera.
* *The Data Engineering Cookbook* — Andreas Kretz.
* *Big Data Fundamentals* — O'Reilly.

---

## 🧭 Conclusión

Este documento guía establece la base técnica y pedagógica para desarrollar un curso modular, práctico y reproducible que forme verdaderos profesionales en ingeniería de datos, con foco en la aplicación real, la calidad técnica y la progresión gradual del aprendizaje.
