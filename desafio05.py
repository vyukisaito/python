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
from random import randint
from time import sleep
itens = ('Pedra','Papel', 'Tesoura')
computador = randint(0, 2)
print('Desafio 045')
print('''SUAS OPÇÕES:
[0] PEDRA
[1] PAPEL
[2] TESOURA
''')
jogador = int(input('Qual a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
print('-=-'*11)
print("Computador jogou {}" .format(itens[computador]))
print('Jogador jogou {}' .format(itens[jogador]))
print('-=-'*11)

if computador == 0: #PEDRA
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCE')
    elif jogador == 2:
        print('COMPUTADOR VENCE')
    else:
        print("Jogada INVALIDA!")
elif computador == 1: #PAPEL
    if jogador == 0:
        print('COMPUTADOR VENCE')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR VENCE')
    else:
        print("Jogada INVALIDA!")
elif computador == 2: #TESOURA
    if jogador == 0:
        print('JOGADOR VENCE')
    elif jogador == 1:
        print('COMPUTADOR VENCE')
    elif jogador == 2:
        print('EMPATE')
    else:
        print("Jogada INVALIDA!")