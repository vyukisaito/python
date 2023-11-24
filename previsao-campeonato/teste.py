import pandas as pd
import requests

requisicao = requests.get('https://pt.wikipedia.org/wiki/Campeonato_Brasileiro_de_Futebol_de_2023_-_S%C3%A9rie_A')

tabelas = pd.read_html(requisicao.text)
print(tabelas)