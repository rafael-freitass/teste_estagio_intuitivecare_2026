import re
from bs4 import BeautifulSoup
from client.ans_client import listar_demonstracoes_contabeis, listar_operadoras_ativas, listar_arquivos_do_ano
from config.settings import settings


def descobrir_diretorios():
    html = listar_demonstracoes_contabeis()
    soup = BeautifulSoup(html, "html.parser")

    diretorios = []

    for link in soup.find_all("a"):
        href = link.get("href")
        if href and href.endswith("/") and href[:-1].isdigit():
            diretorios.append(int(href[:-1]))

    return sorted(diretorios)


def descobrir_arquivo_operadoras():
    html = listar_operadoras_ativas()
    soup = BeautifulSoup(html, "html.parser")

    for link in soup.find_all("a"):
        href = link.get("href")
        if href and href.lower().endswith(".csv"):
            return href

    raise RuntimeError("Arquivo CSV de operadoras não encontrado")


def extrair_ano_e_trimestre(nome_arquivo: str):
    nome = nome_arquivo.lower()

    if not nome.endswith(".zip"):
        return None

    ano_match = re.search(r"(20\d{2})", nome)
    if not ano_match:
        return None

    trimestre_match = re.search(
        r"(?:^|[^0-9])([1-4])\s*[-_ ]?\s*(t|trim|trimestre)",
        nome
    )

    if not trimestre_match:
        return None

    ano = int(ano_match.group(1))
    trimestre = int(trimestre_match.group(1))

    return ano, trimestre


def selecionar_ultimos_tres_trimestres():
    anos = descobrir_diretorios()
    anos_ordenados = sorted(anos, reverse=True)

    trimestres_selecionados = []

    for ano in anos_ordenados:
        html = listar_arquivos_do_ano(ano)
        soup = BeautifulSoup(html, "html.parser")

        trimestres_do_ano = []

        for link in soup.find_all("a"):
            href = link.get("href")
            if not href:
                continue

            resultado = extrair_ano_e_trimestre(href)

            if resultado:
                ano_extraido, trimestre = resultado

                trimestres_do_ano.append({
                    "ano": ano_extraido,
                    "trimestre": trimestre,
                    "arquivo": href,
                    "url": f"{settings.API_BASE_URL}/demonstracoes_contabeis/{ano}/{href}"
                })

        trimestres_do_ano.sort(
            key=lambda x: x["trimestre"],
            reverse=True
        )

        for item in trimestres_do_ano:
            trimestres_selecionados.append(item)

            if len(trimestres_selecionados) == 3:
                return trimestres_selecionados

    return trimestres_selecionados