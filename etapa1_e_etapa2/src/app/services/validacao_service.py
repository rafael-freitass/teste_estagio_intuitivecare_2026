from utils.cnpj_utils import cnpj_eh_valido
import pandas as pd

def validacao_cpf(csv_consolidado):
    return csv_consolidado["cnpj"].apply(cnpj_eh_valido)

def validacao_valores_numericos(csv_consolidado):
    return (
        csv_consolidado["valor_despesas"].notna() &
        pd.to_numeric(csv_consolidado["valor_despesas"], errors="coerce").notna()
    )

def validacao_razao_social(csv_consolidado):
    return csv_consolidado["razao_social"].notna() & (
        csv_consolidado["razao_social"].str.strip() != ""
    )

def aplicar_validacoes(df):
    cnpj_ok = validacao_cpf(df)
    valor_ok = validacao_valores_numericos(df)
    razao_ok = validacao_razao_social(df)

    def definir_status(row):
        if not cnpj_ok[row.name]:
            return "CNPJ_INVALIDO"
        if not valor_ok[row.name]:
            return "VALOR_INVALIDO"
        if not razao_ok[row.name]:
            return "RAZAO_SOCIAL_INVALIDA"
        return "VALIDO"

    df["status_validacao"] = df.apply(definir_status, axis=1)
    return df