import arcpy
fc=r"C:\Curso Python\Dia 2\GDB\Dia2.gdb\predios"
with arcpy.da.SearchCursor(fc,("CodigoPredio","CodigoManzana","SHAPE@XY")) as cursor:
	for registro in cursor:
		print "El predio {0} con codigo de MZ {1} tiene un centroide de: {2}".format(registro[0],registro[1],registro[2])
