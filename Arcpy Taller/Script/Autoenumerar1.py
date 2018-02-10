import arcpy

conjuntodeentidades=arcpy.GetParameterAsText(0)
campo="id"

for entidad in conjuntodeentidades.split(';'):
    arcpy.AddField_management(entidad,campo,"TEXT","","","6")

bloquecodigo="""rec=0
def autoIncrement():
    global rec
    pStart = 1
    pInterval = 1
    if (rec == 0):
        rec = pStart
    else:
        rec += pInterval
    return str(rec).zfill(6)"""
expresion="autoIncrement()"

for entidad in conjuntodeentidades.split(';'):
    arcpy.CalculateField_management(entidad,campo,expresion,"PYTHON_9.3",bloquecodigo)

print "Proceso terminado"