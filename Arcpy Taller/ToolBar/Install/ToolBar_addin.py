import arcpy
import pythonaddins
nombre="Richard"

class ButtonClass2(object):
    """Implementation for ToolBar_addin.button (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
        pythonaddins.MessageBox("Mi primer Addin con Python","Bienvenido " + nombre,0)

class ButtonClass3(object):
    """Implementation for ToolBar_addin.button_1 (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
        pythonaddins.GPToolDialog(r"C:\Curso Python\Dia 5\Modelo\Modeloconparametros.tbx","Buffer")

class ButtonClass4(object):
    """Implementation for ToolBar_addin.button_2 (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
        proyectomxd=arcpy.mapping.MapDocument("Current")
        listadecapas=arcpy.mapping.ListLayers(proyectomxd)
        if len(listadecapas)>0:
          for capa in listadecapas:
            capa.visible=True
          arcpy.RefreshActiveView()
          arcpy.RefreshTOC()
          pythonaddins.MessageBox("Las capas se han activado","Importante",0)
        else:
          pythonaddins.MessageBox("Por favor adiciona las capas","Importante",0)

class ButtonClass5(object):
    """Implementation for ToolBar_addin.button_3 (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
        proyectomxd=arcpy.mapping.MapDocument("Current")
        listadecapas=arcpy.mapping.ListLayers(proyectomxd)
        if len(listadecapas)>0:
          for capa in listadecapas:
            capa.visible=False
          arcpy.RefreshActiveView()
          arcpy.RefreshTOC()
          pythonaddins.MessageBox("Las capas se han activado","Importante",0)
        else:
          pythonaddins.MessageBox("Por favor adiciona las capas","Importante",0)

class ButtonClass6(object):
    """Implementation for ToolBar_addin.button_4 (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
        pythonaddins.GPToolDialog(r"C:\Curso Python\Dia 5\Modelo\Modeloconparametros.tbx","GeneracionIdMasivo")