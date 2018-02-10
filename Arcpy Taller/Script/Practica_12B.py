import arcpy, os

arcpy.env.overwriteOutput=True
arcpy.env.workspace=r"C:\compartir\Curso Python\GDB\Practica.gdb"

fc_lista=arcpy.ListFeatureClasses()

for fc in fc_lista:
	desc=arcpy.Describe(fc)
	if desc.shapeType=='Point':
		bufferdistancia='10 meters'
	elif desc.shapeType=='Polyline':
		bufferdistancia='6 meters'
	elif desc.shapeType=='Polygon':
		bufferdistancia='-2 meters'
	print "Buffer {0} por {1}".format(fc,bufferdistancia)
	in_features=fc
	out_feature_class = fc + 'Buff'
	buffer_distancia = bufferdistancia
	arcpy.Buffer_analysis(in_features,out_feature_class,buffer_distancia)

print "fin"