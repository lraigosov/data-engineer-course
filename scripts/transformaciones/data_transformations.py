"""
Funciones Auxiliares para Transformación de Datos
=================================================

Colección de funciones reutilizables para limpieza y transformación de datos.

Autor: Curso de Ingeniería de Datos
"""

import pandas as pd
import numpy as np
from typing import List, Dict, Any, Optional
import re
from datetime import datetime


def limpiar_columnas_texto(df: pd.DataFrame, columnas: List[str]) -> pd.DataFrame:
    """
    Limpia columnas de texto: elimina espacios, convierte a minúsculas
    
    Args:
        df: DataFrame a procesar
        columnas: Lista de columnas a limpiar
        
    Returns:
        DataFrame con columnas limpias
    """
    df_copy = df.copy()
    
    for col in columnas:
        if col in df_copy.columns:
            df_copy[col] = (df_copy[col]
                           .astype(str)
                           .str.strip()
                           .str.lower())
    
    return df_copy


def validar_emails(df: pd.DataFrame, columna_email: str) -> pd.DataFrame:
    """
    Valida y marca emails válidos/inválidos
    
    Args:
        df: DataFrame con columna de emails
        columna_email: Nombre de la columna con emails
        
    Returns:
        DataFrame con columna adicional de validación
    """
    df_copy = df.copy()
    
    # Patrón simple de validación de email
    patron_email = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    df_copy[f'{columna_email}_valido'] = (
        df_copy[columna_email]
        .astype(str)
        .str.match(patron_email)
    )
    
    return df_copy


def eliminar_outliers(df: pd.DataFrame, 
                      columna: str, 
                      metodo: str = 'iqr',
                      umbral: float = 1.5) -> pd.DataFrame:
    """
    Elimina outliers usando IQR o desviación estándar
    
    Args:
        df: DataFrame a procesar
        columna: Columna numérica a analizar
        metodo: 'iqr' o 'std'
        umbral: Factor de umbral (1.5 para IQR, 3 para std)
        
    Returns:
        DataFrame sin outliers
    """
    df_copy = df.copy()
    
    if metodo == 'iqr':
        Q1 = df_copy[columna].quantile(0.25)
        Q3 = df_copy[columna].quantile(0.75)
        IQR = Q3 - Q1
        
        limite_inferior = Q1 - umbral * IQR
        limite_superior = Q3 + umbral * IQR
        
    elif metodo == 'std':
        media = df_copy[columna].mean()
        std = df_copy[columna].std()
        
        limite_inferior = media - umbral * std
        limite_superior = media + umbral * std
    
    else:
        raise ValueError("Método debe ser 'iqr' o 'std'")
    
    mask = (
        (df_copy[columna] >= limite_inferior) &
        (df_copy[columna] <= limite_superior)
    )
    
    outliers_removidos = (~mask).sum()
    print(f"Outliers removidos de '{columna}': {outliers_removidos}")
    
    return df_copy[mask]


def normalizar_fechas(df: pd.DataFrame, 
                     columna_fecha: str,
                     formato: Optional[str] = None) -> pd.DataFrame:
    """
    Normaliza columnas de fecha a datetime
    
    Args:
        df: DataFrame a procesar
        columna_fecha: Columna con fechas
        formato: Formato de fecha (opcional)
        
    Returns:
        DataFrame con fechas normalizadas
    """
    df_copy = df.copy()
    
    if formato:
        df_copy[columna_fecha] = pd.to_datetime(
            df_copy[columna_fecha],
            format=formato,
            errors='coerce'
        )
    else:
        df_copy[columna_fecha] = pd.to_datetime(
            df_copy[columna_fecha],
            errors='coerce'
        )
    
    # Contar fechas inválidas
    invalidas = df_copy[columna_fecha].isnull().sum()
    if invalidas > 0:
        print(f"Advertencia: {invalidas} fechas inválidas en '{columna_fecha}'")
    
    return df_copy


def crear_columnas_temporales(df: pd.DataFrame, 
                              columna_fecha: str) -> pd.DataFrame:
    """
    Crea columnas derivadas de fecha (año, mes, día, etc.)
    
    Args:
        df: DataFrame con columna de fecha
        columna_fecha: Nombre de la columna fecha
        
    Returns:
        DataFrame con columnas temporales adicionales
    """
    df_copy = df.copy()
    
    # Asegurar que es datetime
    df_copy[columna_fecha] = pd.to_datetime(df_copy[columna_fecha])
    
    # Crear columnas derivadas
    df_copy[f'{columna_fecha}_anio'] = df_copy[columna_fecha].dt.year
    df_copy[f'{columna_fecha}_mes'] = df_copy[columna_fecha].dt.month
    df_copy[f'{columna_fecha}_dia'] = df_copy[columna_fecha].dt.day
    df_copy[f'{columna_fecha}_dia_semana'] = df_copy[columna_fecha].dt.dayofweek
    df_copy[f'{columna_fecha}_trimestre'] = df_copy[columna_fecha].dt.quarter
    df_copy[f'{columna_fecha}_semana'] = df_copy[columna_fecha].dt.isocalendar().week
    
    return df_copy


def imputar_valores_faltantes(df: pd.DataFrame,
                              estrategia: Dict[str, str]) -> pd.DataFrame:
    """
    Imputa valores faltantes según estrategia definida
    
    Args:
        df: DataFrame a procesar
        estrategia: Dict con {columna: método}
                   Métodos: 'mean', 'median', 'mode', 'forward', 'backward', valor
        
    Returns:
        DataFrame con valores imputados
    """
    df_copy = df.copy()
    
    for columna, metodo in estrategia.items():
        if columna not in df_copy.columns:
            print(f"Advertencia: Columna '{columna}' no existe")
            continue
        
        if metodo == 'mean':
            df_copy[columna].fillna(df_copy[columna].mean(), inplace=True)
        elif metodo == 'median':
            df_copy[columna].fillna(df_copy[columna].median(), inplace=True)
        elif metodo == 'mode':
            df_copy[columna].fillna(df_copy[columna].mode()[0], inplace=True)
        elif metodo == 'forward':
            df_copy[columna].fillna(method='ffill', inplace=True)
        elif metodo == 'backward':
            df_copy[columna].fillna(method='bfill', inplace=True)
        else:
            # Valor constante
            df_copy[columna].fillna(metodo, inplace=True)
    
    return df_copy


def estandarizar_columnas(df: pd.DataFrame, 
                         columnas: List[str]) -> pd.DataFrame:
    """
    Estandariza columnas numéricas (media=0, std=1)
    
    Args:
        df: DataFrame a procesar
        columnas: Lista de columnas a estandarizar
        
    Returns:
        DataFrame con columnas estandarizadas
    """
    df_copy = df.copy()
    
    for col in columnas:
        if col in df_copy.columns:
            media = df_copy[col].mean()
            std = df_copy[col].std()
            df_copy[f'{col}_std'] = (df_copy[col] - media) / std
    
    return df_copy


def crear_bins_numericos(df: pd.DataFrame,
                        columna: str,
                        bins: int = 5,
                        etiquetas: Optional[List[str]] = None) -> pd.DataFrame:
    """
    Crea bins (categorías) para una columna numérica
    
    Args:
        df: DataFrame a procesar
        columna: Columna numérica
        bins: Número de bins
        etiquetas: Etiquetas opcionales para los bins
        
    Returns:
        DataFrame con columna de bins
    """
    df_copy = df.copy()
    
    df_copy[f'{columna}_bin'] = pd.cut(
        df_copy[columna],
        bins=bins,
        labels=etiquetas,
        include_lowest=True
    )
    
    return df_copy


def codificar_categoricas(df: pd.DataFrame,
                          columnas: List[str],
                          metodo: str = 'onehot') -> pd.DataFrame:
    """
    Codifica variables categóricas
    
    Args:
        df: DataFrame a procesar
        columnas: Columnas categóricas
        metodo: 'onehot' o 'label'
        
    Returns:
        DataFrame con columnas codificadas
    """
    df_copy = df.copy()
    
    if metodo == 'onehot':
        df_copy = pd.get_dummies(
            df_copy,
            columns=columnas,
            prefix=columnas,
            drop_first=True
        )
    elif metodo == 'label':
        for col in columnas:
            df_copy[f'{col}_encoded'] = pd.factorize(df_copy[col])[0]
    
    return df_copy


def detectar_duplicados_avanzado(df: pd.DataFrame,
                                subset: Optional[List[str]] = None,
                                keep_strategy: str = 'first') -> Dict[str, Any]:
    """
    Detecta y reporta duplicados con estadísticas
    
    Args:
        df: DataFrame a analizar
        subset: Columnas para detectar duplicados
        keep_strategy: 'first', 'last' o False
        
    Returns:
        Dict con estadísticas y DataFrame sin duplicados
    """
    duplicados_mask = df.duplicated(subset=subset, keep=False)
    total_duplicados = duplicados_mask.sum()
    
    resultado = {
        'total_registros': len(df),
        'total_duplicados': total_duplicados,
        'porcentaje_duplicados': (total_duplicados / len(df)) * 100,
        'duplicados_df': df[duplicados_mask],
        'limpio_df': df.drop_duplicates(subset=subset, keep=keep_strategy)
    }
    
    print(f"Total registros: {resultado['total_registros']}")
    print(f"Duplicados encontrados: {resultado['total_duplicados']} "
          f"({resultado['porcentaje_duplicados']:.2f}%)")
    
    return resultado


# Ejemplo de uso
if __name__ == "__main__":
    print("Funciones de transformación cargadas correctamente")
    print("\nFunciones disponibles:")
    print("  - limpiar_columnas_texto")
    print("  - validar_emails")
    print("  - eliminar_outliers")
    print("  - normalizar_fechas")
    print("  - crear_columnas_temporales")
    print("  - imputar_valores_faltantes")
    print("  - estandarizar_columnas")
    print("  - crear_bins_numericos")
    print("  - codificar_categoricas")
    print("  - detectar_duplicados_avanzado")
