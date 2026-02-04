def enriquecer_com_operadoras(df_consolidado, df_operadoras):
    df_operadoras = df_operadoras.drop_duplicates(subset=["cnpj"])

    df_enriquecido = df_consolidado.merge(
        df_operadoras[["cnpj", "registro_ans", "modalidade", "uf"]],
        on="cnpj",
        how="left"
    )

    if "reg_ans" in df_enriquecido.columns:
        df_enriquecido = df_enriquecido.drop(columns=["reg_ans"])

    return df_enriquecido
