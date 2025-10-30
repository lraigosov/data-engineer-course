"""
Tests de Integración para Pipelines ETL
========================================

Suite de tests para validar el funcionamiento completo de los pipelines.

Para ejecutar:
    pytest test_pipelines.py
    pytest test_pipelines.py -v
    pytest test_pipelines.py --cov
"""

import pytest
import pandas as pd
import numpy as np
import sqlite3
import os
import sys
from pathlib import Path
from datetime import datetime
import tempfile
import shutil

# Agregar rutas al path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../scripts/pipelines')))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../scripts/etl')))


class TestDataIngestionPipeline:
    """Tests de integración para pipeline de ingestión"""
    
    @pytest.fixture
    def temp_dir(self):
        """Fixture que crea un directorio temporal"""
        temp_path = tempfile.mkdtemp()
        yield temp_path
        shutil.rmtree(temp_path)
    
    @pytest.fixture
    def sample_csv_file(self, temp_dir):
        """Fixture que crea un archivo CSV de prueba"""
        csv_path = os.path.join(temp_dir, 'test_data.csv')
        df = pd.DataFrame({
            'id': [1, 2, 3, 4, 5],
            'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
            'value': [100, 200, 150, 300, 250],
            'date': ['2024-01-01', '2024-01-02', '2024-01-03', '2024-01-04', '2024-01-05']
        })
        df.to_csv(csv_path, index=False)
        return csv_path
    
    @pytest.fixture
    def sample_json_file(self, temp_dir):
        """Fixture que crea un archivo JSON de prueba"""
        json_path = os.path.join(temp_dir, 'test_data.json')
        df = pd.DataFrame({
            'user_id': [101, 102, 103],
            'action': ['login', 'purchase', 'logout'],
            'timestamp': ['2024-01-01T10:00:00', '2024-01-01T10:05:00', '2024-01-01T10:10:00']
        })
        df.to_json(json_path, orient='records')
        return json_path
    
    @pytest.fixture
    def sample_database(self, temp_dir):
        """Fixture que crea una base de datos SQLite de prueba"""
        db_path = os.path.join(temp_dir, 'test.db')
        conn = sqlite3.connect(db_path)
        
        # Crear tabla y datos de prueba
        conn.execute('''
            CREATE TABLE sales (
                id INTEGER PRIMARY KEY,
                product TEXT,
                quantity INTEGER,
                price REAL
            )
        ''')
        
        sales_data = [
            (1, 'Product A', 5, 10.99),
            (2, 'Product B', 3, 25.50),
            (3, 'Product C', 7, 15.75)
        ]
        
        conn.executemany('INSERT INTO sales VALUES (?, ?, ?, ?)', sales_data)
        conn.commit()
        conn.close()
        
        return db_path
    
    def test_read_csv_file(self, sample_csv_file):
        """Test de lectura de archivo CSV"""
        df = pd.read_csv(sample_csv_file)
        
        assert not df.empty
        assert len(df) == 5
        assert 'id' in df.columns
        assert 'name' in df.columns
        assert 'value' in df.columns
    
    def test_read_json_file(self, sample_json_file):
        """Test de lectura de archivo JSON"""
        df = pd.read_json(sample_json_file)
        
        assert not df.empty
        assert len(df) == 3
        assert 'user_id' in df.columns
        assert 'action' in df.columns
    
    def test_read_database(self, sample_database):
        """Test de lectura desde base de datos"""
        conn = sqlite3.connect(sample_database)
        df = pd.read_sql_query("SELECT * FROM sales", conn)
        conn.close()
        
        assert not df.empty
        assert len(df) == 3
        assert 'product' in df.columns
        assert 'quantity' in df.columns
        assert 'price' in df.columns
    
    def test_data_validation(self, sample_csv_file):
        """Test de validación de datos"""
        df = pd.read_csv(sample_csv_file)
        
        # Validar que no hay valores nulos
        assert not df['id'].isnull().any()
        assert not df['name'].isnull().any()
        
        # Validar tipos de datos
        assert df['id'].dtype in ['int64', 'int32']
        assert df['name'].dtype == 'object'
        assert df['value'].dtype in ['int64', 'int32']
    
    def test_data_transformation(self, sample_csv_file):
        """Test de transformación de datos"""
        df = pd.read_csv(sample_csv_file)
        
        # Transformación: agregar columna calculada
        df['value_doubled'] = df['value'] * 2
        
        # Transformación: convertir fecha
        df['date'] = pd.to_datetime(df['date'])
        
        # Validar transformaciones
        assert 'value_doubled' in df.columns
        assert df['value_doubled'].iloc[0] == 200
        assert df['date'].dtype == 'datetime64[ns]'
    
    def test_remove_duplicates(self):
        """Test de eliminación de duplicados"""
        df = pd.DataFrame({
            'id': [1, 2, 2, 3, 3, 4],
            'value': [10, 20, 20, 30, 30, 40]
        })
        
        df_unique = df.drop_duplicates()
        
        assert len(df_unique) == 4
        assert not df_unique.duplicated().any()
    
    def test_handle_missing_values(self):
        """Test de manejo de valores faltantes"""
        df = pd.DataFrame({
            'id': [1, 2, 3, 4, 5],
            'value': [10, 20, None, 40, 50],
            'category': ['A', 'B', None, 'D', 'E']
        })
        
        # Imputar valores numéricos con media
        df['value'].fillna(df['value'].mean(), inplace=True)
        
        # Imputar valores categóricos con 'Unknown'
        df['category'].fillna('Unknown', inplace=True)
        
        # Validar
        assert not df['value'].isnull().any()
        assert not df['category'].isnull().any()
        assert df['category'].iloc[2] == 'Unknown'
    
    def test_write_to_csv(self, temp_dir):
        """Test de escritura a CSV"""
        df = pd.DataFrame({
            'col1': [1, 2, 3],
            'col2': ['A', 'B', 'C']
        })
        
        output_path = os.path.join(temp_dir, 'output.csv')
        df.to_csv(output_path, index=False)
        
        # Verificar que el archivo existe
        assert os.path.exists(output_path)
        
        # Leer y verificar contenido
        df_read = pd.read_csv(output_path)
        assert len(df_read) == 3
        pd.testing.assert_frame_equal(df, df_read)
    
    def test_write_to_json(self, temp_dir):
        """Test de escritura a JSON"""
        df = pd.DataFrame({
            'id': [1, 2, 3],
            'name': ['X', 'Y', 'Z']
        })
        
        output_path = os.path.join(temp_dir, 'output.json')
        df.to_json(output_path, orient='records')
        
        # Verificar que el archivo existe
        assert os.path.exists(output_path)
        
        # Leer y verificar contenido
        df_read = pd.read_json(output_path)
        assert len(df_read) == 3
    
    def test_write_to_database(self, temp_dir):
        """Test de escritura a base de datos"""
        df = pd.DataFrame({
            'id': [1, 2, 3],
            'product': ['A', 'B', 'C'],
            'price': [10.0, 20.0, 30.0]
        })
        
        db_path = os.path.join(temp_dir, 'output.db')
        conn = sqlite3.connect(db_path)
        
        df.to_sql('products', conn, if_exists='replace', index=False)
        
        # Verificar que los datos se guardaron
        df_read = pd.read_sql_query("SELECT * FROM products", conn)
        conn.close()
        
        assert len(df_read) == 3
        assert list(df_read.columns) == ['id', 'product', 'price']


class TestETLPipelineIntegration:
    """Tests de integración para pipeline ETL completo"""
    
    @pytest.fixture
    def etl_pipeline_data(self):
        """Fixture con datos de ejemplo para ETL"""
        return pd.DataFrame({
            'transaction_id': range(1, 101),
            'customer_id': np.random.randint(1, 20, 100),
            'product': np.random.choice(['A', 'B', 'C', 'D'], 100),
            'amount': np.random.uniform(10, 500, 100).round(2),
            'date': pd.date_range('2024-01-01', periods=100, freq='D')
        })
    
    def test_complete_etl_flow(self, etl_pipeline_data, tmp_path):
        """Test de flujo ETL completo: Extract -> Transform -> Load"""
        
        # 1. EXTRACT: Guardar datos originales
        input_file = tmp_path / "input.csv"
        etl_pipeline_data.to_csv(input_file, index=False)
        
        # Leer datos
        df_extracted = pd.read_csv(input_file)
        assert len(df_extracted) == 100
        
        # 2. TRANSFORM
        df_transformed = df_extracted.copy()
        
        # Agregar columna de mes
        df_transformed['date'] = pd.to_datetime(df_transformed['date'])
        df_transformed['month'] = df_transformed['date'].dt.month
        
        # Agregar columna de categoría de monto
        df_transformed['amount_category'] = pd.cut(
            df_transformed['amount'],
            bins=[0, 100, 300, 1000],
            labels=['Low', 'Medium', 'High']
        )
        
        # Validar transformaciones
        assert 'month' in df_transformed.columns
        assert 'amount_category' in df_transformed.columns
        
        # 3. LOAD: Guardar datos transformados
        output_file = tmp_path / "output.csv"
        df_transformed.to_csv(output_file, index=False)
        
        # Verificar resultado final
        df_loaded = pd.read_csv(output_file)
        assert len(df_loaded) == 100
        assert 'month' in df_loaded.columns
        assert 'amount_category' in df_loaded.columns
    
    def test_aggregation_pipeline(self, etl_pipeline_data):
        """Test de pipeline con agregaciones"""
        
        # Agregar mes
        etl_pipeline_data['month'] = pd.to_datetime(etl_pipeline_data['date']).dt.month
        
        # Agregaciones por producto y mes
        agg_result = etl_pipeline_data.groupby(['product', 'month']).agg({
            'amount': ['sum', 'mean', 'count'],
            'customer_id': 'nunique'
        })
        
        # Validar resultados
        assert not agg_result.empty
        assert agg_result.index.nlevels == 2  # MultiIndex con 2 niveles
    
    def test_data_quality_checks(self, etl_pipeline_data):
        """Test de validaciones de calidad de datos"""
        
        # Check 1: No hay valores nulos en columnas críticas
        critical_columns = ['transaction_id', 'customer_id', 'amount']
        for col in critical_columns:
            assert not etl_pipeline_data[col].isnull().any()
        
        # Check 2: Los IDs son únicos
        assert etl_pipeline_data['transaction_id'].is_unique
        
        # Check 3: Los montos son positivos
        assert (etl_pipeline_data['amount'] > 0).all()
        
        # Check 4: Las fechas están en rango válido
        min_date = pd.to_datetime('2024-01-01')
        max_date = pd.to_datetime('2024-12-31')
        dates = pd.to_datetime(etl_pipeline_data['date'])
        assert (dates >= min_date).all()
        assert (dates <= max_date).all()
    
    def test_error_handling_pipeline(self):
        """Test de manejo de errores en pipeline"""
        
        # Datos con problemas
        df_with_issues = pd.DataFrame({
            'id': [1, 2, None, 4, 5],
            'value': [10, -20, 30, 40, 50],  # Valor negativo
            'category': ['A', 'B', 'C', None, 'E']
        })
        
        # Identificar registros problemáticos
        null_ids = df_with_issues['id'].isnull()
        negative_values = df_with_issues['value'] < 0
        null_categories = df_with_issues['category'].isnull()
        
        # Contar problemas
        issues_count = null_ids.sum() + negative_values.sum() + null_categories.sum()
        
        assert issues_count == 3
        
        # Limpiar datos
        df_clean = df_with_issues.copy()
        df_clean = df_clean[df_clean['id'].notna()]
        df_clean = df_clean[df_clean['value'] >= 0]
        df_clean['category'].fillna('Unknown', inplace=True)
        
        # Validar limpieza
        assert not df_clean['id'].isnull().any()
        assert (df_clean['value'] >= 0).all()
        assert not df_clean['category'].isnull().any()


class TestPerformancePipeline:
    """Tests de rendimiento del pipeline"""
    
    def test_large_dataset_processing(self):
        """Test de procesamiento de dataset grande"""
        
        # Crear dataset grande (1M registros)
        n_records = 1_000_000
        df_large = pd.DataFrame({
            'id': range(n_records),
            'value': np.random.randint(1, 100, n_records),
            'category': np.random.choice(['A', 'B', 'C'], n_records)
        })
        
        # Medir tiempo de procesamiento
        start_time = datetime.now()
        
        # Operaciones típicas
        df_grouped = df_large.groupby('category')['value'].sum()
        df_filtered = df_large[df_large['value'] > 50]
        
        end_time = datetime.now()
        duration = (end_time - start_time).total_seconds()
        
        # Validar que el procesamiento fue exitoso y razonablemente rápido
        assert len(df_grouped) == 3
        assert not df_filtered.empty
        assert duration < 60  # Debe completarse en menos de 60 segundos
        
        print(f"\nProcesamiento de {n_records:,} registros: {duration:.2f} segundos")
    
    @pytest.mark.slow
    def test_batch_processing(self):
        """Test de procesamiento por lotes"""
        
        n_records = 100_000
        batch_size = 10_000
        
        df = pd.DataFrame({
            'id': range(n_records),
            'value': np.random.randint(1, 1000, n_records)
        })
        
        results = []
        
        # Procesar en lotes
        for i in range(0, len(df), batch_size):
            batch = df.iloc[i:i+batch_size]
            batch_sum = batch['value'].sum()
            results.append(batch_sum)
        
        # Validar que todos los lotes fueron procesados
        expected_batches = (n_records + batch_size - 1) // batch_size
        assert len(results) == expected_batches
        
        # Validar que la suma total coincide
        total_sum = sum(results)
        assert total_sum == df['value'].sum()


# Configuración de pytest
def pytest_configure(config):
    """Configuración personalizada de pytest"""
    config.addinivalue_line(
        "markers", "slow: marca test como lento (se puede omitir con -m 'not slow')"
    )


if __name__ == "__main__":
    pytest.main([__file__, '-v', '--tb=short'])
