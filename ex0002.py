n = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
soma = n + n2
vezes = n * n2
divisao = n / n2
divisaoInteira = n // n2
potencia = n**n2
print('A soma é {},\no produto é {} e a divisão é {:.1f} ' .format(soma, vezes, divisao), end='')
# o :.1f serve para deixar so uma casa pos virgula e o end='' serve para que não quebre a linha
# o \n serve para quebrar a linha
print('Divisão inteira {} e potência {} \n' .format(divisaoInteira, potencia))

#DESAFIO 005
print('DESAFIO 005')
numero = int(input('Digite algum número: '))
sucessor = numero + 1
antecessor = numero - 1
print('O sucessor do {} é {}, e o antecessor é {} \n' .format(numero, sucessor, antecessor))

#DESAFIO 006
print('DESAFIO 006')
num = int(input('Digite algum número: '))
dobro = num * 2
triplo = num *3
raiz = num ** (1/2)
print('O dobro do {} é: {}, o seu tripo é: {} e a sua raiz é: {} \n' .format(num, dobro, triplo, raiz))

#DESAFIO 007
print('DESAFIO 007')
nota1 = int(input('Quanto que você tirou em math? '))
nota2 = int(input('Quanto que você tirou em português? '))
media = (nota1 + nota1) / 2
print('Sua nota em math foi: {} e em português foi: {} e sua média foi: {} \n' .format(nota1, nota2, media))

#DESAFIO 008
print('DESAFIO 008')
metros = int(input('Digite um valor em metros: '))
cm = metros * 100
ml = metros * 1000
print('Uma corda possui {} metros, em centimetros seria {} e em milimetros seria {} \n' .format(metros, cm, ml))

#DESAFIO 009
print('DESAFIO 009')
valor = int(input('Digite um número qualquer: '))

dois = valor * 2
tres = valor *3 
quatro = valor * 4
cinco = valor *5
seis = valor * 6
sete = valor* 7
oito = valor * 8
nove = valor * 9
print('A tabuada do {} é:' .format(valor))
print('{} X 1 = {}' .format(valor, valor))
print('{} X 2 = {}' .format(valor, dois))
print('{} X 3 = {}' .format(valor, tres))
print('{} X 4 = {}' .format(valor, quatro))
print('{} X 5 = {}' .format(valor, cinco))
print('{} X 6 = {}' .format(valor, seis))
print('{} X 7 = {}' .format(valor, sete))
print('{} X 8 = {}' .format(valor, oito))
print('{} X 9 = {}\n' .format(valor, nove))

#DESAFIO 010
print('DESAFIO 010')
reais = int(input('Quantos reais você tem? '))
dolar = reais / 4.97
print('Com {}R$ você pode comprar {:.1f} dolares \n' .format(reais, dolar))

#DESAFIO 011
print('DESAFIO 011')
altura = int(input('Qual a altura da sua parede (em métros)? '))
largura = int(input('Qual a largura da sua parede (em métros)? '))
area = altura * largura
tinta = area / 2
print('A area da sua parede é {}, e precisará de {:.1f} litros de tinta para pinta-la \n' .format(area, tinta))

#DESAFIO 012
print('DESAFIO 012')
preco = int(input('Coloque um preço de um produto: '))
desconto = preco * 0.05 
descontoCompleto = preco - desconto
print('O seu produto custa: {}, agora com 5 de desconto: {:.1f} \n' .format(preco, descontoCompleto))

#DESAFIO 013
print('DESAFIO 013')
salario = int(input('Coloque o seu salário: '))
aumento = salario * 0.15 
aumentoCompleto = salario + aumento
print('O seu salário é: {}, agora com 15 de aumento: {:.1f} \n' .format(salario, aumentoCompleto))