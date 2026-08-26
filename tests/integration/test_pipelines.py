"""Integration tests that exercise the repository's real ETL pipelines."""

import json

import pandas as pd

from scripts.etl.simple_etl import SimpleETLPipeline
from scripts.pipelines.data_ingestion_pipeline import DataIngestionPipeline


class FakeResponse:
    """Minimal requests.Response substitute for deterministic API tests."""

    def __init__(self, payload):
        self._payload = payload

    def raise_for_status(self):
        return None

    def json(self):
        return self._payload


def test_simple_etl_pipeline_extract_transform_load(monkeypatch, tmp_path):
    payload = [
        {"id": 1, "nombre": "Ana"},
        {"id": 1, "nombre": "Ana"},
        {"id": 2, "nombre": None},
    ]
    monkeypatch.setattr(
        "scripts.etl.simple_etl.requests.get",
        lambda *args, **kwargs: FakeResponse(payload),
    )
    pipeline = SimpleETLPipeline("https://example.invalid/users", str(tmp_path))

    result = pipeline.run("usuarios.csv")

    assert result["status"] == "success"
    assert result["records_processed"] == 1
    output = pd.read_csv(tmp_path / "usuarios.csv")
    assert output["id"].tolist() == [1]
    assert {"processed_at", "process_id"}.issubset(output.columns)


def test_data_ingestion_pipeline_runs_real_csv_to_json_flow(tmp_path):
    input_path = tmp_path / "clientes.csv"
    output_dir = tmp_path / "processed"
    pd.DataFrame(
        {
            "cliente_id": [1, 1, 2],
            "nombre": ["Ana", "Ana", "Luis"],
            "ciudad": [None, None, "Bogotá"],
        }
    ).to_csv(input_path, index=False)
    config = {
        "output_path": str(output_dir),
        "data_sources": {
            "clientes": {
                "type": "csv",
                "path": str(input_path),
                "validation": {"required_columns": ["cliente_id", "nombre"]},
                "transformations": {
                    "remove_duplicates": True,
                    "fill_nulls": {"ciudad": "Desconocida"},
                    "add_timestamp": True,
                },
                "output": {"type": "json", "filename": "clientes.json"},
            }
        },
    }

    result = DataIngestionPipeline(config).run()

    assert result["status"] == "success"
    assert result["sources_processed"] == 1
    assert result["total_records"] == 2
    with (output_dir / "clientes.json").open(encoding="utf-8") as output_file:
        records = json.load(output_file)
    assert records[0]["ciudad"] == "Desconocida"
    assert "ingestion_timestamp" in records[0]


def test_data_ingestion_pipeline_reports_validation_failure(tmp_path):
    input_path = tmp_path / "invalid.csv"
    pd.DataFrame({"unexpected": [1]}).to_csv(input_path, index=False)
    config = {
        "output_path": str(tmp_path / "processed"),
        "data_sources": {
            "invalid": {
                "type": "csv",
                "path": str(input_path),
                "validation": {"required_columns": ["id"]},
            }
        },
    }

    result = DataIngestionPipeline(config).run()

    assert result["status"] == "completed_with_errors"
    assert result["sources_processed"] == 0
    assert result["errors"] == ["Validación fallida para invalid"]
