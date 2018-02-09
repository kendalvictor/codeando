import requests
from bs4 import BeautifulSoup
import pytesseract
from PIL import Image


URL_RAIZ = 'http://www.sunat.gob.pe/cl-ti-itmrconsruc'

sesion = requests.Session()

respuesta = sesion.get('{}/frameCriterioBusqueda.jsp'.format(URL_RAIZ))

soup = BeautifulSoup(respuesta.content, 'html.parser')
url_imagen = URL_RAIZ + soup.find('img').attrs['src']

respuesta_img = sesion.get(url_imagen)
archivo = open('imagen.jpg', 'wb')
archivo.write(respuesta_img.content)
archivo.close()

texto_captcha = pytesseract.image_to_string(Image.open('imagen.jpg'))
print(texto_captcha)

dni = input('ingrese nro. de DNI: ')

formulario = {
    'accion': 'consPorTipdoc',
    'razSoc': '',
    'nroRuc': '',
    'nrodoc': dni,
    'contexto': 'ti-it',
    'search1': '',
    'codigo': texto_captcha,
    'tQuery': 'on',
    'tipdoc': '1',
    'search2': dni,
    'coddpto': '',
    'codprov': '',
    'coddist': '',
    'search3': '',
}

respuesta_form = sesion.post('{}/jcrS00Alias'.format(URL_RAIZ), data=formulario)
print(respuesta_form.content)

soup = BeautifulSoup(respuesta_form.content, 'html.parser')

tabla = soup.find('table', attrs={'cellpadding': 2})

cabeceras = map(lambda e: e.text.strip(), tabla.find_all('th'))
contenidos = map(lambda e: e.text.strip(), tabla.find_all('td'))

for cabecera, contenido in zip(cabeceras, contenidos):
    print('{}: {}'.format(cabecera, contenido))
