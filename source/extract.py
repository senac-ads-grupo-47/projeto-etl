import pandas as pd
import os

endereco_csv = os.path.join (os.path.dirname (__file__), "..", "data-frame", "original", "car_price_dataset.csv")
df = pd.read_csv (endereco_csv)
print ("Arquivo csv carregado")
