'''
um = [1, 2, 3, 4, 5]

num_dobrado = [numero * 2 for numero in num]
print(num_dobrado)

# HERANÇA
class Celular:
    def ligações(self):
        print('Fazendo ligação...')

    def jogar(self):
        print('Jogando...')
    
    def calcular(self, v1, v2):
        return v1 + v2

class Samsung(Celular):
    marca = 'Samsung'
    modelo = 'A23'
    cor = 'Prata'

samsung = Samsung()
samsung.ligações()
print(samsung.marca)

# POLIMORFISMO DE CLASSE
class Animal:
    def som(self):
        print('Som....')

class Cachorro(Animal):
    def som(self):
        print('Au Au')

class Gato(Animal):
    def som(self):
        print('Miau')

cachorro = Cachorro()
cachorro.som()
gato = Gato()
gato.som()
'''

# POLIMORFISMO DE INFERFACE
class Forma():

    def area(self):
        pass

class Quadrado(Forma):

    def __init__(self, lado):
        self.lado = lado

    def area(self):
        return self.lado ** 2
    
class Circulo(Forma):

    def __init__(self, raio):
        self.raio = raio

    def area(self):
        return 3.14 * self.raio ** 2
    
quadrado = Quadrado(5)
area_quadrado = quadrado.area()
print(area_quadrado)

circulo = Circulo(6)
area_circulo = circulo.area()
print(area_circulo)
