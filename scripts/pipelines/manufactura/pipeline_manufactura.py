"""
Pipeline Manufactura (toy): calcula OEE por turno y exporta datasets/processed/manufactura_oee.csv
- compute_oee(df) recibe un DataFrame con columnas disp, rend, cal y turno.
- CLI con click para leer CSV o generar datos de ejemplo si no se provee.
"""
from __future__ import annotations
from pathlib import Path
import pandas as pd
import click


def compute_oee(df: pd.DataFrame) -> pd.DataFrame:
    out = df.copy()
    for col in ['disp', 'rend', 'cal']:
        if col not in out.columns:
            raise ValueError(f"Falta columna requerida: {col}")
    out['OEE'] = out['disp'] * out['rend'] * out['cal']
    if 'turno' in out.columns:
        return out.groupby('turno', as_index=False).agg(OEE=('OEE', 'mean'))
    return out[['OEE']]


@click.command()
@click.option('--input', 'input_path', type=click.Path(path_type=Path), default=None, help='CSV con columnas turno, disp, rend, cal')
@click.option('--outdir', type=click.Path(path_type=Path), default=Path('datasets/processed'))
def main(input_path: Path | None, outdir: Path):
    outdir.mkdir(parents=True, exist_ok=True)
    if input_path and Path(input_path).exists():
        df = pd.read_csv(input_path)
    else:
        df = pd.DataFrame({
            'turno': ['A','B','C'],
            'disp': [0.92, 0.88, 0.90],
            'rend': [0.93, 0.90, 0.92],
            'cal':  [0.98, 0.95, 0.97],
        })
    oee = compute_oee(df)
    oee.to_csv(outdir / 'manufactura_oee.csv', index=False)
    click.echo(f"OEE exportado a {outdir}")


if __name__ == '__main__':
    main()
