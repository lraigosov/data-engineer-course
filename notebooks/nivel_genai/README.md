# 🤖 Notebooks Nivel GenAI - IA Generativa para Ingeniería de Datos

Este directorio contiene notebooks especializados en aplicaciones de **IA Generativa** (GenAI) para Ingeniería de Datos, incluyendo LLMs, RAG, agentes y automatización inteligente.

## 🎯 Objetivos del Módulo GenAI

Este nivel especializado enseña a:
- Integrar LLMs en pipelines de datos
- Automatizar generación de SQL, código ETL y documentación
- Implementar RAG para consultas sobre metadatos
- Usar embeddings para búsqueda semántica y deduplicación
- Construir agentes para automatización de tareas
- Generar datos sintéticos y validar calidad con LLMs
- Crear chatbots empresariales sobre datos

## 📚 Contenido

### Notebooks Disponibles

1. **00_comparacion_openai_gemini.ipynb**
   - Comparación práctica de proveedores, costos y patrones de uso

2. **01_fundamentos_llms_prompting.ipynb**
   - Fundamentos de LLMs, prompting y evaluación básica

3. **02_generacion_sql_nl2sql.ipynb**
   - Text-to-SQL con validación y controles de seguridad

4. **03_generacion_codigo_etl.ipynb**
   - Generación asistida de código ETL con revisión y pruebas

5. **04_rag_documentacion_datos.ipynb**
   - RAG sobre documentación técnica y catálogos de datos

6. **05_embeddings_similitud_datos.ipynb**
   - Embeddings, similitud, deduplicación y búsqueda semántica

7. **06_agentes_automatizacion.ipynb**
   - Agentes para automatización de tareas de ingeniería de datos

8. **07_calidad_validacion_llm.ipynb**
   - Validación de calidad asistida por LLMs

9. **08_sintesis_aumento_datos.ipynb**
   - Datos sintéticos, anonimización y evaluación de utilidad

10. **09_proyecto_integrador_1.ipynb**
    - Chatbot de consulta de datos con RAG

11. **10_proyecto_integrador_2.ipynb**
    - Plataforma self-service con GenAI

## 🔑 Prerrequisitos

- **Técnicos**:
  - Niveles Junior y Mid completados
  - Python avanzado y APIs REST
  - Experiencia con pipelines de datos
  - Conceptos de ML básicos (opcional)

- **Acceso a APIs**:
  - OpenAI API key para modelos de texto y embeddings
  - Google Gemini API key para modelos de texto y embeddings
  - Anthropic Claude API key (opcional)
  - Azure OpenAI (opcional)
  - Modelos locales: Ollama, LM Studio (opcional)

## 💡 Tecnologías Principales

- **LLMs**: OpenAI, Google Gemini, Anthropic Claude y modelos locales
- **Frameworks**: LangChain, LlamaIndex, LangGraph
- **Embeddings**: OpenAI Ada-002, Google Embeddings, Sentence Transformers
- **Vector DBs**: ChromaDB, Pinecone, Qdrant, FAISS
- **Agentes**: LangGraph, AutoGen
- **Evaluación**: Ragas, LangSmith

## ⚙️ Configuración Inicial

### 1. Variables de Entorno

```bash
# .env

# OpenAI (principal en los ejemplos)
OPENAI_API_KEY=sk-...

# Google Gemini (también usado en ejemplos)
GOOGLE_API_KEY=AIza...
GEMINI_API_KEY=AIza...  # Alternativa

# Otros proveedores (opcionales)
ANTHROPIC_API_KEY=sk-ant-...
AZURE_OPENAI_API_KEY=...
AZURE_OPENAI_ENDPOINT=https://...

# Tracking y monitoreo
LANGCHAIN_API_KEY=ls-...
LANGCHAIN_TRACING_V2=true
LANGCHAIN_PROJECT=data-eng-genai
```

### 2. Dependencias Adicionales

```bash
# LLM Providers
pip install openai anthropic google-generativeai
pip install langchain langchain-openai langchain-google-genai

# Vector stores y embeddings
pip install chromadb faiss-cpu sentence-transformers tiktoken

# Agentes y frameworks avanzados
pip install langchain-community langgraph pyautogen

# Evaluación y monitoreo
pip install ragas langsmith
```

### 3. Costos y Límites

Los precios, ventanas de contexto y límites de rate limit cambian con frecuencia. Antes de ejecutar ejercicios con APIs pagas, revisa la página oficial de precios y cuotas del proveedor que uses:
- OpenAI: https://openai.com/api/pricing/
- Google Gemini: https://ai.google.dev/pricing
- Anthropic Claude: https://www.anthropic.com/pricing

**Recomendaciones**:
- Usa modelos económicos para pruebas y desarrollo
- Reserva modelos de mayor capacidad para tareas críticas o evaluaciones finales
- Implementa caché para reducir llamadas repetidas
- Establece límites de tokens por request (max_tokens)
- Monitorea costos con LangSmith o dashboards custom

## 🎓 Estructura de Aprendizaje

Cada notebook incluye:
1. **Conceptos**: Teoría de GenAI aplicada a datos
2. **Ejemplos**: Casos reales con código ejecutable
3. **Mejores prácticas**: Prompting, error handling, costos
4. **Ejercicios**: Implementaciones guiadas
5. **Proyecto mini**: Aplicación práctica del concepto

## 🚀 Casos de Uso Cubiertos

- 📊 **Text-to-SQL**: Consultas en lenguaje natural
- 🔧 **Code Generation**: ETL automático desde descripciones
- 📚 **RAG**: Chatbot sobre documentación técnica
- 🔍 **Semantic Search**: Búsqueda inteligente en data catalog
- 🤖 **Agents**: Automatización de tareas repetitivas
- ✅ **Validation**: Control de calidad con LLMs
- 🎲 **Synthetic Data**: Generación de datasets de prueba
- 💬 **Chatbots**: Interfaces conversacionales para datos

## ⚠️ Consideraciones Importantes

### Seguridad
- **NUNCA** expongas API keys en código
- Usa variables de entorno o gestores de secretos
- No envíes PII a LLMs externos sin anonimizar
- Implementa rate limiting y timeouts

### Calidad
- Valida siempre las respuestas del LLM
- Usa few-shot prompting para mayor precisión
- Implementa fallbacks ante errores
- Monitorea latencia y costos

### Ética
- Transparencia: indica cuándo usa IA
- No reemplaces juicio humano crítico
- Audita sesgos en generación de datos
- Cumple con políticas de uso de cada proveedor

## 📊 Proyectos Integradores

1. **Chatbot de Datos Empresariales**
   - RAG sobre catálogo + lakehouse
   - Text-to-SQL con validación
   - Dashboard conversacional

2. **Plataforma Self-Service con GenAI**
   - Generación automática de pipelines
   - Documentación auto-generada
   - Agentes de mantenimiento
   - Alertas inteligentes

## 📝 Notas

- **Duración estimada**: 90-120 min por notebook
- **Nivel de dificultad**: Medio/Alto
- **Costos estimados**: $5-20 en APIs durante el curso completo
- **Actualización**: revisar precios y nombres de modelos antes de ejecutar laboratorios con APIs externas

## 🔗 Referencias

- [OpenAI API Docs](https://platform.openai.com/docs)
- [Google Gemini API Docs](https://ai.google.dev/docs)
- [LangChain Docs](https://python.langchain.com/)
- [LangChain Google Integration](https://python.langchain.com/docs/integrations/platforms/google)
- [LlamaIndex](https://docs.llamaindex.ai/)
- [Prompt Engineering Guide](https://www.promptingguide.ai/)
- [Google AI Studio](https://makersuite.google.com/app/prompts/new_freeform) - Playground para Gemini

---

*¡Bienvenido a la frontera de la Ingeniería de Datos con IA! 🚀*
