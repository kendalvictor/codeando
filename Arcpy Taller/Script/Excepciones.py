import arcpy
arcpy.env.overwriteOutput=True
arcpy.env.workspace=r"C:\Curso Python\Dia 2\GDB\practica.gdb"
listaFC=arcpy.ListFeatureClasses("SuperMercado")
for fc in listaFC:
	try:
		arcpy.Buffer_analysis(fc,"fcbuff3km","3 Kilometers")
	except arcpy.ExecuteError:
		print arcpy.GetMessage(2)