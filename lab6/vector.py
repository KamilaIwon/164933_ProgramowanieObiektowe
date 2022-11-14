
import math

class Vector:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    # print
    def __repr__(self):
        return f'[pierwsza wspolrzedna wektora: {self.a}' \
               f' \n druga wspolrzedna wektora: {self.b}]'

    def __str__(self):
        return f'[{self.a},{self.b}]'

    # dodawanie wektorow
    def __add__(self, other):
        return Vector(self.a+other.a,self.b+other.b)

    # odejmowanie wektorow
    def __sub__(self, other):
        return Vector(self.a - other.a, self.b - other.b)

    # dlugosc wektora
    def __len__(self):
        return math.pow(self.a*self.a + self.b*self.b, 0.5)

 # nie działa
    def __getitem__(self, item):
        return self.item