import arcpy

arcpy.env.workspace=r"C:\compartir\Curso Python\GDB\practica.gdb"
try:
	descFC=arcpy.Describe("CentralesHidroelectricas")
	print "El tipo de Shape es: " + descFC.ShapeType
	campos=descFC.fields
	for campo in campos:
		print '---> Campo: ' + campo.name
		print '---> Tipo: ' + campo.type
		print '---> Longitud: ' + str(campo.length)
	ext=descFC.extent
	print "XMin: %f" % (ext.XMin)
	print "YMin: %f" % (ext.YMin)
	print "XMax: %f" % (ext.XMax)
	print "YMax: %f" % (ext.YMax)
except:
	print arcpy.GetMessages()