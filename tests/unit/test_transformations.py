"""
Tests Unitarios para Funciones de Transformación
===============================================

Suite de tests para validar las funciones de transformación de datos.

Para ejecutar:
    pytest test_transformations.py
    pytest test_transformations.py -v
    pytest test_transformations.py --cov
"""

import pytest
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import sys
import os

# Agregar ruta al path para importar módulos
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../scripts/transformaciones')))

# Importar funciones a testear (descomentar cuando existan)
# from data_transformations import (
#     limpiar_columnas_texto,
#     validar_emails,
#     eliminar_outliers
# )


class TestLimpiezaDatos:
    """Tests para funciones de limpieza de datos"""
    
    @pytest.fixture
    def df_ejemplo(self):
        """Fixture con DataFrame de ejemplo"""
        return pd.DataFrame({
            'nombre': ['  Juan  ', 'MARÍA', 'pedro  ', 'ANA'],
            'edad': [25, 30, 35, 28],
            'email': ['juan@example.com', 'maria@test.com', 'invalido', 'ana@demo.co'],
            'salario': [50000, 60000, 200000, 55000]  # 200000 es outlier
        })
    
    def test_dataframe_no_vacio(self, df_ejemplo):
        """Test que el DataFrame de ejemplo no esté vacío"""
        assert not df_ejemplo.empty
        assert len(df_ejemplo) == 4
    
    def test_columnas_esperadas(self, df_ejemplo):
        """Test que el DataFrame tenga las columnas esperadas"""
        columnas_esperadas = ['nombre', 'edad', 'email', 'salario']
        assert list(df_ejemplo.columns) == columnas_esperadas
    
    def test_tipos_datos(self, df_ejemplo):
        """Test que los tipos de datos sean correctos"""
        assert df_ejemplo['nombre'].dtype == 'object'
        assert df_ejemplo['edad'].dtype in ['int64', 'int32']
        assert df_ejemplo['salario'].dtype in ['int64', 'int32']


class TestValidacionDatos:
    """Tests para funciones de validación"""
    
    def test_validacion_email_basica(self):
        """Test de validación básica de emails"""
        emails_validos = [
            'test@example.com',
            'user.name@domain.co',
            'admin@sub.domain.org'
        ]
        emails_invalidos = [
            'invalido',
            '@example.com',
            'test@',
            'test.com'
        ]
        
        # Patrón simple de email
        import re
        patron = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        
        for email in emails_validos:
            assert re.match(patron, email), f"{email} debería ser válido"
        
        for email in emails_invalidos:
            assert not re.match(patron, email), f"{email} debería ser inválido"
    
    def test_deteccion_outliers_iqr(self):
        """Test de detección de outliers usando IQR"""
        datos = [1, 2, 3, 4, 5, 6, 7, 8, 9, 100]  # 100 es outlier
        df = pd.DataFrame({'valor': datos})
        
        Q1 = df['valor'].quantile(0.25)
        Q3 = df['valor'].quantile(0.75)
        IQR = Q3 - Q1
        
        limite_inferior = Q1 - 1.5 * IQR
        limite_superior = Q3 + 1.5 * IQR
        
        outliers = df[(df['valor'] < limite_inferior) | (df['valor'] > limite_superior)]
        
        assert len(outliers) > 0
        assert 100 in outliers['valor'].values


class TestTransformacionFechas:
    """Tests para transformaciones de fechas"""
    
    @pytest.fixture
    def df_fechas(self):
        """Fixture con datos de fechas"""
        return pd.DataFrame({
            'fecha_str': ['2024-01-01', '2024-02-15', '2024-03-30'],
            'fecha_invalida': ['2024-01-01', 'invalida', '2024-03-30']
        })
    
    def test_conversion_fechas(self, df_fechas):
        """Test de conversión de strings a datetime"""
        df_fechas['fecha_dt'] = pd.to_datetime(df_fechas['fecha_str'])
        
        assert df_fechas['fecha_dt'].dtype == 'datetime64[ns]'
        assert not df_fechas['fecha_dt'].isnull().any()
    
    def test_manejo_fechas_invalidas(self, df_fechas):
        """Test de manejo de fechas inválidas"""
        df_fechas['fecha_dt'] = pd.to_datetime(df_fechas['fecha_invalida'], errors='coerce')
        
        # Debe haber exactamente 1 valor nulo (la fecha inválida)
        assert df_fechas['fecha_dt'].isnull().sum() == 1
    
    def test_extraccion_componentes_fecha(self):
        """Test de extracción de componentes de fecha"""
        df = pd.DataFrame({
            'fecha': pd.to_datetime(['2024-01-15', '2024-06-20', '2024-12-25'])
        })
        
        df['año'] = df['fecha'].dt.year
        df['mes'] = df['fecha'].dt.month
        df['dia'] = df['fecha'].dt.day
        
        assert all(df['año'] == 2024)
        assert list(df['mes']) == [1, 6, 12]
        assert list(df['dia']) == [15, 20, 25]


class TestAgregaciones:
    """Tests para funciones de agregación"""
    
    @pytest.fixture
    def df_ventas(self):
        """Fixture con datos de ventas"""
        return pd.DataFrame({
            'producto': ['A', 'B', 'A', 'B', 'A'],
            'cantidad': [10, 20, 15, 25, 30],
            'precio': [100, 200, 100, 200, 100]
        })
    
    def test_agregacion_sum(self, df_ventas):
        """Test de agregación por suma"""
        agg = df_ventas.groupby('producto')['cantidad'].sum()
        
        assert agg['A'] == 55  # 10 + 15 + 30
        assert agg['B'] == 45  # 20 + 25
    
    def test_agregacion_count(self, df_ventas):
        """Test de conteo por grupo"""
        count = df_ventas.groupby('producto').size()
        
        assert count['A'] == 3
        assert count['B'] == 2
    
    def test_agregacion_multiple(self, df_ventas):
        """Test de múltiples agregaciones"""
        agg = df_ventas.groupby('producto').agg({
            'cantidad': ['sum', 'mean'],
            'precio': 'mean'
        })
        
        assert agg.loc['A', ('cantidad', 'sum')] == 55
        assert agg.loc['A', ('cantidad', 'mean')] == pytest.approx(18.33, rel=0.01)


class TestImputacion:
    """Tests para imputación de valores faltantes"""
    
    def test_imputacion_media(self):
        """Test de imputación con media"""
        df = pd.DataFrame({
            'valor': [1, 2, np.nan, 4, 5]
        })
        
        media = df['valor'].mean()
        df['valor'].fillna(media, inplace=True)
        
        assert not df['valor'].isnull().any()
        assert df['valor'].iloc[2] == 3.0  # (1+2+4+5)/4 = 3
    
    def test_imputacion_forward_fill(self):
        """Test de imputación forward fill"""
        df = pd.DataFrame({
            'valor': [1, 2, np.nan, np.nan, 5]
        })
        
        df['valor'] = df['valor'].ffill()
        
        assert not df['valor'].isnull().any()
        assert df['valor'].iloc[2] == 2
        assert df['valor'].iloc[3] == 2


class TestCodificacion:
    """Tests para codificación de variables categóricas"""
    
    def test_one_hot_encoding(self):
        """Test de codificación one-hot"""
        df = pd.DataFrame({
            'categoria': ['A', 'B', 'C', 'A', 'B']
        })
        
        df_encoded = pd.get_dummies(df, columns=['categoria'])
        
        # Debe tener 3 columnas nuevas (una por categoría)
        assert 'categoria_A' in df_encoded.columns
        assert 'categoria_B' in df_encoded.columns
        assert 'categoria_C' in df_encoded.columns
        
        # La suma de cada fila debe ser 1
        assert all(df_encoded.sum(axis=1) == 1)
    
    def test_label_encoding(self):
        """Test de codificación por etiquetas"""
        df = pd.DataFrame({
            'categoria': ['bajo', 'medio', 'alto', 'bajo', 'alto']
        })
        
        df['categoria_encoded'] = pd.factorize(df['categoria'])[0]
        
        assert df['categoria_encoded'].dtype in ['int64', 'int32']
        assert df['categoria_encoded'].nunique() == 3


# Tests de integración
class TestPipelineCompleto:
    """Tests de integración para pipeline completo"""
    
    def test_pipeline_etl_basico(self):
        """Test de pipeline ETL básico"""
        # 1. Extract (simular)
        data_raw = {
            'id': [1, 2, 3, 3, 4],  # 3 está duplicado
            'nombre': ['  Juan  ', 'MARÍA', 'pedro', 'pedro', 'ANA'],
            'edad': [25, None, 35, 35, 28],
            'salario': [50000, 60000, 70000, 70000, 55000]
        }
        df = pd.DataFrame(data_raw)
        
        # 2. Transform
        # Limpiar duplicados
        df = df.drop_duplicates()
        
        # Limpiar nombres
        df['nombre'] = df['nombre'].str.strip().str.title()
        
        # Imputar edad faltante con la media
        df['edad'].fillna(df['edad'].mean(), inplace=True)
        
        # 3. Validate
        assert len(df) == 4  # Debe haber 4 registros después de eliminar duplicados
        assert not df['edad'].isnull().any()  # No debe haber valores nulos en edad
        assert all(df['nombre'].str.istitle())  # Todos los nombres deben estar en Title Case


# Configuración de pytest
def pytest_configure(config):
    """Configuración personalizada de pytest"""
    config.addinivalue_line(
        "markers", "slow: marca test como lento"
    )
    config.addinivalue_line(
        "markers", "integration: marca test como de integración"
    )


# Fixture global
@pytest.fixture(scope="session")
def config_test():
    """Configuración global para tests"""
    return {
        'test_data_dir': '../../datasets/raw/',
        'output_dir': '../../datasets/processed/',
        'log_level': 'INFO'
    }


if __name__ == "__main__":
    # Ejecutar tests si se ejecuta directamente
    pytest.main([__file__, '-v'])
