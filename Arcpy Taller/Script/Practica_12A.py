import arcpy, os

arcpy.env.overwriteOutput=True
EspacioTrabajo=r"C:\compartir\Curso Python\GDB"
ruta=EspacioTrabajo+"\\Practica.mdb"
arcpy.env.workspace=ruta

field_list=arcpy.ListFields("CentralesHidroelectricas")

txtFile=open(os.path.join(EspacioTrabajo,"CentralesHidroelectricas.txt"),"w")
txtFile.write('Detalles de los campos de CentralesHidroelectricas'+"\n")
txtFile.write('=================================================='+"\n")

for field in field_list:
	line="Campo: {0}, Tipo: {1}, Longitud: {2} \n".format(field.name, field.type, field.length)
	txtFile.write(line)
txtFile.close()
print "fin"