import requests

cantidad = float(input('Ingrese cantidad a convertir: '))

respuesta = requests.get('https://api.fixer.io/latest')
respuesta_json = respuesta.json()

resultado = cantidad * respuesta_json['rates']['USD']

print('resultado: {}'.format(resultado))
