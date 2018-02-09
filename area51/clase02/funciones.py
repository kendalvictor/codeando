# import constantes
# from constantes import pi as pi_exacto

from constantes.matematicas import pi


def area_circulo(radio):
    return pi * (radio ** 2)

print(area_circulo(53))
