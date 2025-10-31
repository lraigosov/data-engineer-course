# ⚠️ IMPORTANTE - LEE ESTO ANTES DE EMPEZAR

## 🚨 SOBRE EL USO DE JUPYTER NOTEBOOKS

### ✅ Notebooks son EXCELENTES para:
- 📚 **Aprendizaje y enseñanza** (como este curso)
- 🔬 **Exploración y análisis de datos**
- 🧪 **Prototipado rápido**
- 📊 **Visualización interactiva**
- 📝 **Documentación técnica ejecutable**
- 🧑‍🏫 **Presentaciones y demos**

### ❌ Notebooks NO son recomendables para:
- 🏭 **Sistemas en producción**
- 🔄 **Pipelines ETL automatizados**
- ⚙️ **Workflows orquestados (Airflow, Prefect)**
- 🚀 **Aplicaciones escalables**
- 🔐 **Servicios con requisitos de seguridad estrictos**
- 📦 **Código que requiere testing exhaustivo**
- 🔁 **Procesos que se ejecutan repetidamente**

## 🏗️ MEJORES PRÁCTICAS PARA PRODUCCIÓN

### En lugar de notebooks, usa:

```
notebooks/ (Desarrollo y exploración)
    ↓
    Prototipo validado
    ↓
src/ (Código de producción)
├── pipelines/
│   ├── __init__.py
│   ├── extract.py          ← Módulos Python estructurados
│   ├── transform.py
│   └── load.py
├── models/
│   ├── schemas.py          ← Pydantic models
│   └── entities.py
├── services/
│   └── data_service.py     ← Business logic
├── utils/
│   ├── db.py               ← Database connectors
│   └── validators.py       ← Data validation
└── config/
    └── settings.py         ← Configuration management

tests/                      ← Testing comprehensivo
├── unit/
├── integration/
└── e2e/

.github/workflows/          ← CI/CD automation
└── deploy.yml

Dockerfile                  ← Containerization
docker-compose.yml

airflow/dags/               ← Orchestration
└── sales_pipeline_dag.py
```

## 🔄 FLUJO DE TRABAJO RECOMENDADO

### 1️⃣ EXPLORACIÓN (Notebooks ✅)
```python
# notebooks/exploration/01_explore_sales_data.ipynb
import pandas as pd

# Cargar datos
df = pd.read_csv('data/ventas.csv')

# Explorar
df.describe()
df.plot()

# Probar transformaciones
df['total_clean'] = df['total'].fillna(0)
```

### 2️⃣ PROTOTIPADO (Notebooks ✅)
```python
# notebooks/prototypes/02_sales_etl_prototype.ipynb

# Probar pipeline completo
def extract():
    return pd.read_csv('data/ventas.csv')

def transform(df):
    df['total_clean'] = df['total'].fillna(0)
    df['fecha'] = pd.to_datetime(df['fecha'])
    return df

def load(df):
    df.to_parquet('output/ventas_clean.parquet')

# Ejecutar y validar
df = extract()
df = transform(df)
load(df)
```

### 3️⃣ PRODUCCIÓN (Scripts Python ✅)
```python
# src/pipelines/sales_etl.py
from typing import Optional
import pandas as pd
from pydantic import BaseModel
import logging

logger = logging.getLogger(__name__)

class SalesETL:
    """Pipeline ETL para ventas - Versión producción"""
    
    def __init__(self, config: dict):
        self.config = config
    
    def extract(self) -> pd.DataFrame:
        """Extract sales data from source"""
        logger.info("Starting extraction...")
        try:
            df = pd.read_csv(self.config['source_path'])
            logger.info(f"Extracted {len(df)} records")
            return df
        except Exception as e:
            logger.error(f"Extraction failed: {e}")
            raise
    
    def transform(self, df: pd.DataFrame) -> pd.DataFrame:
        """Transform sales data"""
        logger.info("Starting transformation...")
        df['total_clean'] = df['total'].fillna(0)
        df['fecha'] = pd.to_datetime(df['fecha'])
        
        # Validaciones
        assert not df['total_clean'].isnull().any(), "Nulls found after cleaning"
        
        return df
    
    def load(self, df: pd.DataFrame) -> None:
        """Load to destination"""
        logger.info("Starting load...")
        df.to_parquet(
            self.config['destination_path'],
            compression='snappy',
            index=False
        )
        logger.info(f"Loaded {len(df)} records successfully")
    
    def run(self) -> None:
        """Execute full pipeline"""
        try:
            df = self.extract()
            df = self.transform(df)
            self.load(df)
            logger.info("Pipeline completed successfully")
        except Exception as e:
            logger.error(f"Pipeline failed: {e}")
            raise

# Entry point
if __name__ == '__main__':
    config = {
        'source_path': 'data/ventas.csv',
        'destination_path': 'output/ventas_clean.parquet'
    }
    
    pipeline = SalesETL(config)
    pipeline.run()
```

### 4️⃣ ORQUESTACIÓN (Airflow DAG ✅)
```python
# airflow/dags/sales_pipeline_dag.py
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

def run_sales_etl():
    from src.pipelines.sales_etl import SalesETL
    
    pipeline = SalesETL(config)
    pipeline.run()

default_args = {
    'owner': 'data-team',
    'depends_on_past': False,
    'start_date': datetime(2024, 1, 1),
    'email_on_failure': True,
    'email_on_retry': False,
    'retries': 3,
    'retry_delay': timedelta(minutes=5)
}

with DAG(
    'sales_etl_pipeline',
    default_args=default_args,
    description='Sales ETL pipeline',
    schedule_interval='0 2 * * *',  # Daily at 2 AM
    catchup=False,
    tags=['sales', 'etl']
) as dag:
    
    run_pipeline = PythonOperator(
        task_id='run_sales_etl',
        python_callable=run_sales_etl
    )
```

## 📊 COMPARACIÓN: NOTEBOOK vs PRODUCCIÓN

| Aspecto | Notebook (Desarrollo) | Script Python (Producción) |
|---------|----------------------|----------------------------|
| **Estructura** | Células secuenciales | Módulos y funciones |
| **Reusabilidad** | Baja (copy-paste) | Alta (imports) |
| **Testing** | Difícil | Fácil (pytest) |
| **CI/CD** | No integrable | Completamente integrable |
| **Logging** | Print statements | Logging estructurado |
| **Error Handling** | Básico | Robusto con retry |
| **Version Control** | Problemático (JSON) | Excelente (Python puro) |
| **Schedulling** | Manual | Automatizado (Airflow) |
| **Monitoring** | No | Sí (Datadog, Prometheus) |
| **Escalabilidad** | Limitada | Alta |
| **Mantenibilidad** | Baja | Alta |

## ⚠️ PROBLEMAS COMUNES DE NOTEBOOKS EN PRODUCCIÓN

### 1. Orden de ejecución no garantizado
```python
# Celda 10 ejecutada antes que Celda 5 → resultados inconsistentes
```

### 2. Estado oculto (hidden state)
```python
# Variables definidas en celdas eliminadas siguen en memoria
```

### 3. Difícil de testear
```python
# ¿Cómo hacer pytest de una celda específica?
```

### 4. No hay control de versiones efectivo
```python
# Git diff de notebooks es ilegible (JSON)
```

### 5. No se puede orquestar fácilmente
```python
# ¿Cómo correr un notebook con retry en Airflow?
```

## ✅ RESUMEN

### Este curso usa notebooks porque:
- ✅ Facilita el aprendizaje paso a paso
- ✅ Permite visualizar resultados inmediatamente
- ✅ Combina código y explicaciones
- ✅ Es interactivo y fácil de compartir

### En tu trabajo real usa:
- ✅ Scripts Python modulares (`.py`)
- ✅ Tests automatizados (pytest)
- ✅ CI/CD pipelines (GitHub Actions)
- ✅ Orquestadores (Airflow, Prefect)
- ✅ Contenedores (Docker)
- ✅ Monitoreo (Datadog, New Relic)

## 🎓 APRENDE AQUÍ, APLICA CORRECTAMENTE

**Los notebooks son una herramienta excelente para aprender Data Engineering, pero recuerda siempre:**

> **"Learn with notebooks, deploy with production code."**

---

**Autor:** LuisRai (Luis J. Raigoso V.)  
**Curso:** Data Engineering - Modular Course  
**Repositorio:** https://github.com/lraigosov/data-engineer-course

© 2024-2025 LuisRai - Todos los derechos reservados
