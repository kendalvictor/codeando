import math


class Numero:
    poder_inicial = 24

    def __init__(self, num):
        self.num = num
        self.es_primo = self.primo

    def __str__(self):
        return str(self.num)

    @property
    def primo(self):
        n = self.num
        for i in range(2, math.ceil(math.sqrt(n)) + 1):
            if i < n and n % i == 0:
                return False
        return True

    def es_par(self):
        n = self.num
        if n % 2 == 0:
            return True
        return False

num_7 = Numero(7)
print("Evaluacion de 7")
print(num_7.es_primo)
print(num_7.es_par())

num_16 = Numero(16)
print("Evaluacion de 16")
print(num_16.es_primo)
print(num_16.es_par())
