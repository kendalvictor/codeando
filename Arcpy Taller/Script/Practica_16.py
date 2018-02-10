import arcpy
import os

arcpy.env.overwriteOutput=True
#gdb=arcpy.GetParameterAsText(1)
EspacioTrabajo = sys.argv[1]
featureclass=sys.argv[2]
tipo=sys.argv[3]

reporte="reporte"+tipo
#arcpy.env.workspace = os.path.join(EspacioTrabajo, gdb)

# Crear lista del featureclass.
field_list = arcpy.ListFields(featureclass)

# Abrir el archivo de texto para escribir los resultados
txtFile = open(os.path.join(EspacioTrabajo,reporte), "w")
txtFile.write('Reporte de los campos' + "\n")
txtFile.write("======================" + "\n")

# Recorrer la lista de campos, construir la cadena que contiene propiedades de campo
# y escribir la cadena en el archivo de texto
for field in field_list:
    line = "Campo: {0},  Tipo: {1}, Longitud: {2}\n".format(field.name,
                                                            field.type,
                                                            field.length)
    txtFile.write(line)

# Cerrar el archivo de texto
txtFile.close()
print "Script completado"