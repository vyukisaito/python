#DESAFIO 025
print('Desafio 025')
name = str(input('Digite seu nome completo: ')).strip()
print('Seu nome tem Silva? {}\n' .format('silva' in name.lower()))

#DESAFIO 026
print('Desafio 026')
frase = str(input('Digite alguma coisa: ')).lower().strip()
print('A letra A aparece {} vezes na frase' .format(frase.count('a')))
print('A primeira letra A apareceu na posição {}' .format(frase.find('a')+1))
print('A ultima letra A apareceu na posição {}\n' .format(frase.rfind('a')+1))

#DESAFIO 026
print('Desafio 026')
n = str(input('Digite seu nome completo: ')).strip()
nome = n.split()
print('Seu primeiro nome é {}' .format(nome[0]))
print('Seu último nome é {}\n' .format(nome[len(nome) -1 ]))

#DESAFIO 028
print('Desafio 028')
import random
lista = [0, 1, 2, 3, 4, 5]
num = random.choice(lista)
res = int(input('Escolha um número entre 0 a 5: '))
if res == num:
    print('Parabéns era o número {} \n' .format(res))
elif res > 5 :
    print('São números entre 0 a 5\n')
else: 
    print('VENCI! Eu pensei no número {} e você no {} \n' .format(num, res))

#DESAFIO 029
print('Desafio 029')
velocidade = int(input('Qauntos KM você está correndo? '))
if velocidade > 80:
    print('Você está andando {}KM a mais, a sua multa será: R${:.2f} \n' .format(velocidade-80, (velocidade-80)*7))
else: print('Parabéns! Você está andando na velocidade adequada \n ')

#DESAFIO 030
print('Desafio 030')
numero = int(input('Escreva um número inteiro: '))
if numero % 2 == 0:
    print('O número é par \n')
else:
    print('O número é impar \n')

#DESAFIO 031
print('Desafio 031')
distancia = int(input('Qual a distância da sua viagem? '))
if distancia < 201:
    print('O preço para essa viagem será R${}\n' .format(distancia*0.50))
else:
    print('A sua viagem irá custar R${}\n' .format(distancia*0.45))

#DESAFIO 032
print('Desafio 032')
ano = int(input('Digite um ano: '))
if (ano%4 == 0 and ano%100!=0) or (ano%400==0):
    print('O ano é bissexto\n')
else: 
    print('O ano não é bissexto\n')
