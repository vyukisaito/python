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
