"""
Script de Procesamiento por Lotes (Batch Processing)
====================================================

Pipeline para procesamiento por lotes de grandes volúmenes de datos:
- Lectura eficiente de datos en chunks
- Procesamiento paralelo con multiprocessing
- Agregaciones y transformaciones complejas
- Monitoreo de progreso y rendimiento
"""

import pandas as pd
import numpy as np
import logging
from datetime import datetime
from pathlib import Path
from typing import List, Dict, Any, Callable
import multiprocessing as mp
from functools import partial
import time


logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class BatchProcessor:
    """Procesador de datos por lotes con soporte para procesamiento paralelo"""
    
    def __init__(self, chunk_size: int = 10000, n_workers: int = None):
        """
        Inicializar procesador
        
        Args:
            chunk_size: Tamaño de cada lote
            n_workers: Número de trabajadores paralelos (None = auto)
        """
        self.chunk_size = chunk_size
        self.n_workers = n_workers or mp.cpu_count() - 1
        logger.info(f"Procesador inicializado: chunk_size={chunk_size}, workers={self.n_workers}")
    
    def process_chunk(self, chunk: pd.DataFrame, transform_func: Callable) -> pd.DataFrame:
        """
        Procesar un chunk de datos
        
        Args:
            chunk: DataFrame con el lote de datos
            transform_func: Función de transformación
            
        Returns:
            DataFrame transformado
        """
        try:
            return transform_func(chunk)
        except Exception as e:
            logger.error(f"Error procesando chunk: {str(e)}")
            return pd.DataFrame()
    
    def process_file_sequential(
        self,
        input_path: str,
        output_path: str,
        transform_func: Callable
    ) -> Dict[str, Any]:
        """
        Procesar archivo secuencialmente por chunks
        
        Args:
            input_path: Ruta del archivo de entrada
            output_path: Ruta del archivo de salida
            transform_func: Función de transformación
            
        Returns:
            Diccionario con estadísticas del procesamiento
        """
        logger.info(f"Iniciando procesamiento secuencial: {input_path}")
        start_time = time.time()
        
        stats = {
            'chunks_processed': 0,
            'total_rows': 0,
            'errors': 0
        }
        
        first_chunk = True
        
        for chunk_df in pd.read_csv(input_path, chunksize=self.chunk_size):
            try:
                # Procesar chunk
                transformed_chunk = transform_func(chunk_df)
                
                # Guardar resultado
                mode = 'w' if first_chunk else 'a'
                header = first_chunk
                transformed_chunk.to_csv(output_path, mode=mode, header=header, index=False)
                
                stats['chunks_processed'] += 1
                stats['total_rows'] += len(transformed_chunk)
                first_chunk = False
                
                logger.info(f"Chunk {stats['chunks_processed']} procesado: {len(transformed_chunk)} filas")
                
            except Exception as e:
                logger.error(f"Error en chunk {stats['chunks_processed']}: {str(e)}")
                stats['errors'] += 1
        
        stats['duration'] = time.time() - start_time
        logger.info(f"Procesamiento completado en {stats['duration']:.2f} segundos")
        
        return stats
    
    def process_file_parallel(
        self,
        input_path: str,
        output_path: str,
        transform_func: Callable
    ) -> Dict[str, Any]:
        """
        Procesar archivo en paralelo
        
        Args:
            input_path: Ruta del archivo de entrada
            output_path: Ruta del archivo de salida
            transform_func: Función de transformación
            
        Returns:
            Diccionario con estadísticas del procesamiento
        """
        logger.info(f"Iniciando procesamiento paralelo con {self.n_workers} workers")
        start_time = time.time()
        
        # Leer chunks
        chunks = list(pd.read_csv(input_path, chunksize=self.chunk_size))
        logger.info(f"Archivo dividido en {len(chunks)} chunks")
        
        # Procesar en paralelo
        with mp.Pool(processes=self.n_workers) as pool:
            process_func = partial(self.process_chunk, transform_func=transform_func)
            results = pool.map(process_func, chunks)
        
        # Combinar resultados
        df_final = pd.concat([r for r in results if not r.empty], ignore_index=True)
        
        # Guardar resultado
        df_final.to_csv(output_path, index=False)
        
        stats = {
            'chunks_processed': len(chunks),
            'total_rows': len(df_final),
            'duration': time.time() - start_time
        }
        
        logger.info(f"Procesamiento completado en {stats['duration']:.2f} segundos")
        
        return stats
    
    def aggregate_by_key(
        self,
        input_path: str,
        output_path: str,
        group_by: List[str],
        agg_dict: Dict[str, Any]
    ) -> Dict[str, Any]:
        """
        Realizar agregaciones por lotes
        
        Args:
            input_path: Ruta del archivo de entrada
            output_path: Ruta del archivo de salida
            group_by: Columnas para agrupar
            agg_dict: Diccionario de agregaciones
            
        Returns:
            Diccionario con estadísticas
        """
        logger.info(f"Iniciando agregación por: {group_by}")
        start_time = time.time()
        
        aggregated_chunks = []
        
        for chunk_df in pd.read_csv(input_path, chunksize=self.chunk_size):
            # Agregar chunk
            agg_chunk = chunk_df.groupby(group_by).agg(agg_dict)
            aggregated_chunks.append(agg_chunk)
        
        # Combinar y agregar de nuevo
        df_combined = pd.concat(aggregated_chunks)
        df_final = df_combined.groupby(level=group_by).sum()
        
        # Guardar resultado
        df_final.to_csv(output_path)
        
        stats = {
            'groups': len(df_final),
            'duration': time.time() - start_time
        }
        
        logger.info(f"Agregación completada: {stats['groups']} grupos en {stats['duration']:.2f} segundos")
        
        return stats


# Funciones de transformación de ejemplo
def clean_sales_data(df: pd.DataFrame) -> pd.DataFrame:
    """Limpiar datos de ventas"""
    df = df.copy()
    
    # Eliminar duplicados
    df = df.drop_duplicates()
    
    # Eliminar valores nulos
    df = df.dropna(subset=['cantidad', 'precio_unitario'])
    
    # Calcular total
    df['total'] = df['cantidad'] * df['precio_unitario']
    
    # Agregar timestamp de procesamiento
    df['processed_at'] = datetime.now()
    
    return df


def enrich_customer_data(df: pd.DataFrame) -> pd.DataFrame:
    """Enriquecer datos de clientes"""
    df = df.copy()
    
    # Categorizar por edad
    df['age_group'] = pd.cut(
        df['edad'],
        bins=[0, 25, 35, 50, 100],
        labels=['18-25', '26-35', '36-50', '51+']
    )
    
    # Categorizar por segmento de valor
    if 'total_gastado' in df.columns:
        df['value_segment'] = pd.cut(
            df['total_gastado'],
            bins=[0, 1000, 5000, float('inf')],
            labels=['Low', 'Medium', 'High']
        )
    
    return df


def main():
    """Función principal de ejemplo"""
    
    logger.info("=" * 60)
    logger.info("INICIO DE PROCESAMIENTO POR LOTES")
    logger.info("=" * 60)
    
    # Configuración
    processor = BatchProcessor(chunk_size=1000, n_workers=4)
    
    # Ejemplo 1: Procesamiento secuencial
    logger.info("\n--- Ejemplo 1: Procesamiento Secuencial ---")
    
    input_file = "../../datasets/raw/ventas.csv"
    output_file = "../../datasets/processed/ventas_cleaned.csv"
    
    if Path(input_file).exists():
        stats_seq = processor.process_file_sequential(
            input_file,
            output_file,
            clean_sales_data
        )
        
        logger.info(f"Resultados:")
        logger.info(f"  - Chunks procesados: {stats_seq['chunks_processed']}")
        logger.info(f"  - Total de filas: {stats_seq['total_rows']}")
        logger.info(f"  - Duración: {stats_seq['duration']:.2f}s")
    else:
        logger.warning(f"Archivo no encontrado: {input_file}")
    
    # Ejemplo 2: Agregación
    logger.info("\n--- Ejemplo 2: Agregación por Lotes ---")
    
    if Path(input_file).exists():
        stats_agg = processor.aggregate_by_key(
            input_file,
            "../../datasets/processed/ventas_aggregated.csv",
            group_by=['cliente_id'],
            agg_dict={
                'cantidad': 'sum',
                'total': 'sum'
            }
        )
        
        logger.info(f"Resultados:")
        logger.info(f"  - Grupos: {stats_agg['groups']}")
        logger.info(f"  - Duración: {stats_agg['duration']:.2f}s")
    
    logger.info("\n" + "=" * 60)
    logger.info("PROCESAMIENTO COMPLETADO")
    logger.info("=" * 60)


if __name__ == "__main__":
    main()
