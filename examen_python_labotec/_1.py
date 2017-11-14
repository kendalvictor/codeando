def get_num():
    list_num = []
    try:
        numeros = input("/////Ingrese numeros separados por espacios: ")
        ingresados = [num for num in numeros.split()]
        list_num = [int(num) for num in ingresados]
        print("Numeros ingresados : {0}".format(
            " ".join(ingresados)
        ))
    except ValueError:
        print("ERROR...Ingreso numérico no valido")
    except Exception as e:
        print("ERROR DETECTADO... " + str(e))
    return list_num


def continuacion():
    print("¿Desea continuar? si/no")
    respuesta = input("..... ")
    if respuesta.strip().lower() in ["si", "no"]:
        return respuesta
    else:
        print("Respuesta invalida...", end=" ")
        continuacion()



proceso = True
print("SOLUCION PROBLEMA #1 \n")
while proceso:
    list_num = get_num()
    if list_num:
        list_num.sort()
        print("Num. mayor: ", list_num[-1])
        print("Num. menor: ", list_num[0])
        print("Suma      : ", sum(list_num))

    respuesta = continuacion()
    if respuesta == "no":
        proceso = False
