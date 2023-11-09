'''
# Desafio 46
print("Desafio 46")
from time import sleep
print("Contagem regressiva...")
for c in range(10, 0, -1):
    sleep(1)
    print(c)

# Desafio 47
print("Números pares")
for i in range(2, 51, 2):
    print(i, end=' ')

# Desafio 48
cont = 0
soma = 0
for i in range(1, 501, 2):
    if i % 3 == 0:
        cont = cont + 1
        soma += i
print("A soma é {} de todos os {} valores" .format(soma, cont))

# Desafio 49
num = int(input("Digite um numero inteiro: "))
for i in range(1, 11):
    print("{} x {} = {}" .format(i, num, num * i))

# Desafio 50
cont = 0
soma = 0
for i in range(1, 7):
    num = int(input("Digite o {} valor: ".format(i)))
    if num % 2 == 0:
        soma += num
        cont += 1
print("Você informou {} números e a soma foi {}" .format(cont,  soma))

# Desafio 51
print("="*30)
print("    10 Termos de uma PA")
print("="*30)
primeiro_termo = int(input("Primeiro Termo: "))
razao = int(input("Razão: "))
decimo = primeiro_termo + (10 - 1) * razao
for i in range(primeiro_termo, decimo+razao, razao):
    print(i, end=" → ")
print("Cabou")

# Desafio 52
number = int(input("Digite um número inteiro: "))
total = 0
for i in range(1, number+1):
    if number % i == 0:
        print("\033[33m", end=" ")
        total += 1
    else:
        print("\033[31m", end=" ")
    print(i, end=" ")
print("\n\033[mO número {} foi dividido {} vezes." .format(number, total), end=" ")
if total == 2:
    print("Por isso é PRIMO")
else:
    print("Por isso NÃO é primo")

# Desafio 53
frase = str(input("Digite um frase: ")).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
# sem o for ficaria assim: inverso[::-1]
print("Você digitou a frase: {}".format(junto))
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
print("O inverso de {} é {}".format(junto, inverso))
if inverso == junto:
    print("A frase digitada é um palindromo")
else:
    print("A frase digitada não é um palindromo")

# Desafio 54
from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for i in range(1, 8):
    nasc = int(input("Em que ano a {} pessoa nasceu?: " .format(i)))
    idade = atual - nasc
    if idade >= 21:
        totmaior += 1 
    else:
        totmenor += 1
print("Ao todo tivemos {} pessoas maior de idade" .format(totmaior))
print("Ao todo tivemos {} pessoas menor de idade" .format(totmenor))

# Desafio 55
maior_peso = 0
menor_peso = 0
for i in range(1, 6):
    peso = float(input("Peso da {} pessoa: " .format(i)))
    if peso == 1:
        maior_peso = peso
        menor_peso = peso
    else:
         if peso > maior_peso:
             maior_peso = peso
         if peso < menor_peso:
             menor_peso = peso
print("O maior peso lideo foi {}" .format(maior_peso))
print("O menor peso lideo foi {}" .format(menor_peso))
''' 

# Desafio 56
media = 0
soma = 0
maior_homem = 0
nome_velho = ''
totmulher20 = 0
for i in range(1, 5):
    print("----- {} PESSOA -----" .format(i))
    nome = str(input("Nome: ")).strip()
    idade = int(input("Idade: "))
    sexo = str(input("Sexo [M/F]: ")).strip()
    soma += idade
    if i == 1 and sexo in "Mm":
        maior_homem = idade
        nome_velho = nome
    if sexo in "Mn" and idade > maior_homem:
        maior_homem = idade
        nome_velho = nome
    if sexo in "Ff" and idade < 20:
        totmulher20 += 1
media = soma / 4
print("A media de idade do grupo é de {} anos" .format(media))
print("O homem mais velho tem {} anos, e se chama {}" .format(maior_homem, nome_velho))
print("Ao todo são {} mulheres com menos de 20 anos" .format(totmulher20))