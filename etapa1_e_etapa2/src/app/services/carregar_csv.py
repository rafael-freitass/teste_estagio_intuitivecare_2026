import pandas as pd
from zipfile import ZipFile
from pathlib import Path

def carregar_csv_consolidado(caminho_zip, temp_dir):
    with ZipFile(caminho_zip, "r") as zip_ref:
        zip_ref.extractall(temp_dir)

    caminho_csv = next(Path(temp_dir).rglob("*.csv"))

    df = pd.read_csv(
        caminho_csv,
        dtype={"cnpj": str}
    )

    df.columns = [c.lower() for c in df.columns]

    df["cnpj"] = (
        df["cnpj"]
        .astype(str)
        .str.replace(r"\.0$", "", regex=True)  # remove o .0 do float
        .str.replace(r"\D", "", regex=True)
        .str.zfill(14)
    )

    colunas_esperadas = {
        "cnpj", "razao_social", "trimestre", "ano", "valor_despesas"
    }

    faltando = colunas_esperadas - set(df.columns)
    if faltando:
        raise ValueError(f"Colunas ausentes no consolidado: {faltando}")

    return df


def carregar_operadoras(caminho_csv):
    df = pd.read_csv(
        caminho_csv,
        sep=";",
        encoding="latin1",
        dtype=str
    )

    df.columns = [c.lower() for c in df.columns]

    if "registro_operadora" in df.columns:
        df = df.rename(columns={
            "registro_operadora": "registro_ans"
        })

    colunas_necessarias = {
        "cnpj", "registro_ans", "modalidade", "uf"
    }

    df["cnpj"] = (
        df["cnpj"]
        .astype(str)
        .str.replace(r"\.0$", "", regex=True)  # remove o .0 do float
        .str.replace(r"\D", "", regex=True)
        .str.zfill(14)
    )


    faltando = colunas_necessarias - set(df.columns)
    if faltando:
        raise ValueError(
            f"Colunas obrigatórias ausentes no cadastro de operadoras: {faltando}"
        )

    return df