#Listar el nombre y tipo de campos del feature class CentralesHidroelectricas:
import arcpy
arcpy.env.workspace =r"C:\compartir\Curso Python\GDB\practica.gdb"
# Rellenar los espacios en blanco
field_list = arcpy.ListFields("CentralesHidroelectricas")
for field in field_list:
    print "Campo: "+ field.name, "Tipo: "+field.type