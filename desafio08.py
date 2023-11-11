'''
# Desafio 60
print("=-"*15)
print("Calculadore de FATORIAl")
print("=-"*15)
num = int(input("Digite um número: "))
c = num
f1 = 1 
while c > 1: 
    f1 *= c
    c -= 1
    print(c+1,end="x")
    # ou print('{}'.format(c), end="")
    # print(' x ' if c > 1 else ' = ', end='')
print(1, end=" ")
print("O resutado do fatorial de {} é {}".format(num, f1))
'''

print("    10 Termos de uma PA")
print("="*30)
primeiro = int(input("Primeiro Termo: "))
razao = int(input("Razão: "))
termo = primeiro
cont = 1
while cont <= 10:
    print('{} → ' .format(termo), end="")
    termo += razao
    cont += 1
print("FIM")