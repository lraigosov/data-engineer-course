# Ingeniería de datos aplicada al negocio en LATAM

Este módulo contiene diez escenarios educativos que conectan decisiones de
ingeniería con objetivos y métricas de negocio en contextos latinoamericanos.

> Las cifras de ahorro, mejora, latencia y ROI son supuestos didácticos. No son
> datos de clientes ni benchmarks auditados. En un caso real deben sustituirse
> por métricas internas, supuestos fechados y fuentes verificables.

## Contenido

| Notebook | Contexto | Tema de datos |
| --- | --- | --- |
| `01_estrategia_datos_latam.ipynb` | Estrategia | Madurez, capacidades y decisiones |
| `02_retail_consumo_masivo.ipynb` | Retail | Disponibilidad en góndola y calidad |
| `03_finanzas_banca.ipynb` | Finanzas | Detección de fraude y variables de riesgo |
| `04_salud_farmaceutico.ipynb` | Salud | Interoperabilidad y protección de datos |
| `05_energia_recursos_naturales.ipynb` | Energía | Telemetría y mantenimiento predictivo |
| `06_telecomunicaciones.ipynb` | Telecomunicaciones | Churn y procesamiento de eventos |
| `07_industria_manufactura.ipynb` | Manufactura | SPC y OEE |
| `08_logistica_transporte.ipynb` | Logística | OTIF, ETA y costos |
| `09_agro_alimentos.ipynb` | Agro | NDVI y variabilidad de rendimiento |
| `10_sector_publico_gobierno.ipynb` | Sector público | Interoperabilidad y tiempos de trámite |

## Método de trabajo

Cada escenario sigue la relación:

```text
objetivo → KPI de negocio → KPI de datos → capacidad → decisión → impacto
```

Para que el ejercicio sea defendible:

1. identifica qué valores son supuestos;
2. documenta período, moneda, fuente y fórmula de cada métrica;
3. distingue correlación, estimación y efecto causal;
4. incorpora restricciones regulatorias solo después de verificarlas con una
   fuente oficial y asesoría aplicable a la jurisdicción;
5. expresa incertidumbre y realiza análisis de sensibilidad.

## Componentes ejecutables

Desde la raíz del repositorio y con el entorno instalado:

```bash
python scripts/pipelines/retail/pipeline_retail.py --help
python scripts/pipelines/manufactura/pipeline_manufactura.py --help
pytest -q
```

La suite completa contiene 17 pruebas automatizadas al 26 de agosto de 2026.
Consulta la [guía de instalación](../../docs/guia_instalacion.md) para reproducir
el entorno y las [rúbricas](../../docs/rubricas.md) para evaluar evidencias.

## Resultado esperado

Al finalizar, el estudiante debe poder explicar cómo una decisión técnica
afecta una métrica, qué evidencia respalda esa relación y cuáles son sus
limitaciones. Completar el texto de un notebook no demuestra por sí solo un
impacto económico real.
