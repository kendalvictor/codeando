import arcpy

with arcpy.da.UpdateCursor(r"D:\Publicidad cursos\Taller ArcPy\GDB\Dia4.gdb\Estaciones",["COD_ESTAC", "NOM_ESTAC"]) as cursor:
	for registro in cursor:
		if registro[0]=='27' or registro[0]=='20':
			cursor.deleteRow()

print "Registros eliminados"