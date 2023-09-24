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
print('O Aluno escolhido foi: {}' .format(sorteio))

