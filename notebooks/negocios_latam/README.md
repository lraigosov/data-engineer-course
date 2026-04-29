# 📈 Ingeniería de Datos aplicada al Negocio (LATAM)

**Autor**: Luis J. Raigoso V. (LJRV) - [@lraigosov](https://github.com/lraigosov)

---

Esta sección conecta la ingeniería de datos con la estrategia de negocio en sectores clave de Latinoamérica. Cada notebook demuestra cómo las decisiones técnicas de ingeniería de datos impactan directamente en resultados de negocio cuantificables.

> Nota de rigor: las cifras de ahorro, mejora porcentual y ROI incluidas en los casos sectoriales son escenarios didácticos para practicar priorización y diseño de capacidades de datos. En una propuesta real deben reemplazarse por métricas internas, supuestos documentados y fuentes verificables.

## 🎯 Objetivos de Aprendizaje

- **Alinear estrategia de datos con OKRs corporativos** en contexto LATAM
- **Mapear capacidades técnicas a impacto económico** (OKR → KPI → ROI)
- **Diseñar pipelines con métricas de negocio** (OSA, OEE, OTIF, churn, NDVI)
- **Cuantificar valor de ingeniería de datos** con casos documentados
- **Implementar contratos de datos** con SLOs, ownership y responsabilidades
- **Aplicar patrones sectoriales** con restricciones reales (regulación, costos, latencia)

## 📚 Notebooks Completados (10/10)

### 01. Marco Estratégico
**`01_estrategia_datos_latam.ipynb`** ✅
- **Contenido:**
  - Rol de ingeniería de datos en estrategia corporativa
  - Características estructurales (confiabilidad, escalabilidad, gobernanza, velocidad, observabilidad)
  - Ventajas estratégicas (velocidad ejecución, calidad decisión, reducción riesgo, estandarización, AI enablement)
  - Resultados medibles (ciclos reporte, detección temprana, fricción auditoría, what-if scenarios)
  - Diagnóstico de madurez por dimensión
- **Visualización:** Plotly bar chart de madurez por dimensión
- **Frameworks:** DAMA-DMBOK, ISO 9001:2015 PHVA/PDCA, Data Mesh

### 02. Retail y Consumo Masivo
**`02_retail_consumo_masivo.ipynb`** ✅
- **Caso de uso:** Pipeline OSA (On-Shelf Availability) con POS/ERP/WMS
- **Escenario de impacto:** OSA 92%→96%, detección 48h→2h, ahorro **$1.8M/año**
- **Ejercicio práctico:** Validación calidad datos (nulls, negativos, cobertura)
- **Visualización:** Top 5 SKUs con mayor revenue
- **Tecnologías:** Pandas, SQL, data quality validation

### 03. Finanzas y Banca
**`03_finanzas_banca.ipynb`** ✅
- **Caso de uso:** Detección fraude streaming con Kafka + feature store
- **Escenario de impacto:** Latencia 24h→<200ms, detección 65%→89%, ahorro **$3.2M/año**
- **Ejercicio práctico:** Feature engineering para riesgo (horas nocturnas, montos altos, dispositivos nuevos)
- **Visualización:** Distribución ECL (Expected Credit Loss)
- **Tecnologías:** Kafka, feature stores, PD/LGD/EAD modeling

### 04. Salud y Farmacéutico
**`04_salud_farmaceutico.ipynb`** ✅
- **Caso de uso:** Interoperabilidad HL7/FHIR en emergencias
- **Escenario de impacto:** Tiempo espera 45→28 min, ahorro **$800k/año**
- **Ejercicio práctico:** Pseudonymización con SHA256 para protección PII
- **Visualización:** Box plot comparativo tiempos de espera
- **Tecnologías:** HL7/FHIR, privacy-differential analytics, data lineage

### 05. Energía y Recursos Naturales
**`05_energia_recursos_naturales.ipynb`** ✅
- **Caso de uso:** Mantenimiento predictivo IoT/SCADA
- **Escenario de impacto:** OEE 0.82→0.91, paradas 12→2/año, ahorro **$4.5M/año**
- **Ejercicio práctico:** Detección anomalías con rolling mean + 3-sigma
- **Visualización:** Time-series temperatura con umbral dinámico
- **Tecnologías:** IoT, SCADA, TSDB (InfluxDB/TimescaleDB), alertas <10s

### 06. Telecomunicaciones
**`06_telecomunicaciones.ipynb`** ✅
- **Caso de uso:** Reducción churn con CDR streaming + feature store
- **Escenario de impacto:** Churn 2.5%→1.4%, reacción 24h→15min, LTV salvado **$6.8M**
- **Ejercicio práctico:** Pipeline features churn (uso bajo, quejas altas, tenure)
- **Visualización:** Probabilidad churn por segmento cliente
- **Tecnologías:** CDR processing, GIS enrichment, feature engineering

### 07. Industria y Manufactura
**`07_industria_manufactura.ipynb`** ✅
- **Caso de uso:** SPC (Statistical Process Control) + visión computacional
- **Escenario de impacto:** Scrap 8%→2.8%, OEE 0.78→0.88, ahorro **$6.2M/año**
- **Ejercicio práctico:** Cálculo límites control 3-sigma, detección out-of-control
- **Visualización:** OEE por turno (disponibilidad × rendimiento × calidad)
- **Tecnologías:** PLC/SCADA integration, computer vision, SPC charts

### 08. Logística y Transporte
**`08_logistica_transporte.ipynb`** ✅
- **Caso de uso:** Routing optimization con telemetría GPS
- **Escenario de impacto:** OTIF 88%→96.5%, costo $45→$38/entrega, ahorro **$3.2M/año**
- **Ejercicio práctico:** Cálculo OTIF (On-Time In-Full) y costos logísticos
- **Visualización:** Histograma ETA vs tiempo real
- **Tecnologías:** GPS telemetry, VRP algorithms, geo-enrichment

### 09. Agro y Alimentos
**`09_agro_alimentos.ipynb`** ✅
- **Caso de uso:** Agricultura de precisión con satélite Sentinel-2
- **Escenario de impacto:** Yield 3.2→3.6 ton/ha (+12.5%), pérdidas 15%→7%, revenue adicional **$1.8M**
- **Ejercicio práctico:** Análisis variabilidad intra-lote con NDVI
- **Visualización:** Scatter NDVI vs yield con línea tendencia OLS
- **Tecnologías:** Satellite imagery, geospatial features, precision agriculture zones

### 10. Sector Público y Gobierno
**`10_sector_publico_gobierno.ipynb`** ✅
- **Caso de uso:** Interoperabilidad entre sistemas gubernamentales
- **Escenario de impacto:** Trámites 12→4.2 días, satisfacción 38%→74%, fraude +120% detección, ahorro 35% costos operativos
- **Ejercicio práctico:** Simulación interoperabilidad padrón electoral/registro impuestos
- **Visualización:** Box plot tiempos de procedimientos (antes/después)
- **Tecnologías:** API interoperability, lakehouse by domains, RPA integration

## 🔧 Componentes Técnicos

### Pipelines de Producción
```bash
# Pipeline Retail (OSA KPIs)
python scripts/pipelines/retail/pipeline_retail.py \
  --ventas datasets/raw/ventas.csv \
  --productos datasets/raw/productos.csv \
  --outdir datasets/processed/retail/

# Pipeline Manufactura (OEE por turno)
python scripts/pipelines/manufactura/pipeline_manufactura.py \
  --input datasets/raw/oee_data.csv \
  --outdir datasets/processed/manufactura/
```

### Tests Unitarios
```bash
# Ejecutar suite completa
pytest tests/unit/ -v

# Tests específicos
pytest tests/unit/test_pipeline_retail.py -v
pytest tests/unit/test_pipeline_manufactura.py -v

# Resultado: 18 passing
```

### Visualizaciones Plotly
Cada notebook incluye visualizaciones interactivas:
- Bar charts (OEE, churn, ECL, procedimientos)
- Box plots (tiempos espera, distribuciones)
- Scatter plots (correlaciones NDVI-yield)
- Time-series (temperatura, anomalías)
- Histograms (ETA, OTIF)

## 📊 Metodología: Puente Estrategia ↔ Ingeniería

Cada notebook sigue estructura estándar:

```
1. OKR de Negocio
   ↓
2. KPI Negocio (observable)
   ↓
3. KPI Datos (medible)
   ↓
4. Capacidades Ingeniería (implementable)
   ↓
5. Decisión Técnica (ejecutable)
   ↓
6. Impacto Económico ($, %, tiempo)
```

### Ejemplo Retail (OSA):
```python
contrato_datos = {
    'slo_latencia': '< 15 minutos (alerta quiebre)',
    'slo_freshness': '< 1 hora (sincronización POS)',
    'slo_completitud': '> 98% SKUs con stock actualizado',
    'propietario': 'Equipo Supply Chain Analytics',
    'datasets': ['ventas_pos', 'inventario_wms', 'productos_erp'],
    'decision': 'Reabastecimiento urgente si OSA < 95%',
    'impacto_economico': '$1.8M ahorro/año (ventas perdidas evitadas)'
}
```

## 🌎 Particularidades LATAM

### Contexto Económico
- Monedas múltiples e inflación variable (AR, VE, BR)
- Economías cash y sub-bancarización
- Tipo de cambio como variable crítica

### Contexto Técnico
- Direcciones sin normalización estándar (geocodificación compleja)
- Idiomas: español/portugués (NER para nombres propios)
- Conectividad intermitente (resiliencia pipelines)

### Contexto Regulatorio
- **Argentina**: Ley 25.326 Protección Datos Personales
- **México**: LFPDPPP (Ley Federal Protección Datos)
- **Colombia**: Ley 1581 Habeas Data
- **Brasil**: LGPD (Lei Geral de Proteção de Dados)
- **Chile**: Ley 19.628 Vida Privada
- **Sector Salud**: HIPAA-like regulations
- **Sector Financiero**: Basilea III, regulaciones locales

### Contexto de Datos
- Data sharing con marketplaces y aliados (contratos, SLAs)
- Calidad variable de fuentes externas
- Silos organizacionales y falta de estándares

## 🚀 Cómo Usar Este Módulo

### Ruta de Aprendizaje Recomendada

1. **Semana 1-2: Marco Conceptual**
   - Ejecutar `01_estrategia_datos_latam.ipynb`
   - Entender mapeo OKR→Capacidades→Impacto
   - Completar diagnóstico de madurez

2. **Semana 3-4: Casos Sectoriales (elegir 3)**
   - Seleccionar sectores de interés profesional
   - Ejecutar notebooks y ejercicios prácticos
   - Analizar patrones comunes entre sectores

3. **Semana 5-6: Implementación**
   - Ejecutar pipelines de producción (retail/manufactura)
   - Correr tests unitarios
   - Modificar pipelines para otros sectores

4. **Semana 7-8: Proyecto Personal**
   - Seleccionar sector no cubierto
   - Diseñar pipeline con métricas negocio
   - Documentar impacto económico esperado

### Para Profesionales en Ejercicio

- **Data Engineers**: Enfocarse en arquitecturas y SLOs por sector
- **Data Scientists**: Analizar feature engineering y métricas predictivas
- **Business Analysts**: Estudiar mapeo OKR→KPI y contratos de datos
- **Managers/Leaders**: Revisar marcos de cuantificación de impacto

## 📈 Resultados de Aprendizaje

Al completar este módulo, podrás:

✅ **Traducir OKRs** de negocio a arquitecturas de datos  
✅ **Diseñar contratos de datos** con SLOs y ownership claro  
✅ **Cuantificar ROI** de iniciativas de ingeniería de datos  
✅ **Aplicar patrones sectoriales** con restricciones reales  
✅ **Comunicar valor técnico** en términos de negocio  
✅ **Implementar pipelines** con métricas observables  
✅ **Negociar SLAs** con stakeholders de negocio  
✅ **Priorizar backlog** por impacto económico

## 🔗 Recursos Adicionales

### Frameworks de Referencia
- **DAMA-DMBOK 2**: Data governance y calidad
- **Data Mesh Principles**: Arquitectura descentralizada
- **FinOps Framework**: Optimización costos cloud
- **ITIL 4**: Service management (aplicado a datos)

### Certificaciones Relevantes
- **CDMP** (Certified Data Management Professional)
- **Cloud certifications** con enfoque data (AWS, GCP, Azure)
- **Industry-specific**: HIPAA, PCI-DSS, SOX

### Comunidades LATAM
- Data Engineering LATAM (LinkedIn)
- PyData LATAM meetups
- Cloud provider user groups locales

---

**Progreso del Módulo: ✅ 100% completo (10/10 notebooks)**

© 2024-2025 Luis J. Raigoso V. (LuisRai) - LJRV
