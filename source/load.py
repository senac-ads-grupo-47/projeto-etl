import pandas as pd
import os
from transform import transforming

def load (df):
	endereco_csv = os.path.join (os.path.dirname (__file__), "..", "data-frame", "modified", "car_price_dataset_mod.csv")
	try:
		df.to_csv (endereco_csv, index = False, header = True)
		print ("Arquivo csv (modificado) salvo com sucesso")
		return df
	except (FileNotFoundError, OSError):
		raise Exception (f"Diretório não existe: {endereco_csv}")

def loading(): 
	df_modificado = transforming()
	df_criado = load (df_modificado)

if __name__ == '__main__':
	loading()