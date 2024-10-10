# PASSO A PASSO DO PROJETO

# Passo 1 - entrar no sistema
# Passo 2 - fazer o login
# Passo 3 - importar a base de dados
# Passo 4 -cadastrar o produto
# Passo 5 - repetir até acabar a lista de produtos


import pyautogui
import time

# pyautogui.write -> escrever um texto
# pyautogui.press -> apertar 1 tecla
# pyautogui.click -> clicar em algum lugar da tela
# pyautogui.hotkey -> combinação de teclas
# pyautogui.scroll -> rolar a tela para cima e para baixo

pyautogui.PAUSE = 0.3

# Passo 1: Entrar no sistema da empresa 
# abrir o navegador (edge)
pyautogui.press("win")
pyautogui.write("edge")
pyautogui.press("enter")


# entrar no link https://dlp.hashtagtreinamentos.com/python/intensivao/login
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
time.sleep(3)


# Passo 2: Fazer login
# selecionar o campo de email
pyautogui.click(x=685, y=451)
pyautogui.hotkey("ctrl","a")#seleciona tudo caso já tenha um outro login escrito
# escrever o seu email
pyautogui.write("loginteste.automacao@gmail.com")
pyautogui.press("tab") # passa pro próximo campo
pyautogui.write("senha1234")
pyautogui.click(x=955, y=638) # clique no botao de login
time.sleep(3)

# Passo 3: Importar a base de produtos pra cadastrar
import pandas as pd

tabela = pd.read_csv("produtos.csv")

print(tabela)

# Passo 4: Cadastrar um produto
for linha in tabela.index:
    # clicar no campo de código
    pyautogui.click(x=653, y=294)

    #pegar da tabela o valor de codigo e transformar em string
    codigo = str(tabela.loc[linha, "codigo"])
    pyautogui.write(codigo)# preencher o campo

    #pegar da tabela o valor de marca e transformar em string
    marca = str(tabela.loc[linha, "marca"])
    pyautogui.press("tab")
    pyautogui.write(marca)

    #pegar da tabela o valor de tipo e transformar em string
    tipo = str(tabela.loc[linha, "tipo"])
    pyautogui.press("tab")
    pyautogui.write(tipo)

    #pegar da tabela o valor de categoria e transformar em string
    categoria = str(tabela.loc[linha, "categoria"])
    pyautogui.press("tab")
    pyautogui.write(categoria)

    #pegar da tabela o valor de preco_unitario e transformar em string
    preco = str(tabela.loc[linha, "preco_unitario"])
    pyautogui.press("tab")
    pyautogui.write(preco)

    #pegar da tabela o valor de custo e transformar em string
    custo = str(tabela.loc[linha, "custo"])
    pyautogui.press("tab")
    pyautogui.write(custo)

    #pegar da tabela o valor de obs e transformar em string
    pyautogui.press("tab")
    obs = str(tabela.loc[linha, "obs"])
    if obs != "nan":#caso o "obs" estiver com valor nulo não será escrito nada
        pyautogui.write(obs)

    
    # clicar no botão de enviar(cadastrar o produto)
    pyautogui.press("tab")
    pyautogui.press("enter") 

    pyautogui.scroll(5000)# dar scroll de tudo pra cima
    # Passo 5: Repetir o processo de cadastro até o fim
