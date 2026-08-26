"""Unit tests for the reusable production transformations."""

import numpy as np
import pandas as pd
import pytest

from scripts.transformaciones.data_transformations import (
    codificar_categoricas,
    crear_columnas_temporales,
    detectar_duplicados_avanzado,
    eliminar_outliers,
    imputar_valores_faltantes,
    limpiar_columnas_texto,
    normalizar_fechas,
    validar_emails,
)


def test_limpiar_columnas_texto_does_not_mutate_input():
    source = pd.DataFrame({"nombre": ["  Juan  ", "MARÍA"], "edad": [25, 30]})

    result = limpiar_columnas_texto(source, ["nombre"])

    assert result["nombre"].tolist() == ["juan", "maría"]
    assert source["nombre"].tolist() == ["  Juan  ", "MARÍA"]


def test_validar_emails_marks_valid_and_invalid_values():
    source = pd.DataFrame(
        {"email": ["user.name@example.co", "invalido", "@example.com"]}
    )

    result = validar_emails(source, "email")

    assert result["email_valido"].tolist() == [True, False, False]


@pytest.mark.parametrize("metodo,umbral", [("iqr", 1.5), ("std", 2.0)])
def test_eliminar_outliers_removes_extreme_value(metodo, umbral):
    source = pd.DataFrame({"valor": [10, 10, 11, 9, 10, 1_000]})

    result = eliminar_outliers(source, "valor", metodo=metodo, umbral=umbral)

    assert 1_000 not in result["valor"].tolist()
    assert len(result) == 5


def test_eliminar_outliers_rejects_unknown_method():
    with pytest.raises(ValueError, match="Método"):
        eliminar_outliers(pd.DataFrame({"valor": [1, 2]}), "valor", metodo="mad")


def test_normalizar_y_derivar_fechas():
    source = pd.DataFrame({"fecha": ["2024-01-15", "invalida"]})

    normalized = normalizar_fechas(source, "fecha")
    valid_only = crear_columnas_temporales(normalized.iloc[[0]], "fecha")

    assert normalized["fecha"].isna().sum() == 1
    assert valid_only.loc[0, "fecha_anio"] == 2024
    assert valid_only.loc[0, "fecha_mes"] == 1
    assert valid_only.loc[0, "fecha_dia"] == 15


def test_imputar_valores_faltantes_uses_configured_strategies():
    source = pd.DataFrame(
        {
            "promedio": [1.0, np.nan, 3.0],
            "categoria": ["A", None, "A"],
            "estado": [None, "ok", None],
        }
    )

    result = imputar_valores_faltantes(
        source,
        {"promedio": "mean", "categoria": "mode", "estado": "desconocido"},
    )

    assert result["promedio"].tolist() == [1.0, 2.0, 3.0]
    assert result["categoria"].tolist() == ["A", "A", "A"]
    assert result["estado"].tolist() == ["desconocido", "ok", "desconocido"]


def test_codificar_categoricas_onehot_and_label():
    source = pd.DataFrame({"categoria": ["A", "B", "A"]})

    onehot = codificar_categoricas(source, ["categoria"], metodo="onehot")
    label = codificar_categoricas(source, ["categoria"], metodo="label")

    assert "categoria_B" in onehot.columns
    assert label["categoria_encoded"].nunique() == 2


def test_detectar_duplicados_returns_clean_dataframe_and_metrics():
    source = pd.DataFrame({"id": [1, 2, 2, 3], "valor": [10, 20, 20, 30]})

    result = detectar_duplicados_avanzado(source, subset=["id"])

    assert result["total_registros"] == 4
    assert result["total_duplicados"] == 2
    assert result["limpio_df"]["id"].tolist() == [1, 2, 3]
