import shutil
from services.extrair_service import extrair_arquivos
from services.normalizacao_service import normalizar_arquivos_extraidos, normalizar_operadoras
from services.processamento_service import filtrar_despesas_eventos, associar_operadora_por_reg_ans
from services.consolidado_service import (
    consolidar_despesas_eventos,
    gerar_csv_consolidado,
    gerar_e_compactar_consolidado
)
from services.download_service import download_operadoras
from config.paths import TEMP

def etapa1_pipeline():
    extrair_arquivos()
    normalizar_arquivos_extraidos()
    filtrar_despesas_eventos()

    registros = consolidar_despesas_eventos()
    caminho_consolidado = gerar_csv_consolidado(registros)

    caminho_operadoras = download_operadoras()
    df_operadoras = normalizar_operadoras(caminho_operadoras)

    df_enriquecido = associar_operadora_por_reg_ans(
        caminho_consolidado,
        df_operadoras
    )

    gerar_e_compactar_consolidado(df_enriquecido)

    shutil.rmtree(TEMP, ignore_errors=True)
