import arcpy

descripcion=arcpy.Describe(r"C:\compartir\Curso Python\GDB\practica.gdb\CentralesHidroelectricas")

print "El nombre del elemento es: ", descripcion.name
print "La ruta es: "+descripcion.path
print "El tipo de dato es: %s"%descripcion.dataType
