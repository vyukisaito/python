import pyautogui
import time

pyautogui.PAUSE = 1


pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('enter')
pyautogui.click(x=324, y=770)
pyautogui.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')

pyautogui.press('enter')
time.sleep(3)

#pyautogui.click(x=1274, y=27)
pyautogui.click(x=717, y=364)

pyautogui.write('gmail')
pyautogui.press('tab')
pyautogui.write('suasenha')
pyautogui.press('tab')

pyautogui.press('enter')
time.sleep(3)


import pandas as pd

tabela = pd.read_csv("produtos.csv")


for linha in tabela.index:
    pyautogui.click(x=686, y=237)
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(str(codigo))
    pyautogui.press('tab')

    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press('tab')

    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press('tab')

    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press('tab')

    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press('tab')

    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press('tab')

    obs = tabela.loc[linha, "obs"]
    if not pd.isna(obs): 
        pyautogui.write(str(tabela.loc[linha, "obs"]))
    pyautogui.press('tab')
    pyautogui.press('enter')

    pyautogui.scroll(5000)