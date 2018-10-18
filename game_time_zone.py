from pytz import timezone
from datetime import datetime

local_tz = timezone('America/Lima')
fecha_recibida_string = '2017-10-18 11:12:36'
fecha = local_tz.localize(
    datetime.strptime(fecha_recibida_string, '%Y-%m-%d %H:%M:%S')
)

#add format  RFC-822
fecha = fecha.strftime('%a, %d %b %Y %H:%M:%S %z')
print(fecha)


