import pandas as pd
import os

def extract():
	endereco_csv = os.path.join (os.path.dirname (__file__), "..", "data-frame", "original", "car_price_dataset.csv")
	try:
		df = pd.read_csv(endereco_csv)
		print ("Arquivo csv carregado")
		return df
	except FileNotFoundError:
		raise Exception (f"Arquivo csv não encontrado: {endereco_csv}")

if __name__ == "__main__":
	df = extract()