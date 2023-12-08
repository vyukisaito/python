#nome = input('Qual o seu nome? ')
#print('Prazer em te conhecer', nome)

#nome2 = input('Digite sua idade:')
#print('Você possui {} anos!'.format(nome2))


'''
n1 = int(input('Digite um número: '))
n2 = int(input('Digite mais um número: '))
s = n1 + n2
print('A soma entre {} e {} vale {}' .format(n1, n2, s))

n3 = input('Digite outro número: ')
print(type(n3))
print(type(int(-23)))
print(type(True))
print(type(3.56))

# n = bool(input('Digte um número: '))
#print(n)
# Se eu respoder com algo vai dar True, se nada vai ser False
'''


n = input('Digte algo: ')
print('O tipo primitivo é:' ,type(n))
print('é um número:' ,n.isnumeric())
print('é uma letra:',n.isalpha())
print('está só com letra maisculua?:',n.isupper())
print('está em letra minuscula?:' ,n.islower())
print('é um espaço:', n.isspace())
print('é um número deciaml:', n.isdecimal())
# checar depois

nombre = input('Qual o seu nome? ')
print('Prazer em te conhecer {:^20}!' .format(nombre))


'''
int = número inteiros => 7, 0, -4
float = números reais ou números de pontos flutuantes => 0.3, -12.432, 9.43, 7.0
bool = valores booleanos, ou valores lógicos => True, False (a primeira letra maiuscula)
str = valores caracteres ou strings => 'Olá', '7.5', '34', '', 'Olá mundo!'
'''