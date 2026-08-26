#!/usr/bin/env python3
"""
Ejecuta notebooks realmente (vía nbclient) para verificar que corren de
punta a punta, a diferencia de validate_notebook_code.py que solo revisa
sintaxis con ast.parse.

Por defecto SALTA los notebooks que requieren credenciales de servicios
externos (APIs de OpenAI/Gemini, AWS/GCP/Azure en vivo) — ver
EXTERNAL_DEPENDENCY_PATTERNS más abajo — porque no deben consumir APIs
reales ni depender de secretos en cada corrida de CI. Usa --include-external
para forzar su ejecución (requiere credenciales configuradas localmente).

Uso:
    python scripts/execute_notebooks.py                  # allowlist verificada en CI
    python scripts/execute_notebooks.py --all-local      # descubrimiento heurístico
    python scripts/execute_notebooks.py --include-external
    python scripts/execute_notebooks.py --path notebooks/nivel_junior
    python scripts/execute_notebooks.py --write           # persiste outputs
"""

import argparse
import sys
from pathlib import Path

try:
    import nbformat
    from nbclient import NotebookClient
    from nbclient.exceptions import CellExecutionError
except ImportError:
    print("❌ Faltan dependencias: pip install -r requirements-dev.txt")
    sys.exit(1)

# Notebooks/directorios que requieren credenciales externas (API keys de
# OpenAI/Gemini, cuentas cloud reales) y por eso no se ejecutan en CI por
# defecto. Se validan solo estáticamente (validate_notebook_code.py).
EXTERNAL_DEPENDENCY_PATTERNS = [
    "nivel_genai",         # OpenAI / Gemini API keys
    "03_cloud_aws",        # llamadas reales a AWS
    "03b_cloud_gcp",       # llamadas reales a GCP
    "03c_cloud_azure",     # llamadas reales a Azure
]

DEFAULT_TIMEOUT_SECONDS = 300
DEFAULT_MANIFEST = "config/notebooks-ci.txt"


def requires_external_deps(notebook_path: Path) -> bool:
    return any(pattern in str(notebook_path) for pattern in EXTERNAL_DEPENDENCY_PATTERNS)


def execute_notebook(notebook_path: Path, write: bool, timeout: int) -> tuple[bool, str]:
    nb = nbformat.read(notebook_path, as_version=4)
    client = NotebookClient(
        nb,
        timeout=timeout,
        kernel_name="python3",
        resources={"metadata": {"path": str(notebook_path.parent)}},
    )
    try:
        client.execute()
    except CellExecutionError as e:
        return False, str(e).splitlines()[0] if str(e) else "CellExecutionError"
    except Exception as e:  # kernel startup issues, etc.
        return False, f"{type(e).__name__}: {e}"

    if write:
        nbformat.write(nb, notebook_path)

    return True, ""


def read_manifest(repo_root: Path, manifest_path: str) -> list[Path]:
    manifest = repo_root / manifest_path
    if not manifest.exists():
        raise FileNotFoundError(f"Manifest no encontrado: {manifest}")

    notebooks = []
    for raw_line in manifest.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue
        notebook = (repo_root / line).resolve()
        if repo_root.resolve() not in notebook.parents:
            raise ValueError(f"Ruta fuera del repositorio en {manifest}: {line}")
        if notebook.suffix != ".ipynb" or not notebook.is_file():
            raise FileNotFoundError(f"Notebook inválido en {manifest}: {line}")
        notebooks.append(notebook)
    return notebooks


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--path", help="Directorio o archivo .ipynb a ejecutar")
    parser.add_argument("--manifest", default=DEFAULT_MANIFEST, help="Allowlist de notebooks verificados")
    parser.add_argument("--all-local", action="store_true", help="Descubre todos los notebooks y excluye dependencias externas por heurística")
    parser.add_argument("--include-external", action="store_true", help="Incluye notebooks que requieren credenciales externas")
    parser.add_argument("--write", action="store_true", help="Persiste los outputs de ejecución en el .ipynb")
    parser.add_argument("--timeout", type=int, default=DEFAULT_TIMEOUT_SECONDS, help="Timeout por notebook, en segundos")
    args = parser.parse_args()

    repo_root = Path(__file__).resolve().parents[1]
    if args.path:
        requested = Path(args.path)
        target = (repo_root / requested) if not requested.is_absolute() else requested
        if target.is_file():
            notebooks = [target]
        else:
            notebooks = sorted(target.rglob("*.ipynb"))
    elif args.all_local:
        notebooks = sorted((repo_root / "notebooks").rglob("*.ipynb"))
    else:
        notebooks = read_manifest(repo_root, args.manifest)

    if not args.include_external:
        skipped = [nb for nb in notebooks if requires_external_deps(nb)]
        notebooks = [nb for nb in notebooks if not requires_external_deps(nb)]
        if skipped:
            print(f"⏭️  Saltando {len(skipped)} notebook(s) que requieren credenciales externas (usa --include-external para incluirlos):")
            for nb in skipped:
                print(f"    - {nb.relative_to(repo_root)}")

    if not notebooks:
        print("⚠️  No hay notebooks para ejecutar.")
        return 0

    print(f"\n▶️  Ejecutando {len(notebooks)} notebook(s)...\n")

    failures = []
    for nb_path in notebooks:
        rel = nb_path.relative_to(repo_root)
        print(f"  {rel} ... ", end="", flush=True)
        ok, error = execute_notebook(nb_path, write=args.write, timeout=args.timeout)
        if ok:
            print("✅")
        else:
            print(f"❌ {error}")
            failures.append((rel, error))

    print("\n" + "=" * 80)
    print(f"📊 Resultado: {len(notebooks) - len(failures)}/{len(notebooks)} ejecutados sin errores")
    if failures:
        print("\nFallos:")
        for rel, error in failures:
            print(f"  - {rel}: {error}")
    print("=" * 80)

    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
