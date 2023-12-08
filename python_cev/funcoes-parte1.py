'''
def msg(teste):
    print('------------')
    print(teste)
    print('------------')


msg('Teste')
def soma(a, b):
    print(f"A soma entre {a} e {b} é : {a+b}")
soma(b=5, a=6)

print()
def contador(*num):
    for i in num:
        print(i, end=' ')
    print()


contador(3, 4, 5)
contador(3, 1, 5, 3)

def dobra(lista):
    pos = 0
    while pos < len(lista):
        lista[pos] *= 2
        pos += 1    
valores = [1, 2, 3, 4, 5, 6]
dobra(valores)
print(valores)

# Desafio 96
def area(a, b):
    print(f'A area de um terreno {a}x{b} é de {a*b}m²')

largura = float(input('LARGURA (m): '))
comprimento = float(input('COMPRIMENTO (m): '))
area(largura, comprimento)

# Desafio 97
def escreva(msg):
    tamanho = len(msg) + 4
    print('-'*tamanho)
    print(f'  {msg}')
    print('-'*tamanho)
escreva('TEste')

# Desafio 98
print('Contagem de 1 até 10 em 1 e 1')
for i in range(1, 11):
    print(f'{i}', end=' ')
print("FIM!")   

print('Contagem de 10 até 0 em 2 e 2')
for i in range(10, -1, -2):
    print(i, end=' ')
print("FIM!")

def calc(a, b, c):
    print(f'Contagem de {a} até {b} de {c} em {c}')
    if a < b:
        for i in range(a, b+1, c):
            print(i, end=" ")
    else:
        for i in range(a, b - 1, -c):
            print(i, end=" ")
inicio = int(input("Início: "))
fim = int(input("Fim: "))
passo = int(input("Passo: "))
calc(inicio, fim, passo)
'''

# Desafio 99


def maior(*num):
    c = maior = 0
    print(f'Analisando os valores passados')
    for i in num:
        c += 1
        if c == 1:
            maior = i
        else:
            if i > maior:
                maior = i

        print(i, end=' ')

    print(f'Foram os {len(num)} valores informados, o maior é o {maior}')


maior(1, 2, 9, 4, 5, 6,11, 2)
