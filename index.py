# Teste de commit

# Importando a biblioteca Pandas nomeando como 'pd"
import pandas as pd 
# Importando da biblioteca Selenium alguns comando
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


# Para o Selenium funcionar precisamos "abrir" o chrome para nós puxarmos os dados da URL
service = Service() # Comando para iniciar uma intancia do Chrome WebDriver
options = webdriver.ChromeOptions() # Definição de preferencia para o browser do Chrome
driver = webdriver.Chrome(service=service, options=options) # Inicia a instancia do Chrome WebDriver

url = "https://steamdb.info/charts/" # URL que estou pegando os dados

driver.get(url) # Solicitando para abrir o navegador com a URL imposta

#Definindo uma variavel para buscar os titulos do jogo e o pico de jogadores que já teve
nameGames = driver.find_elements(By.TAG_NAME, 'td')[2:72:7]
PeakGame = driver.find_elements(By.TAG_NAME, 'td')[5:75:7]

# Definindo duas listas
name = []
Peak = []


# Pegando cada item e colocando na sua devida lista
for n in nameGames:
    name.append(n.text)

for N in PeakGame:
    Peak.append(N.text)

# Definindo uma Data Frame
dicDF = {'title': name,
         'All Peak': Peak}

# Exibindo o Data Frame com o Pandas 
print(pd.DataFrame(dicDF))
