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
    print("Esses segmentos podem formar um triangulo")
else:
    print("Esses segmento não podem formar um triangulo")