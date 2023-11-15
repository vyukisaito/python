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

# Desafio 69
adulto = homens = mulher = 0
while True:

    print("=====CADASTRE UMA PESSOA=====")

    idade = int(input('Idade: '))
    if idade >= 18:
         adulto += 1
    sexo = str(input("Sexo [H/M]: ")).strip().upper()[0]
    while sexo not in "HM":
        sexo = str(input("Sexo [H/M]: ")).strip().upper()[0]
    if sexo in "H":
         homens += 1
    if sexo in "M" and idade < 20:
         mulher += 1
    print("="*20)
    continuar = str(input("Quer continuar [S/N]? ")).strip().upper()[0]
    while continuar not in 'SN':
          continuar = str(input("Quer continuar [S/N]? ")).strip().upper()[0]      
    if continuar in 'N':
         break
print("=====FIM DO PROGRAMA=====")
print(f"Ao totao tivemos {adulto} pessoas com mais de 18 anos") 
print(f"Ao todo temos {homens} homens cadastrados")
print(f"Ao todo temos {mulher} mulheres com menos de 20 anos")

# Desagio 70
print("-"*30)
print("{:^30}".format("LOJA"))
print("-"*30)

total = cont =  barato = c = 0
while True:
    produto = str(input("Nome do produtos: ")).strip().lower()
    preco = float(input("Preço: R$"))
    total += preco
    c += 1
    if c == 1:
        barato = preco
        produto_barato = produto
    else:
        if barato > preco:
            produto_barato = produto
            barato = preco
    ctnr = str(input("Quer continuar [S/N]? ")).strip().upper()[0]
    while ctnr not in "SN":
       ctnr = str(input("Quer continuar [S/N]? ")).strip().upper()[0] 
    if preco > 1000:
        cont += 1
    if ctnr in 'N':
        break
print("-----COMRPRA ENCERRADA-----")
print(f"O total da sua compra foi {total:.2f}")
print(f"Temos {cont} produtos com mais de mil reais")
print(f"O produto mais barato foi a(o) {produto_barato} custando {barato}")
'''

# Desafio 71
print("-"*30)
print("{:^30}".format("BANCO VYS"))
print("-"*30)

cinquenta = vinte = dez = um = 0

while True:
    valor = int(input("Qual valor que você quer sacar? "))
    
    cinquenta = valor // 50
    valor %= 50
    
    vinte = valor // 20
    valor %= 20
    
    dez = valor // 10
    valor %= 10
    
    um = valor // 1
    
    break

print(f"Total de {cinquenta} cédula(s) de R$50")
print(f"Total de {vinte} cédula(s) de R$20")
print(f"Total de {dez} cédula(s) de R$10")
print(f"Total de {um} cédula(s) de R$1")
print("VOLTE SEMPRE AO BANCO VYS")
