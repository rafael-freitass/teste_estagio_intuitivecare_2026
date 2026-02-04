import os
import requests
from config.paths import DOWNLOAD
from services.infos_ans import selecionar_ultimos_tres_trimestres, descobrir_arquivo_operadoras
from config.settings import settings

def download_arquivos():
    os.makedirs(DOWNLOAD, exist_ok=True)

    trimestres = selecionar_ultimos_tres_trimestres()

    arquivos_baixados = []

    for item in trimestres:
        url = item["url"]
        nome_arquivo = item["arquivo"]
        caminho_arquivo = os.path.join(DOWNLOAD, nome_arquivo)

        if os.path.exists(caminho_arquivo):
            arquivos_baixados.append(caminho_arquivo)
            continue

        response = requests.get(url, stream=True)
        response.raise_for_status()

        with open(caminho_arquivo, "wb") as f:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)

        arquivos_baixados.append(caminho_arquivo)

    return arquivos_baixados


def download_operadoras():
    os.makedirs(DOWNLOAD, exist_ok=True)

    nome_arquivo = descobrir_arquivo_operadoras()
    caminho = os.path.join(DOWNLOAD, nome_arquivo)

    if os.path.exists(caminho):
        return caminho

    url = f"{settings.API_BASE_URL}/operadoras_de_plano_de_saude_ativas/{nome_arquivo}"
    response = requests.get(url)
    response.raise_for_status()

    with open(caminho, "wb") as f:
        f.write(response.content)

    return caminho