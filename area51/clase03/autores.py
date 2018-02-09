class Libro:
    def __init__(self, titulo, anio):
        self.titulo = titulo
        self.anio = anio

    def __eq__(self, other):
        return self.titulo == other.titulo and self.anio == other.anio


class Autor:
    def __init__(self, nombre, nacimiento):
        self.nombre = nombre
        self.nacimiento = nacimiento
        self.libros = []

    # agregar_libro(titulo='pantelón' anio=1990)
    # agregar_libro(Libro('pantaleon', 1990))
    def agregar_libro(self, *args, **kwargs):
        if len(args) == 1:
            libro = args[0]
            self._agregar_libro(libro)
        else:
            libro = Libro(**kwargs)
            self._agregar_libro(libro)

    def _agregar_libro(self, libro):
        if libro in self.libros:
            print('Libro repetido:', libro.titulo)
        else:
            self.libros.append(libro)


mvll = Autor(nombre='Mario Vargas..', nacimiento=9876)
mvll.agregar_libro(Libro(titulo='Pantaleón..', anio=1990))
mvll.agregar_libro(titulo='la guerra del fin del mundo', anio=2000)
mvll.agregar_libro(titulo='la guerra del fin del mundo', anio=2000)

for libro in mvll.libros:
    print(libro.titulo, libro.anio)
