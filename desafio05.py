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

# DESAFIO 044
print('Desafio 044')
print("="*30)
print("          MERCADO")
print("="*30)
preco = float(input("Preço de compras: "))

print('''FORMAS DE PAGAMENTO:
[1] à vista dinheiro/cheque
[2] à vista cartão
[3] 2x no cartão
[4] 3x ou mais no cartão
''')
opcao = int(input("Qual a opção? "))

duas_vezes = preco / 2
if opcao == 1:
    total = preco * 0.9
elif opcao == 2:
    total = preco - (preco * 5/100)
elif opcao == 3:
    total = preco
    parcela = total / 2
    print("Sua compra setá parcelada em 2x de R${}" .format(parcela))
elif opcao == 4:
    total = preco + (preco * 20 / 100)
    total_parcela = int(input("Quantas parcelas? "))
    parcela = total / total_parcela
    print("Sua compra será parcelada em  {:.2f}x de R${:.2f} com juros" .format(total_parcela, parcela))
print("Sua compra de R${:.2f} vai custar R${:.2f} no final." .format(preco, total))

# DESAFIO 045
import random
print('Desafio 045')
print('''SUAS OPÇÕES:
[0] PEDRA
[1] PAPEL
[2] TESOURA
''')
jogada = int(input("Qual a sua jogada? "))
lista = ["Pedra", "Papel", "Tesoura"]
computador = random.choice(lista)

if jogada == 0:
    gon = 'Pedra'
elif jogada == 1:
    gon = 'Papel'
elif jogada == 2:
    gon = 'Tesoura'


print('=-='*10)
print('Computador jogou {}' .format(computador))
print('O jogador jogou {}' .format(gon))
print('=-='*10)

if gon == computador:
    print("EMPATE")
elif jogada == 0:
    gon = 'Pedra'
    if gon == 'Pedra' and computador == 'Papel':
        print("Computador venceu")
    elif gon == 'Pedra' and computador == 'Tesoura':
        print("JOGADOR VENCEU")
elif jogada == 1:
    gon = 'Papel'
    if gon == 'Papel'and computador == 'Tesoura':
        print("Computador venceu")
    elif gon == 'Papel' and computador == 'Pedra':
        print("jogador venceu")
elif jogada == 2:
    gon = 'Tesoura'
    if gon == 'Tesoura'and computador == 'Pedra':
        print("Computador venceu")
    elif gon == 'Tesoura' and computador == "Papel":
        print("Jogador venceu")
    else:
        print("Opcao invalida")