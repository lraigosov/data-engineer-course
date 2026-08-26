"""Tests de las herramientas que validan y normalizan notebooks."""

from scripts.normalize_notebook_metadata import add_missing_cell_ids
from scripts.validate_notebook_code import CodeValidator


def test_validator_does_not_report_textual_unused_variable_false_positives():
    validator = CodeValidator()
    code = "value = 1\nassert value == 1\nconfig = {'enabled': True}"

    is_valid, issues = validator.validate_cell_code(code, cell_index=1)

    assert is_valid
    assert issues == []


def test_validator_reports_real_syntax_errors():
    validator = CodeValidator()

    is_valid, issues = validator.validate_cell_code("if True print('x')", 1)

    assert not is_valid
    assert any("SINTAXIS ERROR" in issue for issue in issues)


def test_add_missing_cell_ids_is_deterministic_and_preserves_existing_ids():
    first = {
        "cells": [
            {"cell_type": "markdown", "source": ["# Título"], "metadata": {}},
            {"cell_type": "code", "id": "existing", "source": "x = 1"},
        ]
    }
    second = {
        "cells": [
            {"cell_type": "markdown", "source": ["# Título"], "metadata": {}},
            {"cell_type": "code", "id": "existing", "source": "x = 1"},
        ]
    }

    assert add_missing_cell_ids(first, "notebooks/example.ipynb") == 1
    assert add_missing_cell_ids(second, "notebooks/example.ipynb") == 1
    assert first["cells"][0]["id"] == second["cells"][0]["id"]
    assert first["cells"][1]["id"] == "existing"
