import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]))
import pandas as pd
from scripts.pipelines.manufactura.pipeline_manufactura import compute_oee


def test_compute_oee_por_turno():
    df = pd.DataFrame({
        'turno': ['A','B'],
        'disp': [0.9, 0.8],
        'rend': [0.9, 0.85],
        'cal':  [0.95, 0.9],
    })
    oee = compute_oee(df)
    assert set(oee.columns) == {'turno','OEE'}
    assert len(oee) == 2
    # OEE de A debería ser mayor que B en estos datos
    oee_dict = dict(zip(oee['turno'], oee['OEE']))
    assert oee_dict['A'] > oee_dict['B']
