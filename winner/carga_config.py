#importamos 
import ConfigParser
#instanciamos
config= ConfigParser.RawConfigParser()
#defino nombre de archivo
config_file= 'config'
#leo confi
config.read(config_file)
#cargo la data
server=config.get("base_de_datos","servidor")
user=config.get("base_de_datos","usuario")
pwd=config.get("base_de_datos","clave")
puerto=config.get("base_de_datos","puerto")

print "Datos para conectar a la base:"
print server
print user
print pwd
print puerto

raw_input("\nPresiona una tecla para salir......")

