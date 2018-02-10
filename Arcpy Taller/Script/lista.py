# Importando modulo del ARCGIS
import arcpy

# sobre escribir la salida
arcpy.env.overwriteOutput=True

arcpy.env.workspace=r"D:\Publicidad cursos\Taller GDB\Python Dia 2\GDB\Dia2.gdb"

listaCapas=arcpy.ListFeatureClasses()

for capa in listaCapas:
	print capa