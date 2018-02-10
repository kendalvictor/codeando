#Importar la libreria arcpy
import arcpy

#sobrescribir resultados
arcpy.env.overwriteOutput=True

#variable de entorno
arcpy.env.workspace=r"C:\compartir\Curso Python\GDB\practica.gdb"

#variables locales
infeatureclass="CentralesHidroelectricas"
outfeatureclass="CentralesHidroelectricasMayorMedia"
camposeleccionado='Potencia'
nuevocampo="UtilidadOperativa"
cadena="'Muy Buena'"

#Lista local
colector=[]

#Recuperar los registros del feature class
registros=arcpy.SearchCursor(infeatureclass)

#Recorrer los registros y llenar el colector
for registro in registros:
    valor=int(registro.getValue(camposeleccionado))
    colector.append(valor)

#Crear la función que calcula la media
def calcula_media(listaderegistros):
    sumatotal = 0
    for i in listaderegistros:
        sumatotal += i
    media = sumatotal / len(listaderegistros)
    return media

#Consultar media de la lista colector
consultamedia = calcula_media(colector)

#Expresion para seleccion
expresion= '%s >= %d'%(camposeleccionado,consultamedia)

#Seleccionar los valores que cumplen con la expresion y copiarlos a outfeatureclass
arcpy.Select_analysis(infeatureclass,"in_memory\infeatureclassmem",expresion)
arcpy.CopyFeatures_management("in_memory\infeatureclassmem",outfeatureclass)

#Eliminar el feature class temporal
arcpy.Delete_management("in_memory\infeatureclassmem")

#Adicionar campo y llenar el campo creado
arcpy.AddField_management(outfeatureclass,nuevocampo,"Text","#","#","20")
arcpy.CalculateField_management(outfeatureclass,nuevocampo,cadena,"PYTHON_9.3","#")

#Impresion en Pantalla
print "Proceso terminado"