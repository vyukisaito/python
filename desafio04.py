#DESAFIO 033
print('Desafio 033')
um = int(input("Digite um número: "))
dois = int(input("Digite outro um número: "))
tres = int(input("Digite outro um número: "))
if um>dois and um>tres:
    print("O {} é o maior número" .format(um))
if um<dois and dois> tres:
    print("O {} é o maior número" .format(dois))
if um<tres and dois<tres:
    print("O {} é o maior número" .format(tres))
if um<dois and um<tres:
    print("O {} é o menor número \n" .format(um))
if um>dois and dois<tres:
    print("O {} é o menor número \n" .format(dois))
if um>tres and dois>tres:
    print("O {} é o menor número \n" .format(tres))
# Não consegui fazer :(

#DESAFIO 034
print('Desafio 034')
salario = float(input("Qual o seu salário? "))
if salario > 1250:
    print("Você receberá um aumento de 10%, com isso o seu salário é de {} \n" .format(salario + (salario * 0.1)))
else:
    print("Você receberá um aumento de 15%, com isso o seu salário é de {} \n" .format(salario + (salario * 0.15)))
    
#DESAFIO 035
print('Desafio 035')
print("=-=" *20)
print("Analisador de Triângulos")
print("=-=" *20)
s1 = float(input("Primeiro Segmento: "))
s2 = float(input("Segundo Segmento: "))
s3 = float(input("Terceiro Segmento: "))
if s1 < s2 + s3 and s2 < s1 + s3 and s3 < s1 + s2:
    print("Esses segmentos podem formar um triangulo\n")
else:
    print("Esses segmento não podem formar um triangulo\n")

#DESAFIO 036
print('Desafio 036')
casa = float(input("Valor da sua casa: R$"))
salario_ = float(input("Seu salário: R$"))
tempo = float(input("Em quantos anos você vai pagar? "))
preco = casa / (tempo * 12)
print('Para pagar uma casa de R${:.2f} em {} anos ' .format(casa, tempo), end='')
print('a prestação será de R${:.2f}' .format(preco) )
if preco <= salario_* 30/100:
    print("Emprestimo OK\n")
else:
    print("NÃO é possivel\n")

 #DESAFIO 037
print('Desafio 037')
num_inteiro = int(input("Digite um número inteiro: "))
print('''Escolha uma das bases para a conversão:
[1] para convertar para binário
[2] para convertar para octal
[3] para convertar para hexadecimal''')
opcao = int(input("Sua opção: "))
if opcao == 1:
    print("O {} convertido para binário é: {}" .format(num_inteiro, bin(num_inteiro)[2:]))
elif opcao == 2:
    print("O {} convertido para binário é: {}" .format(num_inteiro, oct(num_inteiro)[2:]))
elif opcao == 3:
    print("O {} convertido para binário é: {}" .format(num_inteiro, hex(num_inteiro)[2:]))
else:
    print("Opção invalida. Tente novamente")

#DESAFIO 038
print('Desafio 038')
primeiro_num = float(input("Primeiro número: "))
segundo_num = float(input("Segundo número: "))
if primeiro_num > segundo_num:
    print("O PRIMEIRO valor é maior")
elif segundo_num > primeiro_num:
    print("O SEGUNDO valor é maior")
elif segundo_num == primeiro_num:
    print("Os valores são iguais")
else:
    print("Valor INVÁLIDO")