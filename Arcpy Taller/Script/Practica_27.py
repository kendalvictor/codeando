import arcpy

arcpy.env.overwriteOutput=True

registros=[('Colmena', '21', (-77.03279420699994, -12.052360990999944)),
           ('Jiron de La Union', '22', (-77.03313791899996, -12.049097341999982)),
           ('Tacna', '23', (-77.03788199899998, -12.046206414999972)),
           ('Espana', '25', (-77.04177575099999, -12.057597874999942)),
           ('Quilca', '26', (-77.04231663299998, -12.051428646999966)),
           ('Dos de Mayo', '27', (-77.04275817099995, -12.046392511999954))]
cursor=arcpy.da.InsertCursor(r"D:\Publicidad cursos\Taller ArcPy\GDB\Dia4.gdb\Estaciones",["NOM_ESTAC","COD_ESTAC","SHAPE@XY"])
for registro in registros:
	cursor.insertRow(registro)

del cursor

print "Se insertaron: " + str(len(registros)) + "registros"