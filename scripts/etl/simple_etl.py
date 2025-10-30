"""
Script ETL Simple - Ejemplo de Extracción, Transformación y Carga
==================================================================

Este script demuestra un pipeline ETL básico que:
1. Extrae datos de una API pública
2. Transforma y limpia los datos
3. Carga los resultados en un archivo CSV

Autor: Curso de Ingeniería de Datos
Fecha: 2024
"""

import requests
import pandas as pd
import logging
from datetime import datetime
from typing import Dict, List, Optional
import os


# Configurar logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('etl_simple.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)


class SimpleETLPipeline:
    """
    Pipeline ETL simple para demostración
    """
    
    def __init__(self, api_url: str, output_dir: str = '../datasets/processed'):
        """
        Inicializa el pipeline ETL
        
        Args:
            api_url: URL de la API fuente
            output_dir: Directorio para guardar resultados
        """
        self.api_url = api_url
        self.output_dir = output_dir
        self.data_raw = None
        self.data_transformed = None
        
        # Crear directorio de salida si no existe
        os.makedirs(output_dir, exist_ok=True)
        
        logger.info(f"Pipeline inicializado - URL: {api_url}")
    
    def extract(self) -> bool:
        """
        Extrae datos desde la API
        
        Returns:
            bool: True si la extracción fue exitosa
        """
        try:
            logger.info(f"🔽 Iniciando extracción desde {self.api_url}")
            
            response = requests.get(self.api_url, timeout=30)
            response.raise_for_status()
            
            self.data_raw = response.json()
            
            logger.info(f"✅ Extracción exitosa: {len(self.data_raw)} registros")
            return True
            
        except requests.exceptions.RequestException as e:
            logger.error(f"❌ Error en extracción: {e}")
            return False
        except Exception as e:
            logger.error(f"❌ Error inesperado en extracción: {e}")
            return False
    
    def transform(self) -> bool:
        """
        Transforma y limpia los datos extraídos
        
        Returns:
            bool: True si la transformación fue exitosa
        """
        if not self.data_raw:
            logger.error("❌ No hay datos para transformar")
            return False
        
        try:
            logger.info("⚙️ Iniciando transformación de datos")
            
            # Convertir a DataFrame
            df = pd.DataFrame(self.data_raw)
            
            # Limpiar y transformar
            df_transformed = self._clean_data(df)
            df_transformed = self._enrich_data(df_transformed)
            
            self.data_transformed = df_transformed
            
            logger.info(f"✅ Transformación exitosa: {len(df_transformed)} registros procesados")
            return True
            
        except Exception as e:
            logger.error(f"❌ Error en transformación: {e}")
            return False
    
    def _clean_data(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Limpia los datos
        
        Args:
            df: DataFrame a limpiar
            
        Returns:
            DataFrame limpio
        """
        logger.info("   🧹 Limpiando datos...")
        
        # Remover duplicados
        initial_count = len(df)
        df = df.drop_duplicates()
        duplicates_removed = initial_count - len(df)
        
        if duplicates_removed > 0:
            logger.info(f"   • Duplicados removidos: {duplicates_removed}")
        
        # Manejar valores nulos
        nulls_before = df.isnull().sum().sum()
        df = df.dropna()  # Estrategia simple: eliminar filas con nulls
        nulls_removed = nulls_before - df.isnull().sum().sum()
        
        if nulls_removed > 0:
            logger.info(f"   • Valores nulos procesados: {nulls_removed}")
        
        return df
    
    def _enrich_data(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Enriquece los datos con información adicional
        
        Args:
            df: DataFrame a enriquecer
            
        Returns:
            DataFrame enriquecido
        """
        logger.info("   ✨ Enriqueciendo datos...")
        
        # Agregar timestamp de procesamiento
        df['processed_at'] = datetime.now().isoformat()
        
        # Agregar ID de procesamiento
        df['process_id'] = datetime.now().strftime('%Y%m%d_%H%M%S')
        
        return df
    
    def load(self, filename: str = None) -> bool:
        """
        Carga los datos transformados en un archivo CSV
        
        Args:
            filename: Nombre del archivo de salida (opcional)
            
        Returns:
            bool: True si la carga fue exitosa
        """
        if self.data_transformed is None or self.data_transformed.empty:
            logger.error("❌ No hay datos transformados para cargar")
            return False
        
        try:
            if filename is None:
                timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
                filename = f'etl_output_{timestamp}.csv'
            
            filepath = os.path.join(self.output_dir, filename)
            
            logger.info(f"📤 Cargando datos en {filepath}")
            
            self.data_transformed.to_csv(filepath, index=False, encoding='utf-8')
            
            # Verificar que el archivo se creó correctamente
            if os.path.exists(filepath):
                file_size = os.path.getsize(filepath)
                logger.info(f"✅ Carga exitosa: {filename} ({file_size:,} bytes)")
                return True
            else:
                logger.error("❌ El archivo no se creó correctamente")
                return False
                
        except Exception as e:
            logger.error(f"❌ Error en carga: {e}")
            return False
    
    def run(self, output_filename: str = None) -> Dict[str, any]:
        """
        Ejecuta el pipeline completo ETL
        
        Args:
            output_filename: Nombre del archivo de salida (opcional)
            
        Returns:
            dict: Estadísticas de la ejecución
        """
        logger.info("🚀 Iniciando pipeline ETL completo")
        start_time = datetime.now()
        
        stats = {
            'start_time': start_time.isoformat(),
            'end_time': None,
            'duration_seconds': None,
            'extract_success': False,
            'transform_success': False,
            'load_success': False,
            'records_processed': 0,
            'status': 'failed'
        }
        
        try:
            # Extract
            if not self.extract():
                raise Exception("Fallo en extracción")
            stats['extract_success'] = True
            
            # Transform
            if not self.transform():
                raise Exception("Fallo en transformación")
            stats['transform_success'] = True
            stats['records_processed'] = len(self.data_transformed)
            
            # Load
            if not self.load(output_filename):
                raise Exception("Fallo en carga")
            stats['load_success'] = True
            
            stats['status'] = 'success'
            logger.info("✅ Pipeline completado exitosamente")
            
        except Exception as e:
            logger.error(f"❌ Pipeline falló: {e}")
            stats['status'] = 'failed'
            stats['error'] = str(e)
        
        finally:
            end_time = datetime.now()
            stats['end_time'] = end_time.isoformat()
            stats['duration_seconds'] = (end_time - start_time).total_seconds()
            
            logger.info(f"⏱️ Duración total: {stats['duration_seconds']:.2f} segundos")
        
        return stats


def main():
    """
    Función principal para ejecutar el pipeline
    """
    print("="*60)
    print("🔄 SIMPLE ETL PIPELINE")
    print("="*60)
    
    # Configurar pipeline
    api_url = "https://jsonplaceholder.typicode.com/users"
    pipeline = SimpleETLPipeline(api_url)
    
    # Ejecutar pipeline
    stats = pipeline.run(output_filename='usuarios_procesados.csv')
    
    # Mostrar resumen
    print("\n" + "="*60)
    print("📊 RESUMEN DE EJECUCIÓN")
    print("="*60)
    print(f"Estado: {stats['status'].upper()}")
    print(f"Registros procesados: {stats['records_processed']}")
    print(f"Duración: {stats['duration_seconds']:.2f} segundos")
    print(f"Extracción: {'✅' if stats['extract_success'] else '❌'}")
    print(f"Transformación: {'✅' if stats['transform_success'] else '❌'}")
    print(f"Carga: {'✅' if stats['load_success'] else '❌'}")
    print("="*60)
    
    return stats


if __name__ == "__main__":
    main()
