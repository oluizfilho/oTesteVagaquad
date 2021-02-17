import os
import tweepy as tw
from google.cloud import bigquery

from datetime import datetime

consumer_key = "22Lc30XlqEKIpd8Elt1UWjPVH"
consumer_secret = "HOnJwShKY9Q0PJqj0ypyZZ54ef6QsbhstT61TymbkQul73q4in"
access_token = "1361073430326575107-529KcwJEVdAAsv7BoXZ9OFuuJSgsqM"
access_token_secret = "vKcHddLxhur7r8cBPjwkS99G9HCBk15NQZGxQ2Tpo2Yfk"


#Autenticação Twitter
auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tw.API(auth, wait_on_rate_limit=True)

#Chave Acesso Google - Conta Luiz
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]  = "Access_google.json"

#Conexão Cliente bigquery
client = bigquery.Client()

# Consulta a. Palavras a serem pesquisadas: “Boticário” e o nome da linha com mais
# vendas no mês 12 de 2019 (conforme item 2.d.);
consulta = (
' select linha from('
' select linha,(sum(QTD_VENDA)) Vendas  FROM `primal-outrider-304522.Boticario.tbVendas`'
' where EXTRACT(Month FROM  data_venda) = 12 and EXTRACT(year FROM  data_venda)= 2019'
' group by linha'
' ) as tab1'
' order by vendas desc LIMIT 1')
consulta_job = client.query(consulta)  
retorno = consulta_job.result() 

#Palavra para Pesquisa
for row in retorno: 
    pesquisa = row.linha

dataset_ref = client.dataset('Boticario')
table_ref = dataset_ref.table('tbTweet')
table = client.get_table(table_ref)

def DadosTweets(pesquisa, numTweets ):

	tweets = tw.Cursor(api.search,
              	q=pesquisa,
              	lang="pt",
		since="2021-02-15",
 	      	tweet_mode="extended").items( numTweets)

	for tweet in tweets:
		rows_to_insert = [
			(tweet.user.screen_name,
				tweet.full_text,
				tweet.created_at),]
		print(rows_to_insert )
		errors = client.insert_rows(table, rows_to_insert)		


search_words = ['Boticario',pesquisa]
DadosTweets(pesquisa = search_words , numTweets = 50)
print (pesquisa)

