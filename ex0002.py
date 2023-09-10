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
print('Sua nota em math foi: {} e em português foi: {} e sua média foi: {}' .format(nota1, nota2, media))