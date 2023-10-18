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
print('Seu último nome é {}' .format(nome[len(nome) -1 ]))