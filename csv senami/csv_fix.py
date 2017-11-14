import glob
import csv
import os

indices, fechas, temp, rh, dew_point = [], [], [], [], []
seriales = []

dic_order = {
    0: lambda t: indices.append(list(t)),
    1: lambda t: fechas.append(list(t)),
    2: lambda t: temp.append(list(t)),
    3: lambda t: rh.append(list(t)),
    4: lambda t: dew_point.append(list(t)),
}

detect = 0
for csvname in glob.iglob('*.csv', recursive=True):
    print(csvname)
    with open(csvname, newline='', encoding='iso-8859-1') as workfile:
        readerx = csv.reader(workfile, delimiter=",", dialect='excel')
        readerx.__next__()

        i = 0
        for fila in zip(*list(readerx)):
            if i in [0, 1]:
                if detect == 0:
                    dic_order[i](fila)
            elif i in [2, 3, 4]:
                dic_order[i](fila)
            elif i == 5:
                seriales.append(fila[0])
            else:
                break
            i += 1
    detect += 1

nuevos_archivos = {
    "temp": temp,
    "rh": rh,
    "dew_point": dew_point,
}
encabezado = ["index", "timestamp"] + seriales

if not os.path.exists("output"):
    os.makedirs("output")

for new, data in nuevos_archivos.items():
    with open("output/" + new + ".csv", "w") as outputfile:
        csvoutput = csv.writer(outputfile, dialect='excel')
        matriz = [indices[0], fechas[0]] + data

        csvoutput.writerow(encabezado)
        for row in list(zip(*matriz)):
            csvoutput.writerow(row)

print("PROCESO SATISFACTORIO")







