#DESAFIO 042
print('Desafio 042')
primeiro_lado = float(input("Priemira reta: "))
segundo_lado = float(input("Segunda reta: "))
terceiro_lado = float(input("Terceira reta: "))
if primeiro_lado < segundo_lado + terceiro_lado and segundo_lado < primeiro_lado+terceiro_lado and terceiro_lado < primeiro_lado + segundo_lado:
    print("As retas acima podem formar um triangulo")
    if primeiro_lado == segundo_lado == terceiro_lado:
        print("O seu triangulo é equilátero")
    elif primeiro_lado == segundo_lado or primeiro_lado == terceiro_lado or segundo_lado == terceiro_lado:
        print("O seu triangulo é isosceles")
    elif primeiro_lado != segundo_lado != terceiro_lado:
        print("O seu triangulo é escaleno")
else:
    print("Não pode formar um triangulo")

#DESAFIO 043
print('Desafio 043')
peso = float(input("Qual o seu peso? (KG) "))
altura = float(input("Qual a sua altura? (m) "))
imc = peso / (altura * altura)
print("O IMC dessa pessoa é de {:.1f}".format(imc))
if imc < 18.5:
    print("Abaixo do peso")
elif 18.5 <= imc < 25:
    print("Peso ideal")
elif 25 <= imc < 30:
    print("Sobrepeso")
elif 30 <= imc < 40:
    print("Obesidade ")
elif imc >= 40:
    print("Obersidade Mórbida")