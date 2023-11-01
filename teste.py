#DESAFIO 039
print('Desafio 039')
from datetime import date
atual = date.today().year
nascimento = int(input("Ano de nascimento: "))
idade = 2023 - nascimento
print("Quem nasceu em {} tem {} anos em {}." .format(nascimento, idade, atual))
if idade < 18:
    print("Ainda faltam {} anos para o alistamento " .format(18-idade))
    print("Seu alistamento será em {}".format(2023+(18-idade)))
elif idade > 18:
    print("Você deveria ter se alistado há {} anos, em {}" .format(idade-18, 2023-(idade-18)))
elif idade == 18:
    print("Você deveria fazer o alistamento IMEDIATAMENTE")