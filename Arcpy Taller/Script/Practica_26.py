import arcpy

arcpy.env.overwriteOutput=True
fc=sys.argv[1]
campo1=sys.argv[2]
campo2=sys.argv[3]
campos=[campo1,campo2,'SHAPE@XY']
expresion=sys.argv[4]
rutaReportes=sys.argv[5]
extension=sys.argv[6]
archivoReporte=rutaReportes+"\\"+"Reporte"+extension
xlsFile=open(archivoReporte,"w")
xlsFile.write('Lista de estaciones'  + "\n")
xlsFile.write('========================' + "\n")

if expresion!='':
	with arcpy.da.SearchCursor(fc,campos,expresion) as cursor:
		for registro in cursor:
			linea="\nCODIGO: \t{0} \tDESCRIPCION: \t{1} \tCOORDENADAS: \t{2}\n".format(registro[0],registro[1],registro[2])
			xlsFile.write(linea)			
else:
	with arcpy.da.SearchCursor(fc,campos) as cursor:
		for registro in cursor:
			linea="\nCODIGO: \t{0} \nDESCRIPCION: \t{1} \nCOORDENADAS: \t{2}".format(registro[0],registro[1],registro[2])
			xlsFile.write(linea)
xlsFile.close()
arcpy.AddMessage("Revise el reporte en: " + archivoReporte)