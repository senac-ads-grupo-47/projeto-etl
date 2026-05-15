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