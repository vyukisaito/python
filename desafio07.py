'''
r = "S"
while r == "S":
    n = int(input("Digite um valor: "))
    r = str(input("Quer continuar? [S/N] ")).upper()
print("FIM")
'''
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
