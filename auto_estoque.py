from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from dotenv import load_dotenv
import os
import time

load_dotenv()
usuario = os.getenv("USUARIO")
senha = os.getenv("SENHA")
sistema = os.getenv("SISTEMA")

# Abrir o navegador
driver = webdriver.Chrome()
time.sleep(3)
driver.maximize_window()

# Abrir o sistema
driver.get(sistema)
time.sleep(3)

# Fazer login no sistema
driver.find_element("name", "usuario").send_keys(usuario)
time.sleep(1)
driver.find_element("name", "senha").send_keys(senha)
time.sleep(1)
driver.find_element("name", "acao").click()

# Abrir sessão de estoque
driver.find_element("css selector", "img[title='Estoque']").click()
time.sleep(1)

# Fazer login no estoque
select_estoque = Select(driver.find_element("name", "oid_estoque"))
time.sleep(1)
select_estoque.select_by_visible_text("CENTRAL")
time.sleep(1)
driver.find_element("name", "usuario").send_keys(usuario)
time.sleep(1)
campo_senha = driver.find_element("name", "senha")
campo_senha.send_keys(senha)
time.sleep(0.5)
campo_senha.send_keys(Keys.ENTER)
time.sleep(1)
driver.find_element("xpath", "//input[@value='Consumo'][@type='button']").click()
time.sleep(5)

# Ler o arquivo e separar
## Seleciona profissional
### Por o Código e Quantidade para cada produto e confirmar
#### Ao acabar de um profissional, mudar para o outro e refazer o mesmo processo


