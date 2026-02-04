import requests
from config.settings import settings

def listar_demonstracoes_contabeis():
    response = requests.get(
        f"{settings.API_BASE_URL}/demonstracoes_contabeis"
    )
    response.raise_for_status()
    return response.text

def listar_arquivos_do_ano(ano: int):
    response = requests.get(
        f"{settings.API_BASE_URL}/demonstracoes_contabeis/{ano}"
    )
    response.raise_for_status()
    return response.text

def listar_operadoras_ativas():
    response = requests.get(
        f"{settings.API_BASE_URL}/operadoras_de_plano_de_saude_ativas"
    )
    response.raise_for_status()
    return response.text