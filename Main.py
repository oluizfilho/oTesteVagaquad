from google.cloud import bigquery

import os
import pandas
from datetime import datetime

#Chave Acesso Google - Conta Luiz
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "Access_google.json"

#Dir arquivos texto
cam = r"Files\\"

#Conexão Cliente bigquery
bigqueryClient = bigquery.Client()
tableBq= bigqueryClient.dataset("Boticario").table("tbVendas")


#Percorre os arquivos e insere os dados no Bigquery
for c in os.listdir(cam):
	arquivo = c

	#Arquivo Dados

	caminho = ("Files\\%a" % (arquivo))

	#Leitura Arq

	dadosarq= pandas.read_csv(caminho.replace("'", ""),  header=0,sep=';', parse_dates=True)

	#Trata Campo datetime

	dadosarq['DATA_VENDA'] = pandas.to_datetime(dadosarq['DATA_VENDA'], format='%d/%m/%Y')

	#INSERT Dados

	bigqueryJob = bigqueryClient.load_table_from_dataframe(dadosarq, tableBq)	





		
