nro_notas = int(input('cuántas notas? '))

notas = []

for n in range(nro_notas):
    nota = int(input('nota no. {}'.format(n + 1)))
    notas.append(nota)

promedio = sum(notas) / nro_notas

print('promedio: {}'.format(promedio))