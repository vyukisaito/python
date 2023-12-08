'''
r = "S"
while r == "S":
    n = int(input("Digite um valor: "))
    r = str(input("Quer continuar? [S/N] ")).upper()
print("FIM")

i = 1
par = impar = 0
while i != 0:
    i = int(input('Digite um valor: '))
    if i != 0:
        if i % 2 == 0:
            par += 1
        else:
            impar += 1
print("Você digitou {} número pares e {} números impares!" .format(par, impar))

# Desafio 57
sexo = str(input('Informe seu sexo: [M/F] ')).strip().upper()[0]
while sexo not in 'MF':
    sexo = str(input("Dados inválidos. Por favor insira o seu sexo: ")).strip().upper()[0]
print("Sexo {} registrado com sucesso".format(sexo))

# Desafio 58
import random
resposta = random.randint(1, 10)
palpite = 0
acertou = False
print(resposta)
while not acertou:
    num = int(input("Digite um número de 1 a 10: "))
    palpite += 1
    if num == resposta:
        acertou = True
    else:
        if num < resposta:
            print("Mais...")
        elif num > resposta:
            print("Menos...")
print("Parabéns! O número era {}. Você levou {} vezes para acertar" .format(resposta, palpite))
'''
   
# Desafio 59
finalizar = False
primeiro_valor = int(input("Digite um valor: "))
segundo_valor = int(input("Digite outro valor: "))
while not finalizar:
    print('''[1] somar
[2] multiplicador
[3] maior
[4] novos números
[5] sair do programa
''')
    opcao = int(input("Qual a sua opção? "))
    if opcao == 1:
        somar = primeiro_valor + segundo_valor
        print("A soma dos numeros {} e {} é {}".format(primeiro_valor, segundo_valor, somar))
        finalizar = True
    elif opcao == 2:
        multiplicacao = primeiro_valor * segundo_valor
        print("A multiplicação do {} e {} é: {}" .format(primeiro_valor, segundo_valor, multiplicacao))
        finalizar = True
    elif opcao == 3:
        if primeiro_valor > segundo_valor:
            maior = primeiro_valor
            print("O maior número é: {}" .format(maior))
            finalizar = True
        elif primeiro_valor == segundo_valor:
            print("Os valores são iguais")
            finalizar = True
        else:
            maior = segundo_valor
            print("O maior número é: {}" .format(maior))
            finalizar = True
    elif opcao == 4:
        print('Informe os números novamente:')
        primeiro_valor = int(input("Digite um valor: "))
        segundo_valor = int(input("Digite outro valor: "))  
        finalizar = False
    else:
        finalizar = True

