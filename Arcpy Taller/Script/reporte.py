# Importando modulo del ARCGIS
import arcpy

# sobre escribir la salida
arcpy.env.overwriteOutput=True

arcpy.env.workspace=r"D:\Publicidad cursos\Taller GDB\Python Dia 2\GDB\Practica.mdb"

listaCampos=arcpy.ListFields("CentralesHidroelectricas")

txtReporte=open(r"D:\Publicidad cursos\Taller GDB\Python Dia 2\Reportes\reporte.doc","w")
txtReporte.write("Detalles de los campos de centrales hidroelectricas"+"\n")

for campo in listaCampos:
	linea="Campo: {0}  Tipo: {1} Longitud: {2}\n".format(campo.name,campo.type,campo.length)
	txtReporte.write(linea)

txtReporte.close()

print "verifique su reporte"




