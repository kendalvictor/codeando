import arcpy

arcpy.env.workspace=r"D:\Publicidad cursos\Taller ArcPy\SHP"

sm="SuperMercado.shp"
campo="periodocat"
expresion="buscarPeriodo(!UBIGEO!)"
bloqueCodigo="""
def buscarPeriodo(dato):
	if dato=="150103":
		return 2015
	elif dato=="150108" or dato=="150130":
		return 2014
	elif dato=="150101":
		return 2010
	elif dato=="150135":
		return 2009
	elif dato=="120101":
		return 2013
	else:
		return 2016
"""


arcpy.AddField_management(sm,campo,"DOUBLE")

arcpy.CalculateField_management(sm,campo,expresion,"PYTHON_9.3",bloqueCodigo)

print "proceso con exito"