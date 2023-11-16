lanche = ("sorvete", 'hamburguer', 'suco', 'pizza')
for i in lanche:
    print(f'{i}\n')

for pos, comida in enumerate(lanche):
    print(f'Eu comi {comida} na posicao {pos}')

print(lanche[0:])
print(lanche[:2])
