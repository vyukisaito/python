'''
import random
num = [1, 4, 5, 2]
num.append(9)
num[3] = 4
num.sort(reverse=True)
num.remove(4)
print(num)
print(f'A lista tem {len(num)} elementos')

a = [2, 5, 6, 1]
b = a[:]
b[2] = 8
print(a)
print(b)

valores = []
for i in range(0, 5):
    valores.append(int(input("Digite um valor: ")))
for c, v in enumerate(valores):
    print(f'Na posição {c} tivemos o valor {v}!')


# Desafio 78
valores = []
maior = menor = 0
pos_maior = pos_menor = 0
for i in range(0, 6):
    valores.append(int(input(f"Digite um valor na posição {i}: ")))
    if i == 0:
        maior = valores[i]
        menor = valores[i]
    else:
        if maior < valores[i]:
            maior = valores[i]
            pos_maior = i
        if menor > valores[i]:
            menor = valores[i]
            pos_menor = i

print(f"Você digitou os valores {valores}")
print(f"O maior valor digitado foi {maior} nas posições ",end='')
for c, v in enumerate(valores):
    if v == maior:
        print(f'{c}...', end=' ')
print('')
print(f"O menor valor digitado foi {menor} nas posições ", end='')
for c, v in enumerate(valores):
    if v == menor:
        print(f'{c}...', end=' ')

# Desafio 79
numeros = list()
while True:
    n = int(input("Digite um valor: "))
    if n not in numeros:
        print("Valor adicionado com sucesso...")
        numeros.append(n)
    else:
        print("Esse valor é duplicado...")
    continuar = str(input("Quer continuar [S/N]? ")).strip().upper()[0]
    if continuar in 'N':
        break
numeros.sort()
print(f"Você digitou os valores: {numeros}")
'''

# Desafio 80
num = list()
n1 = 0
for i in range(0, 5):
    n = int(input("Digite um valor: "))
    

