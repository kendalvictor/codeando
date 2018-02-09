from PIL import Image, ImageDraw

imagen = Image.open('gatito.jpg')

rojos = [0 for _ in range(256)]
verdes = [0 for _ in range(256)]
azules = [0 for _ in range(256)]

for (rojo, verde, azul) in imagen.getdata():
    rojos[rojo] += 1
    verdes[verde] += 1
    azules[azul] += 1


def generar_histograma(frecuencias, nombre):
    histograma = Image.new('RGB', (255, 255))
    lapiz = ImageDraw.Draw(histograma)

    maximo = max(frecuencias)
    for (x, cantidad) in enumerate(frecuencias):
        lapiz.line([(x, 255), (x, 255 - (cantidad/maximo) * 255)], 'white', 1)

    histograma.save(nombre)


generar_histograma(rojos, 'rojos.bmp')
generar_histograma(verdes, 'verdes.bmp')
generar_histograma(azules, 'azules.bmp')
