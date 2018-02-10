import arcpy
ruta = r"D:\Publicidad cursos\Taller ArcPy\GDB"
nombre = "clasepython.gdb"
gdb=ruta+"/"+nombre
if arcpy.Exists(gdb):
  print "Ya existe el GDB"
else:
  arcpy.CreateFileGDB_management(ruta, nombre)
  
Departamentos=r"D:\Publicidad cursos\Taller ArcPy\SHP\Departamentos.shp"
NuevoDepartamento=gdb+'/'+"Departamento"
arcpy.CopyFeatures_management(Departamentos,NuevoDepartamento)


