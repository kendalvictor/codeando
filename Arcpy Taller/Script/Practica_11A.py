# Listar datasets:
import arcpy
arcpy.env.workspace=r"C:\compartir\Curso Python\GDB\mundo.gdb"
# Rellenar los espacios en blanco
dataset_list = arcpy.ListDatasets()
for dataset in dataset_list:
    print dataset