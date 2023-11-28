'''
teste = list()
teste.append('Gustavo')
teste.append(40)
galera = list()
galera.append(teste[:])
teste[0] = "Yuki"
teste[1] = 15
galera.append(teste[:])
print(galera)
pessoas = [['Yuki', 15, 2], ['Gustavo', 23], ['Ana', 12]]
print(pessoas[0][1])

for i in pessoas:
    print(f'{i[0]} tem {i[1]} anos de idaide')

dados = list()
pessoas = list()
for i in range(3):
    dados.append(str(input("Qual o seu nome? ")))
    dados.append(int(input("Qual a sua idade? ")))
    pessoas.append(dados[:])
    dados.clear()
print(pessoas)
for i in pessoas:
    if i[1] >= 18:
        print(f'{i[0]} é maior de idade')
    else:
        print(f'{i[0]} é menor de idade')
'''


# Desagio 84
dados = list()
pessoas = list()
maior = menor = 0
while True:
    dados.append(str(input("Nome:  ")))
    dados.append(float(input("Peso: ")))
    if len(pessoas) == 0:
        maior = menor = dados[1]
    else:
        if maior < dados[1]:
            maior = dados[1]
        if menor > dados[1]:
            menor = dados[1]
    pessoas.append(dados[:])
    dados.clear()
    resp = str(input("Quer continar? ")).strip().upper()[0]
    if resp in 'N':
        break

print(f'Ao todo você cadastrou {len(pessoas)} pessoas')
print(f"O maior peso foi de {maior}KG. Peso de ", end='')
for i in pessoas:
    if i[1] == maior:
        print(f'{i[0]} ', end='')
print('')
print(f"O menor peso foi de {menor}KG. Peso de ", end='')
for i in pessoas:
    if i[1] == menor:
        print(f"{i[0]} ", end='')
