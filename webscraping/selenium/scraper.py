# coding=utf-8

from datetime import datetime
import csv
import os
import re
import time
import sys

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SCROLL_PAUSE_TIME = 1.5
SCROLL_BY_ADVANCED = 600

sys.path.append(BASE_DIR)


mobile_emulation = {
    "deviceMetrics": { "width": 720, "height": 900, "pixelRatio": 3.0 },
    "userAgent": "Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 5 \
    Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 \
    Mobile Safari/535.19" }
chrome_options = Options()
chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
driver = webdriver.Chrome(chrome_options=chrome_options)

if __name__ == "__main__":
    list_dfp = ['DFP']
    list_sas = ['SAS']
    list_url = ['URL']
    urlbase = 'https://diariocorreo.pe/'
    tags = ['politica', 'miscelanea', 'gastronomia', 'deportes', 'economia']

    for tag in tags:
        driver.get(urlbase + tag + "/?marfeelads=2")
        list_url.append(urlbase + tag)

        last_height = driver.execute_script(
            "return document.body.offsetHeight;")
        window_height = driver.execute_script(
            "return window.innerHeight + scrollY;")

        while True:
            time.sleep(SCROLL_PAUSE_TIME)
            driver.execute_script("window.scrollBy(0, {0})".format(
                SCROLL_BY_ADVANCED))
            last_height = driver.execute_script(
                "return document.body.offsetHeight;")

            if window_height >= last_height:
                break
            window_height += SCROLL_BY_ADVANCED

        html = driver.execute_script(
            "return document.getElementsByTagName('html')[0].innerHTML")
        soup = BeautifulSoup(html, 'html.parser')
        datus = soup.find_all("div", {"class": "mrf-madInfo"})

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
                elif tipo.upper() == 'SMART':
                    if col1.lower() in ['siteid:', 'pageid:', 'formatid:']:
                        texto += col1 + " " + col2 + " "
            if texto:
                list_sas.append(texto)


        n_max = max(list_url.__len__(), list_sas.__len__(), list_dfp.__len__())
        list_url.extend(['']*(n_max - list_url.__len__()))
        list_sas.extend(['']*(n_max - list_sas.__len__()))
        list_dfp.extend(['']*(n_max - list_dfp.__len__()))

    list_master = [list_url, list_sas, list_dfp]
    list_csv = zip(*list_master)

    with open("analisis_marfeel.csv", 'w') as resultFile:
       wr = csv.writer(resultFile, dialect='excel')
       for row in list_csv:
           wr.writerow(row)






