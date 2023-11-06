'''
# Desafio 46
print("Desafio 46")
from time import sleep
print("Contagem regressiva...")
for c in range(10, 0, -1):
    sleep(1)
    print(c)
# Desafio 47
print("Números pares")
for i in range(2, 51, 2):
    print(i, end=' ')

# Desafio 48
cont = 0
soma = 0
for i in range(1, 501, 2):
    if i % 3 == 0:
        cont = cont + 1
        soma += i
print("A soma é {} de todos os {} valores" .format(soma, cont))
''' 
# Desafio 49
num = int(input("Digite um numero inteiro: "))
for i in range(1, 11):
    print("{} x {} = {}" .format(i, num, num * i))