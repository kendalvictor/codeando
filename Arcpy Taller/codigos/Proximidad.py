import arcpy

arcpy.env.workspace=r"D:\Publicidad cursos\Taller ArcPy\GDB\practica.gdb"

listaCapas=arcpy.ListFeatureClasses()

for capa in listaCapas:
	descFC=arcpy.Describe(capa)
	if descFC.shapeType=='Point':
		distancia="10 Meters"
	elif descFC.shapeType=='Polyline':
		distancia="6 Meters"
	elif descFC.shapeType=='Polygon':
		distancia="-2 Meters"
	#print "Buffer {0} por {1}".format(capa,distancia)
	salida=capa+"_buff"
	arcpy.Buffer_analysis(capa,salida,distancia)

print "Verifique los resultados"