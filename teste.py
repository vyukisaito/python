# Desafio 74
import random
maior = menor = 0
numeros = (random.randint(1, 10), random.randint(1, 10), random.randint(1, 10), random.randint(1, 10), random.randint(1, 10))
print(f"Os valores sorteados foram: {numeros}")
for i in numeros:
    maior = i
    menor = i
    if maior < i:
        maior = i
    if menor > i:
        menor = i
print(f"O maior número foi {maior} e o menor foi {menor}")