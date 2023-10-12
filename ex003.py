'''
import math
num = int(input('Digite um número: '))
raiz = math.sqrt(num)
print(raiz)

import random
print(random.randint(1, 6))
'''


frase = 'São Paulo Maior Clube'
print(frase[3]) # vai printar a quarta letra
print(frase[3:13]) # vai da quarta letra até a 13
print(frase[::2]) # vai saltar de duas em duas letras
print(frase.count('o')) # vai contar quanto 'o' tem
print(len(frase)) # vai contar quantos caracter tem contando com espaço
frase = frase.replace('Clube', 'Seleção')
print(frase)