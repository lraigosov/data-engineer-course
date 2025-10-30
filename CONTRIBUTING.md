# 🤝 Guía de Contribución - Curso de Ingeniería de Datos

¡Gracias por tu interés en contribuir al proyecto! Esta guía te ayudará a participar de manera efectiva y mantener la calidad del contenido educativo.

## 🎯 Tipos de Contribuciones

### 📚 Contenido Educativo
- **Nuevos notebooks**: Lecciones adicionales o temas específicos
- **Mejoras en explicaciones**: Clarificar conceptos complejos
- **Ejercicios prácticos**: Casos de uso reales y desafíos
- **Datasets**: Nuevos conjuntos de datos para ejercicios

### 🐛 Correcciones y Mejoras
- **Errores en código**: Bugs en notebooks o scripts
- **Errores tipográficos**: Documentación y comentarios
- **Optimizaciones**: Mejorar rendimiento del código
- **Actualizaciones**: Versiones de librerías y APIs

### 🛠️ Infraestructura
- **Testing**: Pruebas automatizadas para notebooks
- **CI/CD**: Mejoras en workflows de GitHub Actions
- **Documentación**: Guías y referencias
- **Herramientas**: Scripts de utilidad y automatización

## 🚀 Proceso de Contribución

### 1. Preparar el Entorno
```bash
# Fork del repositorio en GitHub
git clone https://github.com/tu-usuario/curso-ingenieria-datos.git
cd curso-ingenieria-datos

# Configurar upstream
git remote add upstream https://github.com/original/curso-ingenieria-datos.git

# Crear entorno virtual
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Instalar dependencias
pip install -r requirements.txt
pip install -r requirements-dev.txt  # Herramientas de desarrollo
```

### 2. Crear Branch de Trabajo
```bash
# Sincronizar con upstream
git fetch upstream
git checkout main
git merge upstream/main

# Crear nueva rama
git checkout -b feature/nombre-descriptivo
# o
git checkout -b fix/descripcion-del-bug
# o
git checkout -b docs/mejora-documentacion
```

### 3. Realizar Cambios

#### Para Notebooks
- **Ejecutar completamente**: Asegúrate de que el notebook se ejecute sin errores
- **Limpiar outputs**: Usar `jupyter nbconvert --clear-output` antes del commit
- **Documentar bien**: Cada celda debe tener explicaciones claras
- **Incluir metadata**: Objetivo, duración, nivel de dificultad

#### Para Código Python
- **Seguir PEP 8**: Usar black para formateo automático
- **Documentar funciones**: Docstrings claros y completos
- **Type hints**: Usar anotaciones de tipos cuando sea apropiado
- **Tests**: Incluir pruebas para nuevo código

### 4. Validar Cambios
```bash
# Formatear código
black .

# Verificar linting
flake8 .

# Ejecutar tests
pytest

# Validar notebooks
pytest --nbval notebooks/
```

### 5. Commit y Push
```bash
# Agregar cambios
git add .

# Commit con mensaje descriptivo
git commit -m "feat: agregar notebook sobre Apache Kafka

- Introducción a conceptos de streaming
- Ejemplos prácticos con kafka-python
- Ejercicios con casos de uso reales
- Tests automatizados incluidos"

# Push a tu fork
git push origin feature/nombre-descriptivo
```

### 6. Crear Pull Request
- **Título claro**: Describe el cambio principal
- **Descripción detallada**: Explica qué, por qué y cómo
- **Screenshots**: Para cambios visuales
- **Testing**: Describe cómo probaste los cambios
- **Referencias**: Issues relacionados

## 📝 Estándares de Calidad

### Notebooks (.ipynb)
```python
# Estructura estándar de notebook
"""
# [Nivel] - [Número]. [Título del Notebook]

**Objetivos de Aprendizaje:**
- [ ] Objetivo 1
- [ ] Objetivo 2

**Duración Estimada:** 45-60 minutos
**Nivel de Dificultad:** Principiante/Intermedio/Avanzado
**Prerrequisitos:** Lista de notebooks anteriores

**Datasets Necesarios:**
- dataset1.csv (descripción)
- dataset2.json (descripción)
"""

# Cada celda debe tener comentarios explicativos
import pandas as pd
import numpy as np

# Cargar datos con manejo de errores
try:
    df = pd.read_csv('../datasets/raw/ejemplo.csv')
    print(f"✅ Datos cargados: {df.shape[0]} filas, {df.shape[1]} columnas")
except FileNotFoundError:
    print("❌ Error: No se encontró el archivo de datos")
    print("📝 Instrucción: Ejecutar notebook de descarga de datos primero")
```

### Código Python (.py)
```python
"""
Módulo: transformaciones.py
Descripción: Funciones para transformación de datos
Autor: Tu Nombre
Fecha: 2024-01-01
"""

from typing import Optional, List, Dict, Any
import pandas as pd
import logging

# Configurar logging
logger = logging.getLogger(__name__)


def limpiar_datos(
    df: pd.DataFrame,
    columnas_numericas: Optional[List[str]] = None,
    eliminar_duplicados: bool = True
) -> pd.DataFrame:
    """
    Limpia un DataFrame aplicando transformaciones estándar.
    
    Args:
        df: DataFrame a limpiar
        columnas_numericas: Lista de columnas a convertir a numérico
        eliminar_duplicados: Si eliminar filas duplicadas
        
    Returns:
        DataFrame limpio
        
    Raises:
        ValueError: Si el DataFrame está vacío
        
    Example:
        >>> df = pd.DataFrame({'A': ['1', '2', 'invalid'], 'B': [1, 2, 3]})
        >>> df_limpio = limpiar_datos(df, columnas_numericas=['A'])
        >>> assert df_limpio['A'].dtype == 'float64'
    """
    if df.empty:
        raise ValueError("El DataFrame no puede estar vacío")
    
    df_resultado = df.copy()
    
    # Log del estado inicial
    logger.info(f"Limpiando DataFrame: {df.shape[0]} filas, {df.shape[1]} columnas")
    
    # Convertir columnas numéricas
    if columnas_numericas:
        for col in columnas_numericas:
            df_resultado[col] = pd.to_numeric(df_resultado[col], errors='coerce')
    
    # Eliminar duplicados si se solicita
    if eliminar_duplicados:
        duplicados_antes = df_resultado.duplicated().sum()
        df_resultado = df_resultado.drop_duplicates()
        logger.info(f"Eliminados {duplicados_antes} duplicados")
    
    logger.info(f"DataFrame limpio: {df_resultado.shape[0]} filas")
    return df_resultado
```

### Tests (.py)
```python
"""
test_transformaciones.py
Tests para el módulo de transformaciones
"""

import pytest
import pandas as pd
import numpy as np
from scripts.transformaciones import limpiar_datos


class TestLimpiarDatos:
    """Tests para la función limpiar_datos"""
    
    def test_dataframe_vacio_genera_error(self):
        """Test que DataFrame vacío genera ValueError"""
        df_vacio = pd.DataFrame()
        
        with pytest.raises(ValueError, match="El DataFrame no puede estar vacío"):
            limpiar_datos(df_vacio)
    
    def test_conversion_columnas_numericas(self):
        """Test conversión de columnas a numéricas"""
        df = pd.DataFrame({
            'A': ['1', '2', '3'],
            'B': ['text1', 'text2', 'text3']
        })
        
        resultado = limpiar_datos(df, columnas_numericas=['A'])
        
        assert resultado['A'].dtype in ['int64', 'float64']
        assert resultado['B'].dtype == 'object'
    
    def test_eliminacion_duplicados(self):
        """Test eliminación de filas duplicadas"""
        df = pd.DataFrame({
            'A': [1, 2, 2, 3],
            'B': ['a', 'b', 'b', 'c']
        })
        
        resultado = limpiar_datos(df, eliminar_duplicados=True)
        
        assert len(resultado) == 3
        assert not resultado.duplicated().any()
    
    @pytest.fixture
    def sample_dataframe(self):
        """Fixture con DataFrame de ejemplo"""
        return pd.DataFrame({
            'numeros': ['1', '2', 'invalid', '4'],
            'texto': ['a', 'b', 'c', 'd'],
            'duplicado': [1, 1, 2, 3]
        })
    
    def test_integracion_completa(self, sample_dataframe):
        """Test de integración con todas las funcionalidades"""
        resultado = limpiar_datos(
            sample_dataframe,
            columnas_numericas=['numeros'],
            eliminar_duplicados=True
        )
        
        assert len(resultado) == 4  # Sin duplicados en este caso
        assert resultado['numeros'].dtype in ['int64', 'float64']
        assert pd.isna(resultado['numeros'].iloc[2])  # 'invalid' -> NaN
```

## 🔍 Review Process

### Criterios de Aprobación
- [ ] **Funcionalidad**: El código funciona correctamente
- [ ] **Tests**: Pruebas pasan y cubren casos relevantes
- [ ] **Documentación**: Clara y completa
- [ ] **Estilo**: Sigue las convenciones del proyecto
- [ ] **Compatibilidad**: No rompe funcionalidad existente

### Checklist para Reviewers
- [ ] Ejecutar notebook completamente
- [ ] Verificar explicaciones pedagógicas
- [ ] Validar ejemplos y ejercicios
- [ ] Comprobar manejo de errores
- [ ] Revisar performance en datasets grandes

## 🏷️ Convenciones de Naming

### Branches
```
feature/[area]-[descripcion-corta]
fix/[area]-[descripcion-bug]
docs/[tipo-documentacion]
test/[area-testing]
refactor/[area-refactored]

# Ejemplos:
feature/junior-pandas-advanced
fix/airflow-dag-scheduling
docs/installation-guide
test/etl-pipeline-validation
```

### Commits
Usar [Conventional Commits](https://www.conventionalcommits.org/):

```
tipo(scope): descripción

# Tipos válidos:
feat:     Nueva funcionalidad
fix:      Corrección de bug
docs:     Solo documentación
style:    Formateo, punto y coma, etc
refactor: Cambio de código que no es fix ni feature
test:     Agregar o corregir tests
chore:    Cambios en build, dependencias, etc

# Ejemplos:
feat(junior): agregar notebook de introducción a SQL
fix(pipeline): corregir error en transformación de fechas
docs(readme): actualizar instrucciones de instalación
test(etl): agregar tests para validación de datos
```

## 🎨 Estilo Visual

### Notebooks
- **Títulos**: Usar markdown headers (# ## ###)
- **Code blocks**: Indentar consistentemente (4 espacios)
- **Outputs**: Limpiar antes de commit
- **Imágenes**: Incluir alt text y dimensiones apropiadas

### Documentación
- **Emojis**: Usar consistentemente para secciones
- **Links**: Preferir referencias relativas cuando sea posible
- **Código**: Siempre en code blocks con syntax highlighting

## 🐛 Reportar Issues

### Bug Reports
```markdown
## 🐛 Descripción del Bug
Descripción clara y concisa del problema.

## 🔄 Pasos para Reproducir
1. Ir a '...'
2. Ejecutar '...'
3. Ver error

## ✅ Comportamiento Esperado
Descripción de lo que debería pasar.

## 📱 Entorno
- OS: [e.g. Windows 10]
- Python: [e.g. 3.9.7]
- Notebook: [e.g. 05_pandas_fundamentos.ipynb]

## 📎 Información Adicional
Screenshots, logs, o contexto adicional.
```

### Feature Requests
```markdown
## 🚀 Descripción de la Funcionalidad
Descripción clara de la nueva funcionalidad.

## 🎯 Motivación
¿Por qué sería útil esta funcionalidad?

## 💡 Solución Propuesta
Descripción de cómo debería funcionar.

## 🔄 Alternativas Consideradas
Otras soluciones que consideraste.
```

## 📞 Contacto y Soporte

- **GitHub Issues**: Para bugs y feature requests ([Crear Issue](https://github.com/lraigosov/data-engineer-course/issues))
- **GitHub Discussions**: Para preguntas generales ([Ir a Discussions](https://github.com/lraigosov/data-engineer-course/discussions))
- **Email**: A través de GitHub Issues
- **Mantenedor**: Luis J. Raigoso V. ([@lraigosov](https://github.com/lraigosov))

## 🏆 Reconocimiento

Los contribuidores serán reconocidos en:
- **README.md**: Sección de contribuidores
- **CHANGELOG.md**: Créditos por versión
- **Hall of Fame**: Contribuidores destacados

## 👤 Autor y Mantenedor

**Luis J. Raigoso V. (LJRV)**
- GitHub: [@lraigosov](https://github.com/lraigosov)
- LinkedIn: [lraigosov](https://www.linkedin.com/in/lraigosov/)

---

¡Gracias por ayudar a hacer este curso mejor para toda la comunidad! 🙌

© 2024-2025 LJRV - Luis J. Raigoso V.