#DESAFIO 005
print('DESAFIO 005')
numero = int(input('Digite algum número: '))

print('O sucessor do {} é {}, e o antecessor é {} \n' .format(numero, (numero + 1), (numero - 1)))

#DESAFIO 006
print('DESAFIO 006')
num = int(input('Digite algum número: '))
dobro = num * 2
triplo = num *3
raiz = num ** (1/2)
print('O dobro do {} é: {}, o seu tripo é: {} e a sua raiz é: {} \n' .format(num, dobro, triplo, raiz))

#DESAFIO 007
print('DESAFIO 007')
nota1 = float(input('Quanto que você tirou em math? '))
nota2 = float(input('Quanto que você tirou em português? '))
media = (nota1 + nota1) / 2
print('Sua nota em math foi: {} e em português foi: {} e sua média foi: {} \n' .format(nota1, nota2, media))

#DESAFIO 008
print('DESAFIO 008')
metros = float(input('Digite um valor em metros: '))
cm = metros * 100
ml = metros * 1000
print('Uma corda possui {} metros, em centimetros seria {} e em milimetros seria {} \n' .format(metros, cm, ml))

#DESAFIO 009
print('DESAFIO 009')
valor = int(input('Digite um número qualquer: '))


print('A tabuada do {} é:' .format(valor))
print('{} X  1 = {}' .format(valor, valor))
print('{} X  2 = {}' .format(valor, (valor*2)))
print('{} X  3 = {}' .format(valor, (valor*3)))
print('{} X  4 = {}' .format(valor, (valor*4)))
print('{} X  5 = {}' .format(valor, (valor*5)))
print('{} X  6 = {}' .format(valor, (valor*6)))
print('{} X  7 = {}' .format(valor, (valor*7)))
print('{} X  8 = {}' .format(valor, (valor*8)))
print('{} X  9 = {}' .format(valor, valor*9))
print('{} X 10 = {}\n' .format(valor, valor*10))

#DESAFIO 010
print('DESAFIO 010')
reais = int(input('Quantos reais você tem? '))
dolar = reais / 4.97
print('Com {}R$ você pode comprar {:.1f} dolares \n' .format(reais, dolar))

#DESAFIO 011
print('DESAFIO 011')
altura = float(input('Qual a altura da sua parede (em métros)? '))
largura = float(input('Qual a largura da sua parede (em métros)? '))
#utiliza float pois nesse números pode ter 1.5
area = altura * largura
tinta = area / 2
print('A area da sua parede é {}, e precisará de {:.1f} litros de tinta para pinta-la \n' .format(area, tinta))

#DESAFIO 012
print('DESAFIO 012')
preco = float(input('Coloque um preço de um produto: '))
desconto = preco - (preco * 0.05)
print('O seu produto custa: R${:.1f}, agora com 5% de desconto: {:.2f} \n' .format(preco, desconto))

#DESAFIO 013
print('DESAFIO 013')
salario = float(input('Coloque o seu salário: '))
aumento = salario + (salario * 0.15) 
print('O seu salário é: {}, agora com 15% de aumento: R${:.2f} \n' .format(salario, aumento))

#DESAFIO 014
print('DESAFIO 014')
celsius = float(input('Informe a temperatura em Cº: '))
faren = celsius * (9/5) + 32
print('A temperatura de {}ºC conrresponde a {}ºF \n' .format(celsius, faren))

#DESAFIO 015
print('DESAFIO 015')
dias = int(input('Quantos dias você ficou com o carro? '))
km = float(input('Quantos KM você percorreu? '))
aluguel = (dias * 60) + (km * 0.15)
print('O seu alguel vai custar R${:.2f}' .format(aluguel))