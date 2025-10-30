"""
Script de Pipeline de Ingestión de Datos
========================================

Pipeline completo para ingerir datos desde múltiples fuentes:
- APIs REST
- Archivos CSV/JSON
- Bases de datos

El pipeline incluye:
1. Extracción desde múltiples fuentes
2. Validación de datos
3. Transformación básica
4. Carga a destino
5. Logging y monitoreo
"""

import pandas as pd
import json
import logging
import requests
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Any, Optional
import sqlite3


# Configuración de logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class DataIngestionPipeline:
    """Pipeline de ingestión de datos desde múltiples fuentes"""
    
    def __init__(self, config: Dict[str, Any]):
        """
        Inicializar pipeline con configuración
        
        Args:
            config: Diccionario con configuración del pipeline
        """
        self.config = config
        self.data_sources = config.get('data_sources', {})
        self.output_path = Path(config.get('output_path', './data/processed'))
        self.output_path.mkdir(parents=True, exist_ok=True)
        
        logger.info(f"Pipeline inicializado. Output: {self.output_path}")
    
    def extract_from_api(self, api_config: Dict[str, Any]) -> Optional[pd.DataFrame]:
        """
        Extraer datos desde una API REST
        
        Args:
            api_config: Configuración de la API (url, headers, params)
            
        Returns:
            DataFrame con los datos o None si hay error
        """
        try:
            url = api_config['url']
            headers = api_config.get('headers', {})
            params = api_config.get('params', {})
            
            logger.info(f"Extrayendo datos de API: {url}")
            response = requests.get(url, headers=headers, params=params, timeout=30)
            response.raise_for_status()
            
            data = response.json()
            df = pd.DataFrame(data)
            
            logger.info(f"Extraídos {len(df)} registros de API")
            return df
            
        except requests.exceptions.RequestException as e:
            logger.error(f"Error al extraer de API: {str(e)}")
            return None
        except Exception as e:
            logger.error(f"Error inesperado: {str(e)}")
            return None
    
    def extract_from_csv(self, file_path: str) -> Optional[pd.DataFrame]:
        """
        Extraer datos desde archivo CSV
        
        Args:
            file_path: Ruta al archivo CSV
            
        Returns:
            DataFrame con los datos o None si hay error
        """
        try:
            logger.info(f"Leyendo CSV: {file_path}")
            df = pd.read_csv(file_path)
            logger.info(f"Leídos {len(df)} registros de CSV")
            return df
            
        except FileNotFoundError:
            logger.error(f"Archivo no encontrado: {file_path}")
            return None
        except Exception as e:
            logger.error(f"Error al leer CSV: {str(e)}")
            return None
    
    def extract_from_json(self, file_path: str) -> Optional[pd.DataFrame]:
        """
        Extraer datos desde archivo JSON
        
        Args:
            file_path: Ruta al archivo JSON
            
        Returns:
            DataFrame con los datos o None si hay error
        """
        try:
            logger.info(f"Leyendo JSON: {file_path}")
            df = pd.read_json(file_path)
            logger.info(f"Leídos {len(df)} registros de JSON")
            return df
            
        except FileNotFoundError:
            logger.error(f"Archivo no encontrado: {file_path}")
            return None
        except Exception as e:
            logger.error(f"Error al leer JSON: {str(e)}")
            return None
    
    def extract_from_database(self, db_config: Dict[str, Any]) -> Optional[pd.DataFrame]:
        """
        Extraer datos desde base de datos SQL
        
        Args:
            db_config: Configuración de la base de datos
            
        Returns:
            DataFrame con los datos o None si hay error
        """
        try:
            db_path = db_config['path']
            query = db_config['query']
            
            logger.info(f"Conectando a base de datos: {db_path}")
            conn = sqlite3.connect(db_path)
            
            df = pd.read_sql_query(query, conn)
            conn.close()
            
            logger.info(f"Extraídos {len(df)} registros de base de datos")
            return df
            
        except Exception as e:
            logger.error(f"Error al extraer de base de datos: {str(e)}")
            return None
    
    def validate_data(self, df: pd.DataFrame, rules: Dict[str, Any]) -> bool:
        """
        Validar datos según reglas definidas
        
        Args:
            df: DataFrame a validar
            rules: Reglas de validación
            
        Returns:
            True si pasa validación, False si no
        """
        try:
            logger.info("Iniciando validación de datos")
            
            # Validar columnas requeridas
            required_columns = rules.get('required_columns', [])
            missing_cols = set(required_columns) - set(df.columns)
            if missing_cols:
                logger.error(f"Columnas faltantes: {missing_cols}")
                return False
            
            # Validar valores nulos
            if rules.get('no_nulls', False):
                null_counts = df.isnull().sum()
                if null_counts.any():
                    logger.warning(f"Valores nulos encontrados:\n{null_counts[null_counts > 0]}")
            
            # Validar tipos de datos
            expected_types = rules.get('expected_types', {})
            for col, expected_type in expected_types.items():
                if col in df.columns:
                    if not df[col].dtype == expected_type:
                        logger.warning(f"Tipo incorrecto en {col}: {df[col].dtype} != {expected_type}")
            
            # Validar rangos numéricos
            numeric_ranges = rules.get('numeric_ranges', {})
            for col, (min_val, max_val) in numeric_ranges.items():
                if col in df.columns:
                    out_of_range = df[(df[col] < min_val) | (df[col] > max_val)]
                    if not out_of_range.empty:
                        logger.warning(f"Valores fuera de rango en {col}: {len(out_of_range)} registros")
            
            logger.info("Validación completada")
            return True
            
        except Exception as e:
            logger.error(f"Error en validación: {str(e)}")
            return False
    
    def transform_data(self, df: pd.DataFrame, transformations: Dict[str, Any]) -> pd.DataFrame:
        """
        Aplicar transformaciones a los datos
        
        Args:
            df: DataFrame original
            transformations: Transformaciones a aplicar
            
        Returns:
            DataFrame transformado
        """
        try:
            logger.info("Aplicando transformaciones")
            df_transformed = df.copy()
            
            # Eliminar duplicados
            if transformations.get('remove_duplicates', False):
                before = len(df_transformed)
                df_transformed = df_transformed.drop_duplicates()
                logger.info(f"Duplicados eliminados: {before - len(df_transformed)}")
            
            # Rellenar valores nulos
            fill_nulls = transformations.get('fill_nulls', {})
            for col, value in fill_nulls.items():
                if col in df_transformed.columns:
                    df_transformed[col].fillna(value, inplace=True)
            
            # Renombrar columnas
            rename_cols = transformations.get('rename_columns', {})
            if rename_cols:
                df_transformed.rename(columns=rename_cols, inplace=True)
            
            # Convertir tipos de datos
            convert_types = transformations.get('convert_types', {})
            for col, dtype in convert_types.items():
                if col in df_transformed.columns:
                    df_transformed[col] = df_transformed[col].astype(dtype)
            
            # Agregar columna de timestamp
            if transformations.get('add_timestamp', False):
                df_transformed['ingestion_timestamp'] = datetime.now()
            
            logger.info("Transformaciones aplicadas")
            return df_transformed
            
        except Exception as e:
            logger.error(f"Error en transformación: {str(e)}")
            return df
    
    def load_to_csv(self, df: pd.DataFrame, filename: str) -> bool:
        """
        Cargar datos a archivo CSV
        
        Args:
            df: DataFrame a guardar
            filename: Nombre del archivo
            
        Returns:
            True si éxito, False si error
        """
        try:
            output_file = self.output_path / filename
            logger.info(f"Guardando datos en CSV: {output_file}")
            df.to_csv(output_file, index=False)
            logger.info(f"Guardados {len(df)} registros en {output_file}")
            return True
            
        except Exception as e:
            logger.error(f"Error al guardar CSV: {str(e)}")
            return False
    
    def load_to_json(self, df: pd.DataFrame, filename: str) -> bool:
        """
        Cargar datos a archivo JSON
        
        Args:
            df: DataFrame a guardar
            filename: Nombre del archivo
            
        Returns:
            True si éxito, False si error
        """
        try:
            output_file = self.output_path / filename
            logger.info(f"Guardando datos en JSON: {output_file}")
            df.to_json(output_file, orient='records', indent=2, date_format='iso')
            logger.info(f"Guardados {len(df)} registros en {output_file}")
            return True
            
        except Exception as e:
            logger.error(f"Error al guardar JSON: {str(e)}")
            return False
    
    def load_to_database(self, df: pd.DataFrame, db_config: Dict[str, Any]) -> bool:
        """
        Cargar datos a base de datos
        
        Args:
            df: DataFrame a guardar
            db_config: Configuración de la base de datos
            
        Returns:
            True si éxito, False si error
        """
        try:
            db_path = db_config['path']
            table_name = db_config['table']
            if_exists = db_config.get('if_exists', 'append')
            
            logger.info(f"Cargando datos a base de datos: {db_path}")
            conn = sqlite3.connect(db_path)
            
            df.to_sql(table_name, conn, if_exists=if_exists, index=False)
            conn.close()
            
            logger.info(f"Cargados {len(df)} registros en tabla {table_name}")
            return True
            
        except Exception as e:
            logger.error(f"Error al cargar a base de datos: {str(e)}")
            return False
    
    def run(self) -> Dict[str, Any]:
        """
        Ejecutar pipeline completo
        
        Returns:
            Diccionario con resultados de la ejecución
        """
        results = {
            'start_time': datetime.now(),
            'sources_processed': 0,
            'total_records': 0,
            'errors': []
        }
        
        logger.info("=" * 50)
        logger.info("Iniciando pipeline de ingestión de datos")
        logger.info("=" * 50)
        
        try:
            for source_name, source_config in self.data_sources.items():
                logger.info(f"\nProcesando fuente: {source_name}")
                
                # Extracción
                df = None
                source_type = source_config.get('type')
                
                if source_type == 'api':
                    df = self.extract_from_api(source_config)
                elif source_type == 'csv':
                    df = self.extract_from_csv(source_config['path'])
                elif source_type == 'json':
                    df = self.extract_from_json(source_config['path'])
                elif source_type == 'database':
                    df = self.extract_from_database(source_config)
                else:
                    logger.error(f"Tipo de fuente no soportado: {source_type}")
                    continue
                
                if df is None:
                    results['errors'].append(f"Error al extraer de {source_name}")
                    continue
                
                # Validación
                validation_rules = source_config.get('validation', {})
                if validation_rules and not self.validate_data(df, validation_rules):
                    results['errors'].append(f"Validación fallida para {source_name}")
                    continue
                
                # Transformación
                transformations = source_config.get('transformations', {})
                if transformations:
                    df = self.transform_data(df, transformations)
                
                # Carga
                output_config = source_config.get('output', {})
                output_type = output_config.get('type', 'csv')
                
                if output_type == 'csv':
                    filename = output_config.get('filename', f'{source_name}.csv')
                    self.load_to_csv(df, filename)
                elif output_type == 'json':
                    filename = output_config.get('filename', f'{source_name}.json')
                    self.load_to_json(df, filename)
                elif output_type == 'database':
                    self.load_to_database(df, output_config)
                
                results['sources_processed'] += 1
                results['total_records'] += len(df)
            
            results['end_time'] = datetime.now()
            results['duration'] = (results['end_time'] - results['start_time']).total_seconds()
            results['status'] = 'success' if not results['errors'] else 'completed_with_errors'
            
            logger.info("\n" + "=" * 50)
            logger.info("Pipeline completado")
            logger.info(f"Fuentes procesadas: {results['sources_processed']}")
            logger.info(f"Total de registros: {results['total_records']}")
            logger.info(f"Duración: {results['duration']:.2f} segundos")
            logger.info(f"Errores: {len(results['errors'])}")
            logger.info("=" * 50)
            
            return results
            
        except Exception as e:
            logger.error(f"Error crítico en pipeline: {str(e)}")
            results['status'] = 'failed'
            results['errors'].append(str(e))
            return results


def main():
    """Función principal de ejemplo"""
    
    # Configuración de ejemplo
    config = {
        'output_path': '../../datasets/processed',
        'data_sources': {
            'productos': {
                'type': 'csv',
                'path': '../../datasets/raw/productos.csv',
                'validation': {
                    'required_columns': ['producto', 'precio', 'stock'],
                    'no_nulls': False
                },
                'transformations': {
                    'remove_duplicates': True,
                    'add_timestamp': True
                },
                'output': {
                    'type': 'csv',
                    'filename': 'productos_processed.csv'
                }
            },
            'clientes': {
                'type': 'csv',
                'path': '../../datasets/raw/clientes.csv',
                'validation': {
                    'required_columns': ['cliente_id', 'nombre', 'email']
                },
                'transformations': {
                    'remove_duplicates': True,
                    'fill_nulls': {'ciudad': 'Desconocida'},
                    'add_timestamp': True
                },
                'output': {
                    'type': 'json',
                    'filename': 'clientes_processed.json'
                }
            }
        }
    }
    
    # Ejecutar pipeline
    pipeline = DataIngestionPipeline(config)
    results = pipeline.run()
    
    # Mostrar resultados
    print("\n" + "=" * 50)
    print("RESUMEN DE EJECUCIÓN")
    print("=" * 50)
    print(f"Estado: {results['status']}")
    print(f"Fuentes procesadas: {results['sources_processed']}")
    print(f"Total de registros: {results['total_records']}")
    print(f"Duración: {results.get('duration', 0):.2f} segundos")
    
    if results['errors']:
        print(f"\nErrores encontrados:")
        for error in results['errors']:
            print(f"  - {error}")


if __name__ == "__main__":
    main()
