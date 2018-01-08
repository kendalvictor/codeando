# coding=utf-8

from datetime import datetime
import csv
from os import path
import re
import time
import sys
import random
from threading import Thread
import logging

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import WebDriverException


#logging.basicConfig(level=logging.DEBUG,
#                    format='[%(levelname)s] - %(threadName)-10s : %(message)s')

BASE_DIR = path.dirname(path.abspath(__file__))
SCROLL_PAUSE_TIME = 1.5
SCROLL_BY_ADVANCED = 600

sys.path.append(BASE_DIR)

users_agents = [
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36"
]


chrome_options = Options()
chrome_options.add_argument("--window-size=500,900")
chrome_options.add_argument("user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36")
driver = webdriver.Chrome(chrome_options=chrome_options)
#driver.set_page_load_timeout(15)

dicc_portales = {
    'http://ojo.pe/': [
        '', 'actualidad', 'casos-del-corazon', 'ciudad', 'deportes', 'horoscopo',
        'internacional', 'locomundo', 'mascotas', 'misterios', 'ojo-show','policial',
        'salud', 'whatsapp-del-pueblo', 'ojo-videos'],
    'http://mujerpandora.com/': [
         '', 'videos', 'fotos', 'autor/mcancha/', 'noticias/te-cuento', 'amor-y-sexo', 'belleza',
         'espectaculos', 'familia', 'mistica', 'moda', 'salud', 'slam', 'trabajo'],
    'http://elshow.pe/': [
        '', 'cine', 'realitys/combate', 'espectaculos', 'realitys/esto-es-guerra', 'fotos',
        'insolito', 'musica', 'realitys', 'realitys/reto-de-campeones', 'tv'],
    'http://elbocon.pe/': [
        '', 'fotos', 'otros-deportes/basketball', 'otros-deportes/carrera-de-autos',
        'otros-deportes/contacto-wwe-y-ufc', 'futbol-peruano/copa-inca',
        'internacional/copa-libertadores', 'futbol-peruano/copa-peru',
        'internacional/copa-sudamericana', 'futbol-peruano/descentralizado',
        'realitys/reto-de-campeones', 'el-boconcito/el-idolo', 'el-boconcito/el-profe',
         'futbol-peruano', 'el-boconcito/futuros-cracks', 'el-boconcito/galeria',
         'el-boconcito/golazos', 'internacional', 'internacional/liga-de-campeones',
         'internacional/ligas-extranjeras', 'el-boconcito/nutricion', 'otros-deportes',
         'futbol-peruano/promocion-y-reservas', 'futbol-peruano/segunda-division',
         'futbol-peruano/seleccion-peruana', 'otros-deportes/surf', 'zona-del-hincha',
         'internacional/transferencias', 'otros-deportes/voley'],
    'http://diariocorreo.pe/': [
        '', 'deportes', 'noticias/arequipa', 'espectaculos', 'cultura','especiales-web',
        'edicion/cusco', 'economia','noticias/amazonas', 'noticias/ancash', 'noticias/apurimac',
         'noticias/ayacucho', 'noticias/cajamarca','noticias/chimbote', 'chiquitas', 'ciudad',
         'columnista-web', 'correo-tv', 'gastronomia', 'edicion/huancavelica', 'edicion/huancayo',
          'edicion/huanuco', 'edicion/ica', 'noticias/iquitos', 'edicion/la-libertad',
          'edicion/lambayeque','edicion/lima', 'local', 'noticias/madre-de-dios', 'miscelanea',
          'edicion/moquegua', 'mundo', 'edicion/pasco', 'peru', 'edicion/piura', 'politica', 'edicion/puno',
        'regional', 'noticias/san-martin', 'edicion/tacna', 'tema-del-dia', 'edicion/tumbes', 'noticias/ucayali',
        'noticias/whatsapp']
}


def clean_tag_v2(enlace, urlbase):
    list_enlace = enlace.replace(urlbase, '').split("/")
    return list_enlace[1 if list_enlace.__len__() > 1 else 0] if list_enlace else None


def process_data(tagg, urlbase, list_url, list_sas, list_dfp, search_article=True):
    enlace_primer_articulo = None
    tagg_analisis = tagg + "{0}marfeelads=2".format( '?' if '?' not in tagg else '&')
    list_url.append(tagg)
    print("tagg_analisis ", tagg_analisis)

    driver.get(tagg_analisis)
    time.sleep(SCROLL_PAUSE_TIME*3)

    if not driver.execute_script("return document.getElementsByClassName('mrf-madInfo')[0]"):
        try:
            driver.refresh()
            driver.delete_all_cookies()
            driver.get(tagg_analisis)
            print("NECESITO 5 SEG ADICIONALES")
            time.sleep(SCROLL_PAUSE_TIME*4)
        except Exception as e:
            print("ERROR : ", str(e))

    #Inicio de analisis
    if driver.execute_script("return document.getElementsByClassName('mrf-madInfo')[0]"):
        last_height = driver.execute_script("return document.body.offsetHeight;")
        window_height = driver.execute_script("return window.innerHeight + scrollY;")

        while True:
            time.sleep(1)
            driver.execute_script("window.scrollBy(0, {0})".format(
                SCROLL_BY_ADVANCED))

            last_height = driver.execute_script("return document.body.offsetHeight;")
            if window_height >= last_height:
                break

            window_height += SCROLL_BY_ADVANCED

        html = driver.execute_script(
            "return document.getElementsByTagName('html')[0].innerHTML")
        soup = BeautifulSoup(html, 'html.parser')
        datus = soup.find_all("div", {"class": "mrf-madInfo"})
        print("datus", type(datus), datus.__len__())

        n_sas = 0
        n_dfp = 0
        for bloque in datus:
            tipo = bloque.table.tr.td.span.text
            n_row = 0
            texto = ''
            for row in bloque.table.find_all('tr'):

                if n_row == 0:
                    n_row += 1
                    continue

                cols = row.find_all('td')
                col1 = cols[0].span.text
                col2 = cols[1].text

                if tipo.upper() == 'DFP':
                    if col1.lower() == 'slotname:':
                        list_dfp.append(col2)
                        n_dfp += 1
                elif tipo.upper() == 'SMART':
                    if col1.lower() in ['siteid:', 'pageid:', 'formatid:']:
                        texto += col1 + " " + col2 + " "
            if texto:
                list_sas.append(texto)
                n_sas += 1

        n_max = max(list_url.__len__(), list_sas.__len__(), list_dfp.__len__())

        print("SAS --> ", n_sas)
        print("DFP --> ",  n_dfp)

        list_url.extend(['']*(n_max - list_url.__len__()))
        list_sas.extend(['']*(n_max - list_sas.__len__()))
        list_dfp.extend(['']*(n_max - list_dfp.__len__()))


        if search_article:
            find_articulo = soup.find('article')
            if find_articulo:
                find_a = find_articulo.find('a')
                path_url = clean_tag_v2(tagg, urlbase)
                enlace_primer_articulo = find_a["href"]  if find_a and path_url else None

                if enlace_primer_articulo and (path_url not in enlace_primer_articulo):
                    articulos = soup.find_all('article')[:20]
                    for articulo in articulos:
                        if not articulo:
                            continue
                        if not articulo.a:
                            continue

                        enlace = articulo.a["href"]
                        path_url = clean_tag_v2(tagg, urlbase)
                        if path_url and path_url in enlace:
                            enlace_primer_articulo = enlace
                            break
            else:
                print("TAG 'ARTICLE' NO DETECTADO, posible falta de implementación en Marfeel")
    else:
        print("ESTRUCTURA DE MARFEEL NO DETECTAADA, posible falta de implementación en Marfeel")
        list_sas.append('')
        list_dfp.append('')

    driver.delete_all_cookies()
    print("==================================")
    return enlace_primer_articulo


def hilado(func):
    def decorador(*args, **kwargs):
        hilo = Thread(target=func, args=args, kwargs=kwargs, name="HiloMetar")
        hilo.start()
        hilo.join()
    return decorador


@hilado
def connection_tags(urlbase, tags):
    list_dfp = ['DFP']
    list_sas = ['SAS']
    list_url = ['URL']

    for tagg in tags:
        new_enlace = process_data(
            path.join(urlbase, tagg),
            urlbase,
            list_url, list_sas, list_dfp,
            search_article=True if tagg else False
        )
        if not new_enlace:
            continue

        if urlbase.replace('http', '') not in new_enlace:
            new_enlace = path.join(urlbase, new_enlace)

        process_data(
            new_enlace, urlbase,
            list_url, list_sas, list_dfp,
            search_article=False)

    list_master = [list_url, list_sas, list_dfp]
    list_csv = zip(*list_master)

    with open("{0}.csv".format(
        urlbase.split("/")[-2].split(".")[0]), 'w') as resultFile:
       wr = csv.writer(resultFile, dialect='excel')
       for row in list_csv:
           wr.writerow(row)


if __name__ == "__main__":
    for urlbase, tags in dicc_portales.items():
        connection_tags(urlbase, tags)




