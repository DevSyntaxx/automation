import pyautogui
import time 

#21 96721-8715
#ffpyautogui.click => clicar com mouse
#pyautogui.press => pressionar uma tecla do teclado
#pyautogui.write => Escrever um texto
#pyautogui.hotkey => apertar conjunto de teclas
pyautogui.PAUSE =0.5
 
#abrir o navegador
pyautogui.press("win")
pyautogui.write("Edge")
pyautogui.press("Enter")

#Entrar no sistema
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
time.sleep(2)   #pausa o código pelo tempo determinado na linha escolhida

#fazer login
pyautogui.click(x=2038, y=343)
pyautogui.write("danjherstudio@gmail.com")
pyautogui.press("tab")
pyautogui.write ("84846437")
pyautogui.press("tab")
pyautogui.press("enter")

time.sleep(1)

#abrir e importar base de dados
import pandas as pd

#ler e salvar informações
tabela = pd.read_csv("produtos.csv")

#cadastrar um produto

for linha in tabela.index:
    

    codigo = str (tabela.loc[linha, "codigo"])

    #clicar no campo de código do produto
    pyautogui.click (x=1863, y=252)
    #preencher o campo do código
    pyautogui.write(str(tabela.loc[linha, "codigo"]))
    #passar pro proximo campo
    pyautogui.press("tab")
    #preencher marca
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")
    #tipo
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")
    #categoria
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    #preço
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    #custo
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    #obs
    obs = (str(tabela.loc[linha, "obs"]))
    if obs != "nan":
        pyautogui.write(obs)
    pyautogui.press("tab")
    #apertar o botão
    pyautogui.press("enter")
    #scrool pra cima
    pyautogui.scroll(5000)