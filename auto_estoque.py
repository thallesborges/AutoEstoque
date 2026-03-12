from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from dotenv import load_dotenv
import pandas as pd
import os
import time

load_dotenv()
usuario = os.getenv("USUARIO")
senha = os.getenv("SENHA")
sistema = os.getenv("SISTEMA")
planilha = os.getenv("PLANILHA")

# Abrir o navegador
driver = webdriver.Chrome()
driver.maximize_window()

# Abrir o sistema
driver.get(sistema)

# Fazer login no sistema
driver.find_element("name", "usuario").send_keys(usuario)
driver.find_element("name", "senha").send_keys(senha)
driver.find_element("name", "acao").click()

# Abrir sessão de estoque
driver.find_element("css selector", "img[title='Estoque']").click()

# Fazer login no estoque
select_estoque = Select(driver.find_element("name", "oid_estoque"))
select_estoque.select_by_visible_text("CENTRAL")
driver.find_element("name", "usuario").send_keys(usuario)
campo_senha = driver.find_element("name", "senha")
campo_senha.send_keys(senha)
campo_senha.send_keys(Keys.ENTER)
time.sleep(0.5)
driver.find_element("xpath", "//input[@value='Consumo'][@type='button']").click()

df = pd.read_excel(planilha)
dados = {}

nomes = {
    "Camila": "CAMILA CARINA DE OLIVEIRA",
    "Nita": "JOSCENITA FERREIRA ALVES",
    "Hamilton": "HAMILTON SILVA OLIVEIRA",
    "Idê": "IDE DE SOUZA-17-07-58",
    "Flávia": "TAMAR FLAVIA REZENDE DN. 08/02/73",
    "Rosilene": "ROSILENE PEREIRA FERREIRA 19/12/1976"
}

for _, row in df.iterrows():
    profissional = nomes[row["Profissional"]]
    produto = row["ID"]
    quantidade = row["Quantidade"]

    if profissional not in dados:
        dados[profissional] = []

    dados[profissional].append((produto, quantidade))

select_funcionario = Select(driver.find_element("xpath", "//select[@name='oid_funcionario']"))
for pessoa, produtos in dados.items():
    select_funcionario.select_by_visible_text(pessoa)
    for produto, quantidade in produtos:
        campo_produto = driver.find_element("id", "co")
        campo_produto.send_keys(produto)
        campo_produto.send_keys(Keys.ENTER)
        
        campo_quantidade = driver.find_element("id", "q-1")
        campo_quantidade.send_keys(quantidade)
        campo_quantidade.send_keys(Keys.ENTER)


# Ler o arquivo e separar
## Seleciona profissional
### Por o Código e Quantidade para cada produto e confirmar
#### Ao acabar de um profissional, mudar para o outro e refazer o mesmo processo


