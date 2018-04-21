import time

def validate_cuadrada(matriz):
	tamanno = len(matriz) if isinstance(matriz, list) else None
	if not tamanno:
		print("ERROR... Verifique el tipo de dato ingresado")
		return False
	if not all(
		[isinstance(fila, list) and len(fila) == tamanno for fila in matriz]
		):
		print("ERROR... Matriz cuadrada no detectada")
		return False
	return tamanno


def inversa_while(matriz):
	"""
	Imprimire una version de transpuesta de una matriz reflejada en su 2da
	diagonal
	:param matriz (lista de listas, donde el tamaño de cada sublista es
				  igual al de la lista que las contiene):
	:return:
	"""
	tamanno = matriz.__len__()
	ref = tamanno + 1
	i = 1 #incide horizontal
	j = 1 #indice vertical
	while j < ref + 1:
		(new_i, new_j) = (i, j) if i + j == ref else (ref - j, ref - i)
		print(matriz[new_i - 1][new_j - 1], end='  ')

		if j == tamanno:
			print(" ")
			j = 0
			i+= 1

			if i > tamanno:
				del matriz
				break

		j += 1

def get_print_inversa(matriz):
	tamanno = validate_cuadrada(matriz)
	if tamanno:
		inicio_while =time.time()
		inversa_while(matriz)


if __name__ == '__main__':
	matriz = [
		[0, 9, 7, 4],
		[9, 0, 3, 6],
		[7, 2, 7, 5],
		[1, 6, 5, 8],
	]
	get_print_inversa(matriz)


