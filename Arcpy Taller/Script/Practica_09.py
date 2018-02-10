import arcpy

arcpy.env.workspace=r"C:\compartir\Curso Python\GDB\practica.gdb"

desc=arcpy.Describe("CentralesHidroelectricas")

print "Nombre: {0}\nTipo de geometria: {1}\nTipo de dato: {2}".format(desc.name, desc.shapeType, desc.datasetType)

for field in desc.fields:
	print "Campo: {0}\nTipo de dato:{1}| Longitud:{2} | Campo requerido:{3} | Campo nulo:{4}| Alias:{5}".format(field.name,field.type,field.length,field.required,field.isNullable,field.aliasName)

descGDB=arcpy.Describe(arcpy.env.workspace)
print "GDB Tipo: {0} Version: {1} Ruta: {2}".format(descGDB.workspaceType,descGDB.release,descGDB.path)