from PIL import Image, ImageDraw

#  r0,  r1,    r2,   r3, rn
# [10, 100, 24823, 3054,  0]
rojos = [0 for _ in range(256)]
verdes = [0 for _ in range(256)]
azules = [0 for _ in range(256)]

imagen = Image.open('gatito.jpg')
pixeles = imagen.getdata()
#       = [(0, 0, 0), (0, 0, 0), ...]

for rojo, verde, azul in pixeles:
    rojos[rojo] += 1
    verdes[verde] += 1
    azules[azul] += 1


def histograma(colores, nombre):
    lienzo = Image.new('RGB', (255, 255))
    lapiz = ImageDraw.Draw(lienzo)
    maximo_valor = max(colores)

    for color, valor in enumerate(colores):
        altura = valor/maximo_valor * 255
        lapiz.line(
            [(color, 255), (color, 255 - altura)],
            'white',
            1
        )

    lienzo.save('{}.bmp'.format(nombre))


histograma(rojos, 'rojo')
histograma(verdes, 'verde')
histograma(azules, 'azul')
