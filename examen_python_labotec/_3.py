def factorial(nn):
    if nn == 1:
        return 1
    else:
        sol = nn * factorial(nn - 1)
    return sol

dic_operacion = {
    "suma": lambda x, y: x + y,
    "multiplicacion": lambda x, y: x * y,
    "factorial": lambda x: factorial(x)
}


def select_operacion():
    respuesta = input("..... ")
    if respuesta.strip().lower() in ["suma", "multiplicacion", "factorial"]:
        return respuesta
    else:
        print("Respuesta invalida...", end=" ")
        select_operacion()


def get_num(i):
    num = 0
    try:
        num = int(input("Ingrese numero {0}: ".format(i)))
    except ValueError:
        print("ERROR entero no valido, ", end=" /")
        num = get_num(i)
    except Exception as e:
        raise Exception(str(e))
    return num


print("""
Escriba el nombre de la operacion a realizar:
- suma
- multiplicacion
- factorial
""")
respuesta = select_operacion()
if respuesta in ["suma", "multiplicacion"]:
    numero1 = get_num("1")
    numero2 = get_num("2")
    print("Solucion..... ", dic_operacion[respuesta](numero1, numero2))
else:
    numero = get_num("")
    print("Solucion..... ", dic_operacion[respuesta](numero))
