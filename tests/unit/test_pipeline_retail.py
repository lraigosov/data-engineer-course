import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]))
import pandas as pd
from scripts.pipelines.retail.pipeline_retail import compute_kpis


def test_compute_kpis_basic():
    ventas = pd.DataFrame({
        'fecha': ['2025-01-10','2025-01-15','2025-02-01'],
        'producto_id': ['A','B','A'],
        'cantidad': [2, 1, 3],
        'precio': [10.0, 20.0, 10.0],
    })
    productos = pd.DataFrame({
        'producto_id': ['A','B'],
        'nombre': ['SKU A','SKU B']
    })
    kpis = compute_kpis(ventas, productos)

    # Mensual debe tener 2 filas (ene y feb) y suma correcta
    mensual = kpis['mensual']
    assert mensual['ingreso'].sum() == (2*10.0 + 1*20.0 + 3*10.0)

    # Top SKU: A debe estar primero
    top = kpis['top_sku']
    assert top.iloc[0]['producto_id'] == 'A'
    assert 'nombre' in top.columns
