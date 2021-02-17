from google.cloud import bigquery

import os
#Chave Acesso Google - Conta Luiz
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "Access_google.json"

client = bigquery.Client()


table_id = "primal-outrider-304522.Boticario.tbTweet"

schema = [
    bigquery.SchemaField("User", "STRING", mode="NULLABLE"),
    bigquery.SchemaField("Text", "STRING", mode="NULLABLE"),
    bigquery.SchemaField("Date", "DATE", mode="NULLABLE"),
]

table = bigquery.Table(table_id, schema=schema)
table = client.create_table(table)  # Make an API request.
print(
    "Created table {}.{}.{}".format(table.project, table.dataset_id, table.table_id)
)