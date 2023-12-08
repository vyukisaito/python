''''
lanche = ("sorvete", 'hamburguer','z', 'suco', 'pizza')
for i in lanche:
    print(f'{i}')

print('')

for pos, comida in enumerate(lanche):
    print(f'Eu comi {comida} na posicao {pos}')

print('')

for cont in range(0, len(lanche)):
    print(f"comi {lanche[cont]} na posicao {cont}")

print('')
print(lanche[0:])
print(lanche[:2])
print('')

print(sorted(lanche))

a = (2,5,4)
b = (9,6,7,5)
c = a + b
print(c.count(9))
print(c.index(5)) # em que posicao esta o 5
print(c.index(5, 2)) # nesse caso ele vai comecar a contar a partir da posicao 2
del(c) # deleta o c

# Desafio 72    
num = int(input("Digite um número entre 0 e 20: "))
tupla = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while num < 0 or num > 20:
    num = int(input("Tente novamente. Digite um número entre 0 e 20: "))
print(f"Você digitou o número {tupla[num]}")

# Desafio 73
brasileirao = ('Palmeiras', 'Botafogo', 'Grêmio', 'RB Bragantino', 'Atlético-MG', 'Flamengo', 'Athletico-PR', 'Fluminensem', 'Cuiabá', 'São Paulo', 'Corinthians', 'Fortaleza', 'Internacional', 'Santos', 'Vasco', 'Bahia', 'Cruzeiro', 'Goiás', 'Coritiba', 'América-MG')

c = 0
print("A lista do Brasileirão está assim: ")
for i in brasileirao:
    c += 1
    print(f"{c} - {i}")

print(" ")

print(f"Os cinco primeiros colocados do Brasileirao são: ")
for i in range(-1, 4):
    i += 1
    print(f"{i+1} - {brasileirao[i]}")
# print(f"Os cinco primeiros colocados do Brasileirao são: {brasileira[:5]}") ou fazer assim, que fica feio

print('')

print("Os que estão no z4 são: ")
for i in range(15, 19):
    i += 1
    print(f"{i+1} - {brasileirao[i]}")

print("")
print(f"Aqui está a lista em ordem Alfabética: {sorted(brasileirao)}")
print("")

sp =  brasileirao.index('São Paulo') + 1
print(f"O Time São Paulo esta na {sp} posição")

# Desafio 74
import random
maior = menor = cont =0
numeros = (random.randint(1, 10), random.randint(1, 10), random.randint(1, 10), random.randint(1, 10), random.randint(1, 10))
print(f"Os valores sorteados foram: ", end='')
for i in numeros:
    print(f'{i}, ', end="")
for i in numeros:
    cont += 1
    if cont == 1:
        maior = i
        menor = i
    else:
        if maior < i:
            maior = i
        if menor > i:
            menor = i
print(f"\nO maior número foi {max(numeros)} e o menor foi {min(numeros)}")

# Desafi 75:
num = (int(input("Digite um número: ")), int(input("Digite um número: ")), int(input("Digite mais um número: ")), int(input("Digite o ultimo número: ")))
print(f"Os número digitados foram: {num}")

if 9 in num:
    print(f"O número 9 apareceu {num.count(9)}")
else:
    print("O número 9 nao apareceu nenhuma vez")
if 3 in num:
    print(f"O primeiro valor 3 foi digitado na posiçao {num.index(3)+1}\n")
else:
    print(("O número 3 não aprece nenhuma vez \n"))

print(f'O(s) número(s) par(es) são: ', end="")
for i in num:
    if i % 2 == 0:
        par = i
        print(i, end=" ")

# Desafio 76
produtos = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 23.75, 'Mochila', 123.43)
for pos in range(0, len(produtos)):
    if pos % 2 == 0:
        print(f'{produtos[pos]:.<30}', end="")
    else: 
        print(f'R${produtos[pos]:>6.2f}')
'''

# Desafio 77:
palavras = ('Palmeiras', 'Botafogo', 'Grêmio', 'Bragantino', 'Flamengo', 'Athletico', 'Fluminensem', 'Corinthians', 'Fortaleza', 'Internacional', 'Santos', 'Vasco', 'Bahia', 'Cruzeiro',  'Coritiba')
for i in palavras:
    print(f'\nNa palavra {i.upper()} temos: ', end="")
    for palavras in i:
        if palavras.lower() in 'aeiou':
            print(palavras, end=" ")
