from config.paths import OUTPUT, CONSOLIDADO
import zipfile

def agragacao_rs_uf(df):
    df_agregado = (
        df
        .groupby(["razao_social", "uf"])
        .agg(
            total_despesas=("valor_despesas", "sum"),
            media_trimestral=("valor_despesas", "mean"),
            desvio_padrao=("valor_despesas", "std")
        )
        .reset_index()
    )

    df_agregado = df_agregado.sort_values(
        by="total_despesas",
        ascending=False
    )

    return df_agregado

def salvar_csv_agregado(df_agregado):
    caminho_csv = f"{OUTPUT}/despesas_agregadas.csv"
    df_agregado.to_csv(caminho_csv, index=False)
    return caminho_csv

def compactar_resultado(nome):
    zip_path = f"{OUTPUT}/Teste_{nome}.zip"
    csv_path = f"{OUTPUT}/despesas_agregadas.csv"

    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zipf:
        zipf.write(csv_path, arcname="despesas_agregadas.csv")

    return zip_path
