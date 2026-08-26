# Nivel GenAI: IA generativa para ingeniería de datos

Este directorio reúne once notebooks educativos sobre LLM, generación de SQL y
código, RAG, embeddings, agentes, calidad y datos sintéticos.

## Contenido

| Notebook | Tema principal |
| --- | --- |
| `00_comparacion_openai_gemini.ipynb` | Comparación de patrones entre OpenAI y Gemini |
| `01_fundamentos_llms_prompting.ipynb` | Fundamentos, instrucciones y evaluación |
| `02_generacion_sql_nl2sql.ipynb` | NL2SQL con validación y controles de seguridad |
| `03_generacion_codigo_etl.ipynb` | Generación asistida de ETL con revisión |
| `04_rag_documentacion_datos.ipynb` | RAG sobre documentación técnica |
| `05_embeddings_similitud_datos.ipynb` | Similitud, deduplicación y búsqueda semántica |
| `06_agentes_automatizacion.ipynb` | Agentes y límites operativos |
| `07_calidad_validacion_llm.ipynb` | Calidad asistida por modelos |
| `08_sintesis_aumento_datos.ipynb` | Datos sintéticos y evaluación de utilidad |
| `09_proyecto_integrador_1.ipynb` | Chatbot con RAG y NL2SQL |
| `10_proyecto_integrador_2.ipynb` | Plataforma self-service asistida por GenAI |

## Instalación

Completa primero el entorno base de la
[guía de instalación](../../docs/guia_instalacion.md). Con `pip` 25.1 o
posterior, instala el grupo declarado por el repositorio:

```bash
python -m pip install --group genai
```

Este grupo contiene los SDK y herramientas realmente declarados en
`pyproject.toml`: OpenAI, Google GenAI, LangChain, LangGraph, ChromaDB, FAISS,
Sentence Transformers y Tiktoken. Otras tecnologías mencionadas con fines
comparativos no forman parte del entorno predeterminado.

## Credenciales y modelos

1. Copia `notebooks/nivel_genai/.env.example` como `.env`.
2. Configura únicamente la clave del proveedor que vas a usar.
3. Mantén `.env` fuera de Git y nunca uses secretos de producción.
4. Verifica el identificador del modelo justo antes de ejecutar: catálogos,
   disponibilidad, cuotas y precios cambian independientemente del curso.

Los ejemplos modernos de OpenAI usan la Responses API. Los ejemplos de Gemini
usan el SDK `google-genai`; el SDK heredado no es la referencia de esta guía.
Consulta los catálogos oficiales de
[modelos OpenAI](https://developers.openai.com/api/docs/models) y
[modelos Gemini](https://ai.google.dev/gemini-api/docs/models).

## Límites del entorno automatizado

La CI valida la estructura y sintaxis de todos los notebooks, pero solo ejecuta
la allowlist local de `config/notebooks-ci.txt`. Los notebooks de este directorio
requieren credenciales o modelos externos y no se ejecutan automáticamente.
Contenido escrito no equivale a una llamada de API validada.

## Seguridad y calidad

- No envíes PII, secretos ni datos regulados a un proveedor sin autorización.
- Trata toda salida del modelo como entrada no confiable; valida SQL y código
  antes de ejecutarlos.
- Limita tokens, tiempo, reintentos y presupuesto desde la aplicación.
- Registra modelo, versión, parámetros y conjunto de evaluación para que una
  comparación sea reproducible.
- Confirma costos en las páginas oficiales de
  [OpenAI](https://openai.com/api/pricing/) y
  [Gemini](https://ai.google.dev/gemini-api/docs/pricing); esta documentación no
  publica estimaciones fijas.
