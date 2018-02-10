# Script que realizael buffer a 1 km de distancia
'''
Programa realizado por: CAEG
Periodo: 2015
'''

# Importamos la libreria del Arcgis
import arcpy

#Sobre escribir resultados
arcpy.env.overwriteOutput=True

#Declaramos una variable de entorno
arcpy.env.workspace=r"D:\Geotaller\GDB\Practica.gdb"

listadecapas=arcpy.ListFeatureClasses()

xlsFile=open(r"D:\Geotaller\Reportes\Lista_de_Estaciones.xls","w")
xlsFile.write("Lista de Estaciones" + "\n" )
xlsFile.write("===================" + "\n" )

registros=arcpy.SearchCursor("Estaciones")

for registro in registros:
    valor = registro.getValue('NOM_ESTAC')
    xlsFile.write("\n" + valor)

xlsFile.close()
#Impresion de finalizado
print "Reporte generado"