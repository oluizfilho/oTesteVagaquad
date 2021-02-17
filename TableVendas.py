from google.cloud import bigquery

import os
#Chave Acesso Google - Conta Luiz
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "Access_google.json"

client = bigquery.Client()


table_id = "primal-outrider-304522.Boticario.tbVendas"

schema = [
    bigquery.SchemaField("ID_MARCA", "INTEGER", mode="NULLABLE"),
    bigquery.SchemaField("MARCA", "STRING", mode="NULLABLE"),
    bigquery.SchemaField("ID_LINHA", "INTEGER", mode="NULLABLE"),
    bigquery.SchemaField("LINHA", "STRING", mode="NULLABLE"),
    bigquery.SchemaField("DATA_VENDA", "DATE", mode="NULLABLE"),
    bigquery.SchemaField("QTD_VENDA", "INTEGER", mode="NULLABLE"),
]

table = bigquery.Table(table_id, schema=schema)
table = client.create_table(table)  # Make an API request.
print(
    "Created table {}.{}.{}".format(table.project, table.dataset_id, table.table_id)
)