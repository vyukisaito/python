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

