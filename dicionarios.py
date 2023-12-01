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


# Desafio 91
from random import randint
from time import sleep
from operator import itemgetter
jogo = {'jogador1': randint(1, 6),
        'jogador2': randint(1, 6),
        'jogador3': randint(1, 6),
        'jogador4': randint(1, 6)}
ranking = list()
for k, v in jogo.items():
    print(f"{k} tirou {v} no dado.")
    #sleep(1)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print(ranking[1])
for i, v in enumerate(ranking):
    print(f"{i+1}o Lugar: {v[0]} com {v[1]} ")

# Desafio 92
from datetime import date
dados = dict()
dados['nome'] = str(input("Nome: "))
ano = int(input("Ano de nascimento: "))
dados['idade'] = date.today().year - ano
carteira = int(input("Carteira de Trabalho (0 não tem): "))
if carteira == 0:
    for k, v in dados.items():
        print(f'{k} tem valor {v}')
else:
    dados['ctps']= carteira
    dados['contratação'] = int(input("Ano de Contratação: "))
    dados['salário'] = float(input("Salário: R$"))
    aposentadoria = dados['contratação'] + 35 - date.today().year + dados['idade']
    dados['aposentadoria'] = aposentadoria
    for k, v in dados.items():
        print(f"{k} tem o valor de {v}")

# Desafio 93
jogador = dict()
gols = list()
soma = 0
jogador['nome'] = str(input("Nome: "))
partidas = int(input(f"Quantas partidas {jogador['nome']} fez? "))
for i in range(1, partidas+1):
    gol = int(input(f'Quantos gol {jogador["nome"]} fez na {i} partida? '))
    if i == 1:
        soma = gol
    else:
        soma += gol
    gols.append(gol)
jogador['gols'] = gols
jogador['total'] = soma
print()
print(jogador)
print()
for k, v in jogador.items():
    print(f'No campo {k} tem o valor {v}')
print()
print(f"O jogador {jogador['nome']} fez {partidas} partidas")
for i in range(1, partidas+1):
    if i == partidas:
        i +=1
        print(f"   => Na partida {i-1}, fez {gols[i-2]}")
    else:
       print(f"   => Na partida {i}, fez {gols[i-1]}")
media = jogador['total'] / partidas
print(f"Foi um total de {jogador['total']} gols em {partidas} partidas. Média de {media:.1f} gol(s) por jogo.")

# Desafio 94
galera = list()
pessoa = dict()
media = 0
soma = 0
while True:
    pessoa['nome'] = str(input("Nome: "))
    while True:
        pessoa['sexo'] = str(input("Sexo: [M/F] ")).strip().upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print("Valor incorrto. Apenas M ou F")
    pessoa['idade'] = int(input("Idade: "))
    galera.append(pessoa.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if resp in 'S':
            break
        if resp in 'N':
            break
    if resp in 'N':
        break
print()
print(f'- O grupo tem {len(galera)} pessoas')
#print(galera[0]['idade'])
for i in range(0, len(galera)):
    if i == 0:
        soma = galera[i]['idade']
    else: 
        soma += galera[i]['idade'] 
media = soma / len(galera)
print(f"A média de idade é de {media} anos")
print("As mulheres cadastradas são: ", end='')
for i in range(0, len(galera)):
    if galera[i]['sexo'] in 'F':
        print(f"{galera[i]['nome']} ", end='')
print()
print("Listas das pessoas que estão acima da média: ")
for i in range(0, len(galera)):
    if galera[i]['idade'] > media:
        print(f"Nome = {galera[i]['nome']}; idade = {galera[i]['idade']}; sexo = {galera[i]['sexo']}")
'''

# Desafio 95
jogadores = list()
jogador = dict()
gols = list()
soma = 0
while True:
    jogador['nome'] = str(input("Nome: "))
    partidas = int(input(f"Quantas partidas {jogador['nome']} fez? "))
    for i in range(1, partidas+1):
        gol = int(input(f'Quantos gol {jogador["nome"]} fez na {i} partida? '))
        if i == 1:
            soma = gol
        else:
            soma += gol
        gols.append(gol)
    jogador['gols'] = gols
    jogador['total'] = soma
    jogadores.append(jogador.copy())
    gols = []
    gol = 0
    resp = str(input("Quer continuar? ")).strip().upper()[0]
    if resp in 'N':
        break

print(f'cod {"nome":<9}{"gols":<13}total')
print('-------------------------------------------------------------------')
for i in range(0, len(jogadores)):
    print(f"{i} {jogadores[i]['nome']:<10}{jogadores[i]['gols']:<10}{jogadores[i]['total']}")
print('-------------------------------------------------------------------')
while True:
    while True:
        mostrar = int(input("Mostra dados de qual jogador?(999 para parar) "))
        if mostrar == 999:
            break
        if mostrar > len(jogadores) - 1 or mostrar < 0:
            print("Valor não esta na lista. Tente novamente! ")
        else:
            break
    if mostrar == 999:
        break
    print(f'-- DADOS DO JOGADOR {jogadores[mostrar]["nome"]}: ')
    for i in range(0, partidas+1):
        if i == partidas:
            i += partidas
            print(f"  Na partida {i-1}, fez {jogadores[i-2]['gols']}")
        else:
            print(f"  Na partida {i}, fez {jogadores[i-1]['gols']}")
            



