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
vista_dinheiro = preco * 0.9
vista_cartao = preco * 0.5
duas_vezes = preco / 2
