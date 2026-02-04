import os
import pandas as pd
from config.paths import EXTRACTED, NORMALIZED
from utils.normalizar_texto import normalizar_texto

def ler_arquivo(path: str):
    try:
        if path.lower().endswith((".csv", ".txt")):
            return pd.read_csv(
                path,
                sep=None,
                engine="python",
                encoding="latin1"
            )
        if path.lower().endswith(".xlsx"):
            return pd.read_excel(path)
    except Exception as e:
        print(f"[WARN] Erro ao ler {path}: {e}")
        return None

def normalizar_arquivos_extraidos():
    for pasta in os.listdir(EXTRACTED):
        origem = os.path.join(EXTRACTED, pasta)
        destino = os.path.join(NORMALIZED, pasta)

        if not os.path.isdir(origem):
            continue

        os.makedirs(destino, exist_ok=True)

        for arquivo in os.listdir(origem):
            if not arquivo.lower().endswith((".csv", ".txt", ".xlsx")):
                continue

            caminho = os.path.join(origem, arquivo)
            df = ler_arquivo(caminho)

            if df is None or df.empty:
                continue

            df.columns = [normalizar_texto(c) for c in df.columns]

            nome_saida = os.path.splitext(arquivo)[0] + ".csv"
            caminho_saida = os.path.join(destino, nome_saida)

            df.to_csv(caminho_saida, index=False)


def normalizar_operadoras(caminho_csv):
    df = pd.read_csv(caminho_csv, sep=";", encoding="latin1")

    df.columns = [normalizar_texto(c) for c in df.columns]

    if "registro_operadora" in df.columns:
        df = df.rename(columns={"registro_operadora": "reg_ans"})

    return df