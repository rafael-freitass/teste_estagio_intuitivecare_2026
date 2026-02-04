import shutil
from config.paths import OUTPUT, TEMP
from services.carregar_csv import carregar_csv_consolidado, carregar_operadoras
from services.validacao_service import aplicar_validacoes
from services.enriquecimento_service import enriquecer_com_operadoras
from services.download_service import download_operadoras
from services.agregacao_service import agragacao_rs_uf, salvar_csv_agregado, compactar_resultado

def etapa2_pipeline():
    df = carregar_csv_consolidado(f"{OUTPUT}/consolidado_despesas.zip", TEMP)
    df = aplicar_validacoes(df)
    
    caminho_operadoras = download_operadoras()
    df_operadoras = carregar_operadoras(caminho_operadoras)

    df = enriquecer_com_operadoras(df, df_operadoras)

    df_agregado = agragacao_rs_uf(df)
    salvar_csv_agregado(df_agregado)

    compactar_resultado("Rafael")
    shutil.rmtree(TEMP, ignore_errors=True)