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

# Desafio 61 e 62
print("    10 Termos de uma PA")
print("="*30)
primeiro = int(input("Primeiro Termo: "))
razao = int(input("Razão: "))
termo = primeiro
cont = 1
total = 0   
novos_num = 10
while novos_num != 0:
    total = total + novos_num   
    while cont <= total:
        print('{} → ' .format(termo), end="")
        termo += razao
        cont += 1
    print("PAUSA")
    novos_num = int(input("Quantos termos voce quer mostrar mais? "))
print("Progressão finalizada com {} termos mostrados" .format(total))

# Desafio 63
print('='*20)
print("Seuquencia de Fibonacci")
print('='*20)
n = int(input("Quantos termos você quer mostrar? "))
t1 = 0
t2 = 1
print('{} → {}' .format(t1, t2), end="")
cont = 3
while cont <= n:
    t3 = t1 + t2
    print(' → {}'.format(t3), end='')
    t1 = t2
    t2 = t3
    cont += 1
print(" → FIM")

# Desafio 64
num = soma = cont = 0
num = int(input("Digite um número [999 para parar]: "))
while num != 999:
    soma += num
    cont += 1
    num = int(input("Digite um número [999 para parar]: "))
print("Você digitou {} valores. A soma dos valores é {} ".format(cont, soma))
'''

# Desafio 65
maior = menor = cont = media = soma = 0
continuar = False
while not continuar:
    num = int(input("Digite um número: "))
    cont += 1
    sim = str(input("Quer continuar [S/N]? ")).strip().upper()[0]
    if cont == 1:
        maior = menor = num
    else: 
        if maior < num:
            maior = num
        if menor > num:
            menor = num
    soma += num
    media = soma / cont
    if sim in 'S':
        continuar = False
    else: 
        continuar = True
        print("O maior valor foi {}, o menor valor foi {}, e a média foi {}" .format(maior, menor, media))
