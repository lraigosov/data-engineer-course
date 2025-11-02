"""
Pipeline Retail (toy): lee ventas y productos, calcula KPIs simples y exporta a datasets/processed/retail_kpis.csv
- Función pura compute_kpis(ventas_df, productos_df) retorna DataFrames para testear sin IO.
- CLI con click para correr desde terminal.
"""
from __future__ import annotations
from pathlib import Path
import pandas as pd
import click


def compute_kpis(ventas: pd.DataFrame, productos: pd.DataFrame) -> dict[str, pd.DataFrame]:
    df = ventas.copy()
    if 'fecha' in df.columns:
        df['fecha'] = pd.to_datetime(df['fecha'], errors='coerce')
    qty = df.get('cantidad', df.get('unidades', 1))
    df['ingreso'] = df.get('precio', 0) * qty

    mensual = (
        df.groupby(pd.Grouper(key='fecha', freq='M'))['ingreso'].sum().reset_index()
        if 'fecha' in df.columns else pd.DataFrame({'fecha': [], 'ingreso': []})
    )
    if 'producto_id' in df.columns:
        top_sku = df.groupby('producto_id')['ingreso'].sum().reset_index()
        # enriquecer con nombre/categoría si está disponible
        if not productos.empty and 'producto_id' in productos.columns:
            cols = [c for c in productos.columns if c != 'producto_id']
            top_sku = top_sku.merge(productos[['producto_id'] + cols], on='producto_id', how='left')
        top_sku = top_sku.sort_values('ingreso', ascending=False).head(10)
    else:
        top_sku = pd.DataFrame({'producto_id': [], 'ingreso': []})
    return {"mensual": mensual, "top_sku": top_sku}


@click.command()
@click.option('--ventas', 'ventas_path', type=click.Path(path_type=Path), default=Path('datasets/raw/ventas.csv'))
@click.option('--productos', 'productos_path', type=click.Path(path_type=Path), default=Path('datasets/raw/productos.csv'))
@click.option('--outdir', type=click.Path(path_type=Path), default=Path('datasets/processed'))
def main(ventas_path: Path, productos_path: Path, outdir: Path):
    outdir.mkdir(parents=True, exist_ok=True)
    ventas_df = pd.read_csv(ventas_path)
    productos_df = pd.read_csv(productos_path)
    kpis = compute_kpis(ventas_df, productos_df)
    kpis['mensual'].to_csv(outdir / 'retail_ingreso_mensual.csv', index=False)
    kpis['top_sku'].to_csv(outdir / 'retail_top_sku.csv', index=False)
    click.echo(f"KPIs exportados a {outdir}")


if __name__ == '__main__':
    main()
