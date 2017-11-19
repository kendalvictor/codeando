import requests
import csv
from bs4 import BeautifulSoup
from threading import Thread
from os.path import dirname, join, realpath, exists
from os import makedirs
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='[%(levelname)s] - %(threadName)-10s : %(message)s')


def to_str(bytes_or_str):
    if isinstance(bytes_or_str, bytes):
        value = bytes_or_str.decode('utf-8')
    else:
        value = bytes_or_str
    return value


def hilado(func):
    def decorador(*args, **kwargs):
        hilo = Thread(target=func, args=args, kwargs=kwargs, name="HiloMetar")
        hilo.start()
        hilo.join()
    return decorador


@hilado
def extract_in_csv(soup, dir_save):
    metar = soup.find("div", {"class": "interpretado"})
    list_texto = metar.br.text.split() if metar else []
    list_texto = [to_str(_) for _ in list_texto]
    if list_texto:
        try:
            titulo = soup.find("td").text.replace("/", "_")
            ruta = join(dir_save, titulo + ".csv")
            with open(ruta, 'w') as resultFile:
                wr = csv.writer(resultFile, dialect='excel')
                wr.writerow(list_texto)
            print("METAR:: ", list_texto)
        except Exception as e:
            print("ERROR: ", str(e))
    print("///////////////////////")
    del soup


API_url = 'http://www.corpac.gob.pe/app/Meteorologia/tiempo/consultas/select1.php'

dicc_struct = {"aerop": ("spme", "spqt", "spyl", "spur", "spms", "spja",
                         "sppy", "sphi", "spst", "spjr", "spji", "spru",
                         "spcl", "speo", "spgm", "sphz", "spnc", "spjc",
                         "sptu", "spho", "spzo", "sphy", "spso", "spza",
                         "spjl", "spqu", "splo", "sptn", "spay", "spje",
                         "spjj", "spmf")}

dir_actual = dirname(realpath(__file__))
dir_save = join(dir_actual, "metar")
if not exists(dir_save):
    makedirs(dir_save)

for aerop in dicc_struct["aerop"]:
    response = requests.post(API_url, data={"aerop": aerop})

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        response.close()
        extract_in_csv(soup, dir_save)
    else:
        raise Exception(response.reason)


