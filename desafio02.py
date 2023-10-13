import math
#DESAFIO 016
print('Desafio 016')
num = float(input('Digite um número: '))
nume = math.floor(num)
print('O número {} tem a parte Inteira {}\n' .format(num, nume))

#DESAFIO 017
print('Desafio 017')
co = float(input('Digite um cateto oposto: '))
ca = float(input('Agora digite um cateto adjacente: '))
#hi = (co**2 + ca**2)**(1/2)
#essa é uma das maneiras
hi = math.hypot(co, ca)
print('A hipotenusa vai medir {:.2f}\n' .format(hi))

#DESAFIO 018
print('Desafio 018')
angulo = float(input('Digite um ângulo qualquer: '))
sen = math.sin(math.radians(angulo))
print('O ângulo de {} tem o SENO de {}' .format(angulo, sen))
cos = math.cos(math.radians(angulo))
print('O ângulo de {} tem o COSSENO de {}' .format(angulo, cos))
tan = math.tan(math.radians(angulo))
print('O ângulo de {} tem o TANGENTE de {}\n' .format(angulo, tan))

#DESAFIO 019
print('Desafio 019')
import random
um = str(input('Primeiro aluno: '))
dois = str(input('Segundo aluno: '))
tres = str(input('Terceiro aluno: '))
quatro = str(input('Quarto aluno: '))
cinco = str(input('Quinto aluno: '))
lista = [um , dois, tres, quatro, cinco]
sorteio = random.choice(lista)
print('O Aluno escolhido foi: {}\n' .format(sorteio))

#DESAFIO 020
print('Desafio 020')
n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))
n5 = cinco = str(input('Quinto aluno: '))
lista2 = [n1, n2, n3, n4, n5]
random.shuffle(lista2)
print('Essa será a ordem de apresentação: {}\n' .format(lista2))

#DESAFIO 021
print('Desafio 021\n')

# visitar a pasta teste

#DESAFIO 022
print('Desafio 022')
nome = input('Digite se nome completo: ')
print('Seu nome em maisculas é: {}' .format(nome.upper()))
print('Seu nome em minusculas é: {}' .format(nome.lower()))
print('Seu nome tem ao todo:', (len(nome) - nome.count(' ')))
print('Seu primeiro nome tem {} letras' .format(nome.find(' ')))
