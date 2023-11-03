# DESAFIO 045
import random
print('Desafio 045')
print('''SUAS OPÇÕES:
[0] PEDRA
[1] PAPEL
[2] TESOURA
''')
jogada = int(input("Qual a sua jogada? "))
lista = ["Pedra", "Papel", "Tesoura"]
computador = random.choice(lista)

if jogada == 0:
    gon = 'Pedra'
elif jogada == 1:
    gon = 'Papel'
elif jogada == 2:
    gon = 'Tesoura'


print('=-='*10)
print('Computador jogou {}' .format(computador))
print('O jogador jogou {}' .format(gon))
print('=-='*10)

if gon == computador:
    print("EMPATE")
elif jogada == 0:
    gon = 'Pedra'
    if gon == 'Pedra' and computador == 'Papel':
        print("Computador venceu")
    elif gon == 'Pedra' and computador == 'Tesoura':
        print("JOGADOR VENCEU")
elif jogada == 1:
    gon = 'Papel'
    if gon == 'Papel'and computador == 'Tesoura':
        print("Computador venceu")
    elif gon == 'Papel' and computador == 'Pedra':
        print("jogador venceu")
elif jogada == 2:
    gon = 'Tesoura'
    if gon == 'Tesoura'and computador == 'Pedra':
        print("Computador venceu")
    elif gon == 'Tesoura' and computador == "Papel":
        print("Jogador venceu")
    else:
        print("Opcao invalida")


