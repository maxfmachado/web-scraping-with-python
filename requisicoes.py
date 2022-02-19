import pandas as pd
import json
from selenium import webdriver
from datetime import date, datetime

driver = webdriver.Chrome()
nomes = []
lista_com_nome_e_data = []
url_base = 'https://www.google.com/search?q=data+nascimento+'

# Abrindo e lendo o arquivo json para extrair somente os nomes para a pesquisa:
with open("web-scraping\dados.json", encoding='utf-8') as dados_json:
    dados = json.load(dados_json)

for i in dados:
    nomes.append(i['nome'])

# Fazendo a pesquisa da data de nascimento a partir da lista de nomes extraida acima e montando o arquivo excel 
# com as colunas 'Nome' e 'Data_Nascimento':
for nome in nomes:
    driver.get(url_base + nome)
    data = driver.find_element_by_xpath("//div[@data-attrid='kc:/people/person:date of birth']/div/div").text
    data_formatada = data.replace("de", "/").replace(" ", "")
    
    lista_com_nome_e_data.append([nome, data_formatada])

driver.close()

datas = pd.DataFrame(lista_com_nome_e_data, columns=['Nome', 'Data_Nascimento'])
print(datas)
# datas.to_excel('lista_com_datas_nascimento.xlsx')