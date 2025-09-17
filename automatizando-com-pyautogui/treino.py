import pyautogui
import time
import pandas as pd

# Abrindo navegador

pyautogui.PAUSE = 0.5 #intervalo para executar cada comando

pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
time.sleep(2)

#Entrar no site

pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
time.sleep(2)

#Fazer login 

pyautogui.click(x=762, y=464)
pyautogui.write("boztentech@gmail.com")
pyautogui.press("tab")
pyautogui.write("naquelepique")
pyautogui.press("enter")

#Importar a base de dados

tabela = pd.read_csv("produtos.csv")
print(tabela)

#Cadastro dos produtos

for linha in tabela.index:
    pyautogui.click(x=659, y=332)
    
    codigo = str(tabela.loc[linha, "codigo"])
    pyautogui.write(codigo)
    pyautogui.press("tab")

    marca = str(tabela.loc[linha, "marca"])
    pyautogui.write(marca)
    pyautogui.press("tab")

    tipo = str(tabela.loc[linha, "tipo"])
    pyautogui.write(tipo)
    pyautogui.press("tab")

    categoria = str(tabela.loc[linha, "categoria"])
    pyautogui.write(categoria)
    pyautogui.press("tab")

    preco_unitario = str(tabela.loc[linha, "preco_unitario"])
    pyautogui.write(preco_unitario)
    pyautogui.press("tab")

    custo = str(tabela.loc[linha, "custo"])
    pyautogui.write(custo)
    pyautogui.press("tab")

    obs = str(tabela.loc[linha, "obs"])

    if obs != "nan":
        pyautogui.write(str(obs))

    pyautogui.press("tab")
    pyautogui.press("enter")
    pyautogui.scroll(9999)


