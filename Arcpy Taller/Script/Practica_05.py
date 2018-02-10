import arcpy

arcpy.env.overwriteOutput=True

arcpy.env.workspace=r"C:\compartir\Curso Python\Shapefiles"
shape="SuperMercado.shp"
campo="Periodo"
#escribiendo una funcion
expresion="rellenarcampo( !UBIGEO!)"
codigo='''def rellenarcampo(dato):
	if dato=='150103':
		return 2016
	elif dato=='150130':
		return 2014
	else:
	  return 2015
'''

arcpy.AddField_management(shape,campo,"DOUBLE")

arcpy.CalculateField_management(shape,campo,expresion,"PYTHON_9.3",codigo)

print 'fin del proceso'