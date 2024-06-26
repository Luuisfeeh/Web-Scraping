# importando a biblioteca Psycopg2 
import psycopg2
from sqlalchemy import create_engine
# Importando a biblioteca Pandas nomeando como 'pd"
import pandas as pd 
# Importando da biblioteca Selenium alguns comando
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
# Importante a libs Datetime
import datetime

# definindo uma variavel para a data atual
Atual = datetime.datetime.today().strftime("%d-%m-%y")

#Definindo uma conxão com o Servidor Local no Dbeaver e criando um cursor
host='localhost'
port='5432'
dbname='postgres'
user='postgres'
password='Lua20022020%'

Connection = f'postgresql://{user}:{password}@{host}:{port}/{dbname}'
Connection1 = psycopg2.connect(host=host,
                               port=port ,
                               database=dbname,
                               user=user,
                               password=password)

conexao = create_engine(Connection)
cur = Connection1.cursor()

# Para o Selenium funcionar precisamos "abrir" o chrome para nós puxarmos os dados da URL
service = Service() # Comando para iniciar uma intancia do Chrome WebDriver
options = webdriver.ChromeOptions() # Definição de preferencia para o browser do Chrome
driver = webdriver.Chrome(service=service, options=options) # Inicia a instancia do Chrome WebDriver

url = "https://steamdb.info/sales/" # URL que estou pegando os dados

driver.get(url) # Solicitando para abrir o navegador com a URL imposta

'''
*ESSE TRECHO DO CÓDIGO É UMA FORMA DE ARMAZENAR OS DADOS DE UM OUTRO URL E EXIBIR EM UM DATAFRAME*
Definindo uma variavel para buscar os titulos do jogo e o pico de jogadores que já teve
nameGames = driver.find_elements(By.TAG_NAME, 'td')[2:72:7]
PeakGame = driver.find_elements(By.TAG_NAME, 'td')[5:75:7]

 Definindo duas listas
name = []
Peak = []


 Pegando cada item e colocando na sua devida lista
for n in nameGames:
    name.append(n.text)

for N in PeakGame:
    Peak.append(N.text)

 Definindo uma Data Frame
dicDF = {'title': name,
         'All Peak': Peak}

 Exibindo o Data Frame com o Pandas 
print(pd.DataFrame(dicDF))
'''

# A classe com o nome "b" puxa o nome dos jogos a partir do 0
NameGame = driver.find_elements(By.CLASS_NAME, "b")[0:10:1]
RankGame = driver.find_elements(By.CLASS_NAME, 'dt-type-numeric')[8:78:7]
PriceGame = driver.find_elements(By.CLASS_NAME, 'dt-type-numeric')[9:79:7]
RatingGame = driver.find_elements(By.CLASS_NAME, 'dt-type-numeric')[10:80:7]
RealeaseGame = driver.find_elements(By.CLASS_NAME, 'dt-type-numeric')[11:81:7]

nomes = []
rank = []
price = []
rating = []
realease = []


tabela = '"DataBase".tabela'
Nome = '"Name"'



for i in NameGame:
    nomes.append(i.text)

for i in RankGame:
    rank.append(i.text)

for i in PriceGame:
    price.append(i.text)

for i in RatingGame:
    rating.append(i.text)

for i in RealeaseGame:
    realease.append(i.text)



Dframe = {'Name': nomes,
          'Porcentagem': rank,
          'Price': price,
          'Rating': rating,
          'Realease': realease}


DataF = pd.DataFrame(Dframe)



# Método no qual cria uma tabela e para que haja atualixação o execute elimina a tabela atual e cria novamente uma mais recente
'''
cur.execute('drop table "Tabela_de_Infos" ')
Connection1.close()
DataF.to_sql('Tabela_de_Infos',conexao, schema='DataBase', index=False)
'''

# Método que cria uma tabela com a data atual da atualização
DataF.to_sql("Tabela_de_Infos_"+Atual,conexao, schema='DataBase', index=False)



