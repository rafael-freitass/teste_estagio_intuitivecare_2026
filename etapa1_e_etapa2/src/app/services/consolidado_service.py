import csv
import zipfile
import pandas as pd
from config.paths import CONSOLIDADO, OUTPUT
from domain.despesas_eventos_sinistros import DespesasEventoSinistros
from config.paths import PROCESSED
import os

def consolidar_despesas_eventos():
    registros = []

    for pasta in os.listdir(PROCESSED):
        caminho_pasta = os.path.join(PROCESSED, pasta)

        if not os.path.isdir(caminho_pasta):
            continue

        try:
            ano_str, trimestre_str = pasta.split("_T")
            ano = int(ano_str)
            trimestre = int(trimestre_str)
        except ValueError:
            continue

        for arquivo in os.listdir(caminho_pasta):
            if not arquivo.endswith(".csv"):
                continue

            df = pd.read_csv(os.path.join(caminho_pasta, arquivo))

            if "vl_saldo_final" not in df.columns:
                continue

            col_reg_ans = next(
                (c for c in df.columns if c in ("reg_ans", "registro_operadora")),
                None
            )

            for _, row in df.iterrows():
                try:
                    valor = float(
                        str(row["vl_saldo_final"])
                        .replace(".", "")
                        .replace(",", ".")
                    )
                except ValueError:
                    continue

                registros.append(
                    DespesasEventoSinistros(
                        reg_ans=row[col_reg_ans] if col_reg_ans else None,
                        cnpj=None,
                        razao_social=None,
                        trimestre=trimestre,
                        ano=ano,
                        valor=valor
                    )
                )

    return registros


def gerar_csv_consolidado(registros):
    CONSOLIDADO.mkdir(parents=True, exist_ok=True)

    caminho = CONSOLIDADO / "consolidado_despesas.csv"

    registros = sorted(registros, key=lambda r: (r.ano, r.trimestre))

    with open(caminho, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([
            "reg_ans",
            "cnpj",
            "razao_social",
            "trimestre",
            "ano",
            "valor_despesas"
        ])

        for r in registros:
            writer.writerow([
                r.reg_ans,
                r.cnpj,
                r.razao_social,
                r.trimestre,
                r.ano,
                r.valor
            ])

    return caminho


def gerar_e_compactar_consolidado(df_enriquecido):
    OUTPUT.mkdir(parents=True, exist_ok=True)
    CONSOLIDADO.mkdir(parents=True, exist_ok=True)

    caminho_csv_temp = CONSOLIDADO / "consolidado_despesas.csv"
    df_enriquecido.to_csv(caminho_csv_temp, index=False)

    caminho_zip = OUTPUT / "consolidado_despesas.zip"

    with zipfile.ZipFile(caminho_zip, "w", zipfile.ZIP_DEFLATED) as zipf:
        zipf.write(
            caminho_csv_temp,
            arcname="consolidado_despesas.csv"
        )


    return