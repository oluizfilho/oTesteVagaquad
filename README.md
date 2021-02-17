1. Realizar a importação dos dados dos 3 arquivos em uma tabela criada por você
no banco de dados de sua escolha;
2. Com os dados importados, modelar 4 novas tabelas e implementar processos
que façam as transformações necessárias e insiram as seguintes visões nas
tabelas:
a. Tabela1: Consolidado de vendas por ano e mês;
b. Tabela2: Consolidado de vendas por marca e linha;
c. Tabela3: Consolidado de vendas por marca, ano e mês;
d. Tabela4: Consolidado de vendas por linha, ano e mês;
3. Criar uma conta de acesso comum ao Twitter
4. Acessar https://developer.twitter.com/en/apply-for-access e criar uma conta
de desenvolvedor;
5. Após criar a conta, acesse o menu App e crie um aplicativo. Para fins de testes,
os dados não precisam ser precisos. A URL por exemplo, pode
colocar http://localhost.com
6. Após criado o app, acesse o mesmo e gere o token e token secret
7. Criar um processo de captura de dados através da API do Twitter, que utilize
os seguintes parâmetros:
a. Palavras a serem pesquisadas: “Boticário” e o nome da linha com mais
vendas no mês 12 de 2019 (conforme item 2.d.);
b. Recuperar os 50 twitts mais recentes;
c. Recuperar apenas twitts que estejam em português.
8. Criar um processo que salve os nomes dos usuários e o texto dos twitts
recuperados em uma tabela do banco de dados.
