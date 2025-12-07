#!/usr/bin/env python3
"""
Script para agregar secciones de navegación a todos los notebooks del curso.
Estructura: Agrega una celda de markdown al final de cada notebook con links de navegación.
"""

import json
import os
from pathlib import Path
from typing import Dict, List, Tuple

# Estructura del curso
NIVELES = {
    "nivel_junior": [
        "01_introduccion_ingenieria_datos",
        "02_python_manipulacion_datos",
        "03_pandas_fundamentos",
        "04_sql_basico",
        "05_limpieza_datos",
        "06_visualizacion_datos",
        "07_git_control_versiones",
        "08_apis_web_scraping",
        "09_proyecto_integrador_1",
        "10_proyecto_integrador_2",
    ],
    "nivel_mid": [
        "01_apache_airflow_fundamentos",
        "02_streaming_kafka",
        "03_cloud_aws",
        "03b_cloud_gcp",
        "03c_cloud_azure",
        "04_bases_datos_postgresql_mongodb",
        "05_dataops_cicd",
        "06_conectores_avanzados_rest_graphql_sftp",
        "07_optimizacion_sql_particionado",
        "08_fastapi_servicios_datos",
        "09_proyecto_integrador_1",
        "10_proyecto_integrador_2",
    ],
    "nivel_senior": [
        "01_data_governance_calidad",
        "02_lakehouse_delta_iceberg",
        "03_spark_streaming",
        "04_arquitecturas_modernas",
        "05_ml_pipelines_feature_stores",
        "06_cost_optimization_finops",
        "07_seguridad_compliance",
        "08_observabilidad_linaje",
        "09_proyecto_integrador_1",
        "10_proyecto_integrador_2",
    ],
    "nivel_genai": [
        "00_comparacion_openai_gemini",
        "01_fundamentos_llms_prompting",
        "02_generacion_sql_nl2sql",
        "03_generacion_codigo_etl",
        "04_rag_documentacion_datos",
        "05_embeddings_similitud_datos",
        "06_agentes_automatizacion",
        "07_calidad_validacion_llm",
        "08_sintesis_aumento_datos",
        "09_proyecto_integrador_1",
        "10_proyecto_integrador_2",
    ],
    "negocios_latam": [
        "01_estrategia_datos_latam",
        "02_retail_consumo_masivo",
        "03_finanzas_banca",
        "04_salud_farmaceutico",
        "05_energia_recursos_naturales",
        "06_telecomunicaciones",
        "07_industria_manufactura",
        "08_logistica_transporte",
        "09_agro_alimentos",
        "10_sector_publico_gobierno",
    ],
}

# Nombres legibles para los títulos
NOMBRES_LEGIBLES = {
    "00_comparacion_openai_gemini": "Comparación OpenAI vs Google Gemini",
    "01_introduccion_ingenieria_datos": "Introducción a la Ingeniería de Datos",
    "01_estrategia_datos_latam": "Estrategia de Datos LATAM: Marco Conceptual",
    "02_python_manipulacion_datos": "Programación en Python para Datos",
    "02_retail_consumo_masivo": "Retail y Consumo Masivo",
    "03_pandas_fundamentos": "Pandas Fundamentos",
    "03_finanzas_banca": "Finanzas y Banca",
    "04_sql_basico": "SQL Básico",
    "04_salud_farmaceutico": "Salud y Farmacéutico",
    "05_limpieza_datos": "Limpieza de Datos",
    "05_energia_recursos_naturales": "Energía y Recursos Naturales",
    "06_visualizacion_datos": "Visualización de Datos",
    "06_telecomunicaciones": "Telecomunicaciones",
    "07_git_control_versiones": "Git y Control de Versiones",
    "07_industria_manufactura": "Industria y Manufactura",
    "08_apis_web_scraping": "APIs y Web Scraping",
    "08_logistica_transporte": "Logística y Transporte",
    "09_proyecto_integrador_1": "Proyecto Integrador 1",
    "09_agro_alimentos": "Agro y Alimentos",
    "10_proyecto_integrador_2": "Proyecto Integrador 2",
    "10_sector_publico_gobierno": "Sector Público y Gobierno",
    "01_apache_airflow_fundamentos": "Apache Airflow: Fundamentos",
    "02_streaming_kafka": "Streaming con Kafka",
    "03_cloud_aws": "Cloud AWS: S3, Glue, Athena, Lambda",
    "03b_cloud_gcp": "Cloud GCP: BigQuery, Dataflow, Cloud Run",
    "03c_cloud_azure": "Cloud Azure: ADLS, Synapse, ADF, Databricks",
    "04_bases_datos_postgresql_mongodb": "Bases de Datos: PostgreSQL y MongoDB",
    "05_dataops_cicd": "DataOps y CI/CD",
    "06_conectores_avanzados_rest_graphql_sftp": "Conectores Avanzados: REST, GraphQL, SFTP",
    "07_optimizacion_sql_particionado": "Optimización SQL y Particionado",
    "08_fastapi_servicios_datos": "FastAPI y Servicios de Datos",
    "01_data_governance_calidad": "Gobernanza y Calidad de Datos",
    "02_lakehouse_delta_iceberg": "Data Lakehouse: Delta y Iceberg",
    "03_spark_streaming": "Spark Streaming Avanzado",
    "04_arquitecturas_modernas": "Arquitecturas Modernas: Lambda, Kappa, Data Mesh",
    "05_ml_pipelines_feature_stores": "ML Pipelines y Feature Stores",
    "06_cost_optimization_finops": "FinOps y Optimización de Costos Cloud",
    "07_seguridad_compliance": "Seguridad y Compliance",
    "08_observabilidad_linaje": "Observabilidad y Linaje de Datos",
    "01_fundamentos_llms_prompting": "Fundamentos de LLMs y Prompting",
    "02_generacion_sql_nl2sql": "Generación SQL: NL2SQL",
    "03_generacion_codigo_etl": "Generación Automática de Código ETL",
    "04_rag_documentacion_datos": "RAG: Documentación de Datos",
    "05_embeddings_similitud_datos": "Embeddings y Similitud de Datos",
    "06_agentes_automatizacion": "Agentes y Automatización",
    "07_calidad_validacion_llm": "Validación y Calidad con LLMs",
    "08_sintesis_aumento_datos": "Síntesis y Aumento de Datos",
}


def get_navigation_cell(nivel: str, notebook_name: str, indice: int) -> Dict:
    """Genera la celda de navegación para un notebook."""
    
    notebooks = NIVELES[nivel]
    total = len(notebooks)
    
    # Determinar anterior y siguiente
    if indice > 0:
        prev_notebook = notebooks[indice - 1]
        prev_link = f"[← {NOMBRES_LEGIBLES.get(prev_notebook, prev_notebook.replace('_', ' '))}]({prev_notebook}.ipynb)"
    else:
        if nivel == "negocios_latam":
            prev_link = "[← README del Curso](../../README.md)"
        else:
            prev_link = "[← README del Curso](../../README.md)"
    
    if indice < total - 1:
        next_notebook = notebooks[indice + 1]
        next_link = f"[{NOMBRES_LEGIBLES.get(next_notebook, next_notebook.replace('_', ' '))} →]({next_notebook}.ipynb)"
    else:
        # Último notebook: link al siguiente nivel si existe
        next_levels = {
            "nivel_junior": ("nivel_mid", "Nivel Mid - Pipelines y Automatización"),
            "nivel_mid": ("nivel_senior", "Nivel Senior - Arquitectura y Gobernanza"),
            "nivel_senior": ("nivel_genai", "Nivel GenAI - IA Generativa"),
            "nivel_genai": ("negocios_latam", "Negocio LATAM - Estrategia y Sectores"),
        }
        if nivel in next_levels:
            next_nivel, next_name = next_levels[nivel]
            next_link = f"[{next_name} →](../{next_nivel}/README.md)"
        else:
            next_link = ""
    
    # Construir índice del nivel actual
    indice_items = []
    for i, nb in enumerate(notebooks):
        nb_name = NOMBRES_LEGIBLES.get(nb, nb.replace("_", " ").title())
        if i == indice:
            indice_items.append(f"- [{nb_name}]({nb}.ipynb) ← 🔵 Estás aquí")
        else:
            indice_items.append(f"- [{nb_name}]({nb}.ipynb)")
    
    # Nombre del nivel
    nivel_names = {
        "nivel_junior": "Nivel Junior",
        "nivel_mid": "Nivel Mid",
        "nivel_senior": "Nivel Senior",
        "nivel_genai": "Nivel GenAI",
        "negocios_latam": "Negocio LATAM",
    }
    nivel_name = nivel_names.get(nivel, nivel)
    
    # Construir el markdown de navegación
    navigation_text = f"""---

## 🧭 Navegación

**← Anterior:** {prev_link}

**Siguiente →:** {next_link}

**📚 Índice de {nivel_name}:**
{chr(10).join(indice_items)}

**🎓 Otros Niveles:**
- [Nivel Junior](../nivel_junior/README.md)
- [Nivel Mid](../nivel_mid/README.md)
- [Nivel Senior](../nivel_senior/README.md)
- [Nivel GenAI](../nivel_genai/README.md)
- [Negocio LATAM](../negocios_latam/README.md)"""
    
    return {
        "cell_type": "markdown",
        "metadata": {},
        "source": navigation_text.split('\n'),
    }


def add_navigation_to_notebook(notebook_path: Path, nivel: str, indice: int):
    """Agrega la celda de navegación a un notebook."""
    
    try:
        # Intentar con utf-8, si falla, intentar con utf-8-sig o con manejo de errores
        try:
            with open(notebook_path, 'r', encoding='utf-8') as f:
                notebook = json.load(f)
        except (UnicodeDecodeError, json.JSONDecodeError):
            # Intentar con encoding más permisivo
            with open(notebook_path, 'rb') as f:
                content = f.read()
            # Decodificar ignorando errores inválidos
            text = content.decode('utf-8', errors='replace')
            notebook = json.loads(text)
        
        # Crear la celda de navegación
        nav_cell = get_navigation_cell(nivel, notebook_path.stem, indice)
        
        # Verificar si ya existe una celda de navegación (comenzaría con "---")
        if notebook["cells"] and notebook["cells"][-1]["cell_type"] == "markdown":
            last_cell_text = "".join(notebook["cells"][-1]["source"])
            if last_cell_text.startswith("---\n\n## 🧭 Navegación"):
                # Reemplazar la celda existente
                notebook["cells"][-1] = nav_cell
            else:
                # Agregar nueva celda
                notebook["cells"].append(nav_cell)
        else:
            # Agregar nueva celda
            notebook["cells"].append(nav_cell)
        
        # Guardar el notebook con encoding robusto
        with open(notebook_path, 'w', encoding='utf-8', errors='replace') as f:
            json.dump(notebook, f, indent=1, ensure_ascii=False)
        
        print(f"✅ {notebook_path.relative_to(notebook_path.parent.parent.parent)}")
        return True
    
    except Exception as e:
        print(f"❌ Error en {notebook_path}: {e}")
        return False


def main():
    """Función principal."""
    
    notebooks_dir = Path("f:/GitHub/data-engineer-course/notebooks")
    
    if not notebooks_dir.exists():
        print(f"❌ Directorio no encontrado: {notebooks_dir}")
        return
    
    total_processed = 0
    total_success = 0
    
    # Procesar cada nivel
    for nivel, notebooks in NIVELES.items():
        nivel_dir = notebooks_dir / nivel
        
        if not nivel_dir.exists():
            print(f"⚠️  Directorio no encontrado: {nivel_dir}")
            continue
        
        print(f"\n📂 Procesando {nivel.upper()}:")
        
        for indice, notebook_name in enumerate(notebooks):
            notebook_path = nivel_dir / f"{notebook_name}.ipynb"
            
            total_processed += 1
            if add_navigation_to_notebook(notebook_path, nivel, indice):
                total_success += 1
    
    print(f"\n✨ Resumen: {total_success}/{total_processed} notebooks procesados exitosamente")


if __name__ == "__main__":
    main()
