# Preguntas frecuentes

## ¿Debo ejecutar los notebooks en orden?

Sí. La ruta recomendada es Junior, Mid, Senior, GenAI y Negocio LATAM. Cada notebook incluye navegación de anterior/siguiente e índice del módulo.

## ¿Los notebooks reemplazan código de producción?

No. Los notebooks se usan para aprendizaje, exploración y prototipado. Para producción usa scripts versionados, pruebas automatizadas, CI/CD, orquestación y observabilidad.

## ¿Necesito cuentas cloud o API keys?

Solo para ejercicios opcionales que integran servicios externos. Los notebooks priorizan ejemplos locales o simulados cuando es posible.

## ¿Las cifras de impacto económico son reales?

Son escenarios didácticos salvo que el notebook indique una fuente concreta. En proyectos reales deben reemplazarse por métricas internas, supuestos documentados y referencias verificables.

## ¿Cómo valido el repositorio?

Ejecuta:

```bash
python scripts/validate_notebook_code.py
pytest -q
```
