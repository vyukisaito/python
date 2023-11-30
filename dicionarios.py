'''
pessoas = {'nome': 'Gustavo', 'time': 'Botafogo', 'idade': 22}
print(f'O {pessoas["nome"]} torce para o {pessoas["time"]}')
print(pessoas.keys(), pessoas.values(), pessoas.items())
for k in pessoas.keys():
    print(k)
for v in pessoas.values():
    print(v)
for k, v in pessoas.items():
    print(f'{k} = {v}')

brasil= list()
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)
print(brasil)
print(brasil[0]['uf'])

pessoa = dict()
dados = list()
for i in range(0, 3):
    pessoa['nome'] = str(input("Nome: "))
    pessoa['idade'] = int(input("Idade: "))
    dados.append(pessoa.copy())
print(dados)
for i in dados:
    for v in i.values():
        print(v)
'''

# Desafio 90
pessoa = dict()
pessoa['nome'] = str(input("Nome: "))
pessoa['media'] = int(input(f"Média de {pessoa['nome']}: "))
print(f"Nome é {pessoa['nome']}")
print(f"Média é igual a {pessoa['media']}")
if pessoa['media'] >= 7:
    print("Situação atual aprovado")
else:
    print("Situação atua desaprovado")
