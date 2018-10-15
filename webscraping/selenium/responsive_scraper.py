# coding=utf-8

from datetime import datetime
import csv
from os import path
from urllib.parse import urljoin
import re
import ast
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
PAUSE_TIME = 1.5
SCROLL_BY_ADVANCED = 600
sys.path.append(BASE_DIR)

chrome_options = Options()
chrome_options.add_argument("--window-size=500,900")
chrome_options.add_argument("user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36")
driver = webdriver.Chrome(
    executable_path='/home/villacorta/STORAGE/codeando/webscraping/selenium/chromedriver',
    chrome_options=chrome_options)

dicc_portales = {
    'http://diariocorreo.pe/': [
        '', 'deportes', 'noticias/arequipa', 'espectaculos', 'cultura','especiales-web',
        'edicion/cusco', 'economia','noticias/amazonas', 'noticias/ancash', 'noticias/apurimac',
         'noticias/ayacucho', 'noticias/cajamarca','noticias/chimbote', 'chiquitas', 'ciudad',
         'columnista-web', 'correo-tv', 'gastronomia', 'edicion/huancavelica', 'edicion/huancayo',
          'edicion/huanuco', 'edicion/ica', 'noticias/iquitos', 'edicion/la-libertad',
          'edicion/lambayeque','edicion/lima', 'local', 'noticias/madre-de-dios', 'miscelanea',
          'edicion/moquegua', 'mundo', 'edicion/pasco', 'peru', 'edicion/piura', 'politica', 'edicion/puno',
        'regional', 'noticias/san-martin', 'edicion/tacna', 'tema-del-dia', 'edicion/tumbes', 'noticias/ucayali',
        'noticias/whatsapp'],
    'http://elbocon.pe/': [
        '', 'fotos', 'el-boconcito/nutricion','otros-deportes/basketball', 'otros-deportes/carrera-de-autos',
        'otros-deportes/contacto-wwe-y-ufc', 'futbol-peruano/copa-inca',
        'internacional/copa-libertadores', 'futbol-peruano/copa-peru',
        'internacional/copa-sudamericana', 'futbol-peruano/descentralizado',
        'noticias/reto-de-campeones', 'el-boconcito/el-idolo', 'el-boconcito/el-profe',
         'futbol-peruano', 'el-boconcito/futuros-cracks', 'el-boconcito/galeria', 'galeria',
         'el-boconcito/golazos', 'golazo','internacional', 'internacional/liga-de-campeones',
         'internacional/ligas-extranjeras', 'otros-deportes',
         'futbol-peruano/promocion-y-reservas', 'futbol-peruano/segunda-division',
         'futbol-peruano/seleccion-peruana', 'otros-deportes/surf', 'zona-del-hincha',
         'internacional/transferencias', 'otros-deportes/voley'],
    'http://elshow.pe/': [
        '', 'cine', 'realitys/combate', 'espectaculos', 'realitys/esto-es-guerra', 'fotos',
        'insolito', 'musica', 'realitys', 'realitys/reto-de-campeones', 'tv'],
    'http://mujerpandora.com/': [
         '', 'videos', 'fotos', 'autor/mcancha/', 'noticias/te-cuento', 'amor-y-sexo', 'belleza',
         'espectaculos', 'familia', 'mistica', 'moda', 'salud', 'slam', 'trabajo'],
    'http://ojo.pe/': [
        '', 'actualidad', 'casos-del-corazon', 'ciudad', 'deportes', 'horoscopo',
        'internacional', 'locomundo', 'mascotas', 'misterios', 'ojo-show','policial',
        'salud', 'whatsapp-del-pueblo', 'ojo-videos']
}


def clean_tag_v2(enlace, urlbase):
    list_enlace = enlace.replace(urlbase, '').split("/")
    return list_enlace[1 if list_enlace.__len__() > 1 else 0] if list_enlace else None


def process_data(tagg, urlbase, list_url, list_sas, list_dfp, search_article=True):
    enlace_primer_articulo = None
    nn_pre_sas = list_sas.__len__()
    nn_pre_dfp = list_dfp.__len__()

    print("URL ----> ", tagg)
    list_url.append(tagg)
    try:
        driver.get(tagg)
        time.sleep(PAUSE_TIME)
        dicc_struct_sas = driver.execute_script("""
            var data_struct = {
                'visibles' : [],
                'pageid': 0,
                'siteid': 0
            };

            [].slice.call(document.querySelectorAll("script:not([src]")).filter((script) => {
                buscando = script.innerHTML.match(/(\w+)/g);
                if (buscando && script.innerHTML.trim().indexOf("sas.cmd.push") == 0 && window.getComputedStyle(script.parentNode).display != 'none') {
                    data_struct.visibles.push(buscando[6]);
                    return script
                }else{
                    posicion_siteid = buscando.indexOf('siteId');
                    posicion_pageid = buscando.indexOf('pageId');
                    if(posicion_siteid >= 0){
                        data_struct.siteid = buscando[posicion_siteid + 1]
                    }
                    if(posicion_pageid >= 0){
                        data_struct.pageid = buscando[posicion_pageid + 1]
                    }
                }
            });
            return data_struct
        """)

        texto = ''
        visibles = []
        for k, v in dicc_struct_sas.items():
            if not isinstance(v, list):
                texto += k + " : " + str(v) + " "
            else:
                visibles = v

        list_sas.append(texto)
        list_sas.extend([str(num) for num in visibles])

        dicc_struct_dfp = driver.execute_script("""
            var data_struct = {
                'codigos' : [],
                'code_mayor': []
            };

            [].slice.call(document.querySelectorAll("script:not([src]")).filter((script) => {
                if (script.innerHTML.trim().indexOf("googletag.cmd.push") == 0) {
                    let buscando = script.innerHTML.match(/(\w+)/g);
                    if(buscando.length < 11){
                        code = buscando.slice(6).join('-');
                        data_struct.codigos.push(code)
                    }else{
                        let buscando2 = script.innerHTML.match(/googletag.defineSlot\((.+).addService/g);
                        data_struct.code_mayor = buscando2
                    }
                }
            });
            return data_struct
        """)

        lista_codigos = [_.replace('-', '').replace('_', '') for _ in dicc_struct_dfp["codigos"]]

        for _ in dicc_struct_dfp["code_mayor"]:
            str_lista = _.replace("googletag.defineSlot(", "[").replace(").addService", "]")
            new_lista = ast.literal_eval(str_lista)

            if new_lista[-1].replace('-', '').replace('_', '') in lista_codigos:
                list_dfp.append(new_lista[0])

        nn_url = list_url.__len__()
        nn_sas = list_sas.__len__()
        nn_dfp = list_dfp.__len__()

        n_max = max(nn_url, nn_sas, nn_dfp)
        print("SAS : ", nn_sas - 1 - nn_pre_sas)
        print("DFP : ", nn_dfp - nn_pre_dfp)
        list_url.extend(['']*(n_max - nn_url))
        list_sas.extend(['']*(n_max - nn_sas))
        list_dfp.extend(['']*(n_max - nn_dfp))


        if search_article:
            patron = re.compile("[0-9]+")
            html = driver.execute_script(
            "return document.getElementsByTagName('html')[0].innerHTML")
            soup = BeautifulSoup(html, 'html.parser')

            articulo = soup.find("article") or \
                       soup.find("div", {"class": "share-article"}) or \
                       soup.find("figure") or \
                       soup.find("h2")
            if articulo:
                find_a = articulo.find('a')
                path_url = clean_tag_v2(tagg, urlbase)
                if find_a:
                    enlace_primer_articulo = (
                        find_a["href"] if 'href' in find_a.attrs else find_a["data-href"]) \
                        if find_a and path_url else None

                if not find_a or not enlace_primer_articulo or \
                    (enlace_primer_articulo and (
                        path_url not in enlace_primer_articulo or not patron.search(enlace_primer_articulo))
                    ) :
                    salta = False
                    articulos = soup.find_all("article")[:20] or \
                                soup.find_all("div", {"class": "share-article"})[:20] or \
                                soup.find_all("figure")[:20] or \
                                soup.find_all("h2")[:20]

                    for articulo in articulos:
                        for link in articulo.find_all('a')[:3]:
                            enlace = (
                            link["href"] if 'href' in link.attrs else link["data-href"]) \
                            if link else None

                            if enlace and path_url in enlace and patron.search(enlace):
                                enlace_primer_articulo = enlace
                                salta = True
                                break
                        if salta:
                            break

            else:
                print("ARTICULO NO DETECTADO")
                list_sas.append('')
                list_dfp.append('')


        driver.delete_all_cookies()
    except Exception as e:
        list_sas.append('')
        list_dfp.append('')
        print("ERROR : ", str(e))

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
            new_enlace = urljoin(urlbase, new_enlace)

        process_data(
            new_enlace, urlbase,
            list_url, list_sas, list_dfp,
            search_article=False)


    list_master = [list_url, list_sas, list_dfp]
    list_csv = zip(*list_master)

    with open("{0}.csv".format(
        urlbase.split("/")[-2].split(".")[0] + "_responsive"), 'w') as resultFile:
       wr = csv.writer(resultFile, dialect='excel')
       for row in list_csv:
           wr.writerow(row)


if __name__ == "__main__":
    for urlbase, tags in dicc_portales.items():
        connection_tags(urlbase, tags)


