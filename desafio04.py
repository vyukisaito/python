#DESAFIO 033
print('Desafio 033')
um = int(input("Digite um número: "))
dois = int(input("Digite outro um número: "))
tres = int(input("Digite outro um número: "))
if um > dois and um > tres:
    print("O {} é o ma ior número \n" .format(um))
elif um < dois and dois > tres:
    print("O {} é o maior número \n" .format(dois))
elif um < tres and dois < tres:
    print("O {} é o maior número \n" .format(tres))
elif um < dois and um < tres:
    print("O {} é o menor número \n" .format(um))
elif um > dois and dois < tres:
    print("O {} é omenor número \n" .format(dois))
elif um > tres and dois < tres:
    print("O {} é o menor número \n" .format(tres))
# Não consegui fazer :(

#DESAFIO 034
print('Desafio 034')
salario = float(input("Qual o seu salário? "))
if salario > 1250:
    print("Você receberá um aumento de 10%, com isso o seu salário é de {} \n" .format(salario + (salario * 0.1)))
else:
    print("Você receberá um aumento de 15%, com isso o seu salário é de {} \n" .format(salario + (salario * 0.15)))