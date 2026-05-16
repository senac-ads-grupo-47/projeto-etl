import pandas as pd
import os
from transform import transform

def load (df):
	endereco_csv = os.path.join (os.path.dirname (__file__), "..", "data-frame", "modifified", "car_price_dataset_mod.csv")
	try:
		df.to_csv (endereco_csv, index = False, header = True)
		print ("Arquivo csv criado")
		return df
	except FileNotFoundError:
		raise Exception (f"Diretório não existe: {endereco_csv}")

if __name__ == '__main__':
	df = transform()
	df_criado = load (df_modificado)
