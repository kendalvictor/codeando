import arcpy
ruta = r"D:\Publicidad cursos\Taller ArcPy\Ejecutar_Python_CMD"
nombre = "mi_gdb.gdb"
gdb=ruta+"/"+nombre
if arcpy.Exists(gdb):
  print "Ya existe el GDB"
else:
  arcpy.CreateFileGDB_management(ruta, nombre)
 