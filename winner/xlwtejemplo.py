# Ejemplo de creacion de hoja Excel
#xlwt, xlrd y xlutils.
import xlwt
from datetime import datetime
style0 = xlwt.easyxf('font: name Times New Roman, colour black, bold on')
style1 = xlwt.easyxf('',num_format_str='DD-MMM-YY')
wb = xlwt.Workbook()
ws = wb.add_sheet('A Test Sheet',cell_overwrite_ok=True)
ws.write(0, 0, 'Test', style0)
ws.write(1, 0, datetime.now(), style1)
ws.write(2, 0, 4)
ws.write(2, 1, 1)
ws.write(2, 2, xlwt.Formula("A3+B3"))
wb.save('example.xls')
