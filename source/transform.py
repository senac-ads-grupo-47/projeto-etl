import pandas as pd
from datetime import datetime

def transform(df):

    df = df.drop_duplicates()
    df = df.dropna()

    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
    )

    colunas_numericas = [
        "year",
        "price",
        "mileage",
        "engine_size",
        "doors",
        "owner_count"
    ]

    for coluna in colunas_numericas:

        if coluna in df.columns:

            df[coluna] = pd.to_numeric(
                df[coluna],
                errors="coerce"
            )

    df = df.dropna()

    colunas_texto = [
        "brand",
        "model",
        "fuel_type",
        "transmission"
    ]

    for coluna in colunas_texto:

        if coluna in df.columns:

            df[coluna] = (
                df[coluna]
                .astype(str)
                .str.strip()
                .str.lower()
            )

    ano_atual = datetime.now().year

    if "year" in df.columns:

        df["car_age"] = ano_atual - df["year"]

    if "price" in df.columns and "mileage" in df.columns:

        df["price_per_km"] = (
            df["price"] / (df["mileage"] + 1)
        )

    if "price" in df.columns:
        
        df["price_category"] = pd.qcut(
            df["price"],
            q=4,
            labels=["baixo", "medio", "alto", "luxo"]
        )

    df = df.reset_index(drop=True)

    print("Transformação concluída com sucesso")
    return df                