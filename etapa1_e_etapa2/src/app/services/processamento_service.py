import os
import pandas as pd
from config.paths import NORMALIZED, PROCESSED

def filtrar_despesas_eventos():
    for pasta in os.listdir(NORMALIZED):
        origem = os.path.join(NORMALIZED, pasta)
        destino = os.path.join(PROCESSED, pasta)

        if not os.path.isdir(origem):
            continue

        os.makedirs(destino, exist_ok=True)

        for arquivo in os.listdir(origem):
            if not arquivo.endswith(".csv"):
                continue

            caminho = os.path.join(origem, arquivo)
            df = pd.read_csv(caminho)

            col_descricao = None
            for c in df.columns:
                if "descricao" in c:
                    col_descricao = c
                    break

            if not col_descricao:
                continue

            descricao = df[col_descricao].astype(str).str.lower()

            filtro = (
                descricao.str.contains("despesa") &
                (
                    descricao.str.contains("evento") |
                    descricao.str.contains("sinistro")
                )
            )

            df_filtrado = df[filtro]

            if df_filtrado.empty:
                continue

            nome_saida = f"despesas_eventos_{arquivo}"
            df_filtrado.to_csv(
                os.path.join(destino, nome_saida),
                index=False
            )


def associar_operadora_por_reg_ans(caminho_consolidado, df_operadoras):
    despesas = pd.read_csv(caminho_consolidado)

    despesas["reg_ans"] = despesas["reg_ans"].astype(str)
    df_operadoras["reg_ans"] = df_operadoras["reg_ans"].astype(str)

    df = despesas.merge(
        df_operadoras[["reg_ans", "cnpj", "razao_social"]],
        on="reg_ans",
        how="left"
    )

    df["cnpj"] = df["cnpj_y"]
    df["razao_social"] = df["razao_social_y"]

    df_final = df[[
        "reg_ans",
        "cnpj",
        "razao_social",
        "trimestre",
        "ano",
        "valor_despesas"
    ]]

    return df_final