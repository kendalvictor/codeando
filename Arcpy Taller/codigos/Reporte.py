import arcpy

arcpy.env.workspace=r"D:\Publicidad cursos\Taller ArcPy\GDB\Practica.mdb"
fc="CentralesHidroelectricas"

listaCampos=arcpy.ListFields(fc)

txtReporte=open(r"D:\Publicidad cursos\Taller ArcPy\Reportes\CentralesHidroelectricas.xls","w")
txtReporte.write("Detalle de los campos de centrales hidroelectricas\n")
txtReporte.write("==================================================\n")

for campo in listaCampos:
	linea= "Campo:{0} \t Tipo:{1} \t Longitud:{2}\n".format(campo.name,campo.type,campo.length)
	txtReporte.write(linea)
txtReporte.close()
print "Puede visualizar los resultados en la carpeta reportes"
