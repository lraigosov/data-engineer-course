#!/usr/bin/env python3
"""Añade IDs deterministas a celdas legacy de notebooks nbformat 4.5+."""

import argparse
import hashlib
import json
import sys
from pathlib import Path
from typing import Any


def _cell_source(cell: dict[str, Any]) -> str:
    source = cell.get("source", "")
    return "".join(source) if isinstance(source, list) else str(source)


def add_missing_cell_ids(notebook: dict[str, Any], relative_path: str) -> int:
    """Añade IDs estables y únicos; devuelve cuántas celdas cambió."""
    cells = notebook.get("cells", [])
    used_ids = {cell.get("id") for cell in cells if cell.get("id")}
    changed = 0

    for index, cell in enumerate(cells):
        if cell.get("id"):
            continue

        seed = "\0".join(
            (relative_path, str(index), cell.get("cell_type", ""), _cell_source(cell))
        )
        attempt = 0
        while True:
            value = hashlib.sha256(f"{seed}\0{attempt}".encode()).hexdigest()[:8]
            if value not in used_ids:
                break
            attempt += 1

        cell["id"] = value
        used_ids.add(value)
        changed += 1

    return changed


def normalize_notebooks(repo_root: Path, check: bool = False) -> tuple[int, int]:
    """Normaliza notebooks y devuelve (archivos, celdas) pendientes."""
    changed_files = 0
    changed_cells = 0

    for path in sorted((repo_root / "notebooks").rglob("*.ipynb")):
        relative_path = path.relative_to(repo_root).as_posix()
        notebook = json.loads(path.read_text(encoding="utf-8"))
        count = add_missing_cell_ids(notebook, relative_path)
        if not count:
            continue

        changed_files += 1
        changed_cells += count
        if not check:
            path.write_text(
                json.dumps(notebook, ensure_ascii=False, indent=1) + "\n",
                encoding="utf-8",
            )

    return changed_files, changed_cells


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--check",
        action="store_true",
        help="No modifica archivos y falla si encuentra celdas sin ID.",
    )
    args = parser.parse_args()

    repo_root = Path(__file__).resolve().parents[1]
    files, cells = normalize_notebooks(repo_root, check=args.check)
    if args.check and cells:
        print(f"❌ {cells} celda(s) sin ID en {files} notebook(s)")
        return 1

    action = "normalizadas" if not args.check else "verificadas"
    print(f"✅ Metadata {action}: {cells} celda(s) en {files} notebook(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
