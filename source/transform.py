import pandas as pd
from datetime import datetime

def transform(df):

    df = df.drop_duplicates()
    df = df.dropna()
