# Desafio 66
'''
n = s = c = 0
while True:
    n = int(input("Digite um número "))
    if n == 999:
        break
    s += n
    c += 1
print(f"A soma dos {c} valores são: {s}")

# Desafio 67
while True:
    n = int(input("Quer ver qual tabuada de qual valoe? "))
    if n < 0:
        break
    for i in range(1, 11):
        print(f"{n} x {i} = {n*i}")
print("Programa tabuada encerrado")
'''

# Desafio 68
from random import randint
from time import sleep
jogador = vitoria  = computador = 0
while True:
    computador = randint(1, 30)
    jogador = int(input("Diga um valor: "))
    par_impar = str(input("Par ou Impar [P/I]? ")).strip().upper()[0]
    if (jogador + computador) % 2 == 0 and par_impar in 'P':
        print(f"Você jogou {jogador} e o computador jogou {computador}. Total deu {jogador + computador}. DEU PAR")
        print("VOCÊ VENCEU!")
        print("Vamos jogar novamente...")
        print('-=-'*30)
        sleep(2)
        vitoria += 1
    elif (jogador + computador) % 2 != 0 and par_impar in 'I':
        print(f"Você jogou {jogador} e o computador jogou {computador}. Total deu {jogador + computador}. DEU IMPAR")
        print("VOCÊ VENCEU!")
        print("Vamos jogar novamente...")
        print('-=-'*30)
        sleep(2)
        vitoria += 1
    elif (jogador + computador) % 2 == 0 and par_impar in 'I':
        print(f"Você jogou {jogador} e o computador jogou {computador}. Total deu {jogador + computador}. DEU PAR")
        print(f"GAME OVER! Você venceu {vitoria} vezes")
        jdn = str(input("Quer jogar de novo [S/N]? ")).strip().upper()[0]
        if jdn in 'N':
            break
    elif (jogador + computador) % 2 != 0 and par_impar in 'P':
        print(f"Você jogou {jogador} e o computador jogou {computador}. Total deu {jogador + computador}. DEU IMPAR")
        print(f"GAME OVER! Você venceu {vitoria} vezes")
        jdn = str(input("Quer jogar de novo [S/N]? ")).strip().upper()[0]
        if jdn in 'N':
            break
print("Jogo finalizado")
           