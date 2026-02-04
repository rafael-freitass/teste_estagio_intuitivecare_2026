import os
import zipfile
from config.paths import EXTRACTED
from services.download_service import download_arquivos
from services.infos_ans import extrair_ano_e_trimestre

def extrair_arquivos():
    os.makedirs(EXTRACTED, exist_ok=True)

    arquivos_zip = download_arquivos()

    pastas_extraidas = []

    for caminho_zip in arquivos_zip:
        nome_arquivo = os.path.basename(caminho_zip)

        resultado = extrair_ano_e_trimestre(nome_arquivo)
        if not resultado:
            continue

        ano, trimestre = resultado
        pasta_destino = os.path.join(EXTRACTED, f"{ano}_T{trimestre}")

        if os.path.exists(pasta_destino):
            pastas_extraidas.append(pasta_destino)
            continue

        os.makedirs(pasta_destino, exist_ok=True)

        with zipfile.ZipFile(caminho_zip, "r") as zip_ref:
            zip_ref.extractall(pasta_destino)

        pastas_extraidas.append(pasta_destino)

    return pastas_extraidas