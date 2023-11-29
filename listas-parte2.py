'''
teste = list()
teste.append('Gustavo')
teste.append(40)
galera = list()
galera.append(teste[:])
teste[0] = "Yuki"
teste[1] = 15
galera.append(teste[:])
print(galera)
pessoas = [['Yuki', 15, 2], ['Gustavo', 23], ['Ana', 12]]
print(pessoas[0][1])

for i in pessoas:
    print(f'{i[0]} tem {i[1]} anos de idaide')

dados = list()
pessoas = list()
for i in range(3):
    dados.append(str(input("Qual o seu nome? ")))
    dados.append(int(input("Qual a sua idade? ")))
    pessoas.append(dados[:])
    dados.clear()
print(pessoas)
for i in pessoas:
    if i[1] >= 18:
        print(f'{i[0]} é maior de idade')
    else:
        print(f'{i[0]} é menor de idade')

# Desagio 84
dados = list()
pessoas = list()
maior = menor = 0
while True:
    dados.append(str(input("Nome:  ")))
    dados.append(float(input("Peso: ")))
    if len(pessoas) == 0:
        maior = menor = dados[1]
    else:
        if maior < dados[1]:
            maior = dados[1]
        if menor > dados[1]:
            menor = dados[1]
    pessoas.append(dados[:])
    dados.clear()
    resp = str(input("Quer continar? ")).strip().upper()[0]
    if resp in 'N':
        break

print(f'Ao todo você cadastrou {len(pessoas)} pessoas')
print(f"O maior peso foi de {maior}KG. Peso de ", end='')
for i in pessoas:
    if i[1] == maior:
        print(f'{i[0]} ', end='')
print('')
print(f"O menor peso foi de {menor}KG. Peso de ", end='')
for i in pessoas:
    if i[1] == menor:
        print(f"{i[0]} ", end='')

# Desafio 85
num = [[], []]
valor = 0
for i in range(1, 8):
    valor = int(input(f"Digite o {i}o valor: "))
    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)
print(f"Os valores pares digitados foram: {num[0]}")
print(f"Os valores impares digitados foram: {num[1]}")

# Desafio 86 e 87
num = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
par = soma = teceira = maior = 0
for l in range(0, 3):
    for c in range(0, 3):
        num[l][c] = int(input(f"Digite um número na posição [{l}, {c}]: "))

for l in range(0, 3):
    for c in range(0, 3):
        print(f"[{num[l][c]:^5}]", end='')
        if num[l][c] % 2 == 0:
            par += 1
            if par == 1:
                soma = num[l][c]
            else:
                soma += num[l][c]
        
        for i in range(0, 3):
            if i == 0:
                maior = num[1][i]
                terceira = num[i][2]
            else:
                terceira += num[i][2]
                if maior < num[1][i]:
                    maior = num[1][i]

    print()
print(f"A soma dos valores pares é {soma}")
print(f"A soma dos valores da terceira coluna é {terceira}")
print(f"O maior valor da segunda linha é {maior}")

# Desafio 88
from random import randint
from time import sleep
print('SORTEADOR'.center(30))
lista = [[], [], [], [], [], []]
jogos = int(input("Quantos jogos você quer que eu sorteie? "))
for i in range(1, jogos+1):
    for c in range(0,6):
        if c == 0:
            lista[c] = randint(1, 60)
        else:
            while True:
                if lista[c] == lista[c-1]:
                    lista[c] = randint(1, 60)
                else:
                    lista[c] = randint(1, 60)
                    break
    lista.sort()
    print(f"Jogo {i}:  {lista}")
    lista = [[], [], [], [], [], []]
    sleep(1)
'''

aluno = [ ['caio',[12]], ['Maria',[12]] ]
teste = ['caio',[23]]
aluno.append(teste)
print(aluno)
