#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 22 14:06:36 2017
@author: villacorta
"""
import requests
from bs4 import BeautifulSoup
import re


def apply_soup(dominio, busqueda):
    url = dominio + busqueda
    page = requests.get(url)
    soup = None
    if page.status_code == 200:
        soup = BeautifulSoup(page.content, 'html.parser')
        page.close()
    return soup


dominio = "http://sofifa.com/"

terminos = {}
for letra in list(map(chr, range(67, 91))):

    print("/////////////// ", letra, "/////////////// ")
    busqueda = "?pais=Per%FA&tipobusqueda=1&inicial=" + letra + "&Submit=Mostrar"
    soup = apply_soup(dominio, busqueda)
    if soup:
        lista_de_palabras = soup.find("div", {"id": "lista_de_palabras"})
        cols = lista_de_palabras.table.tr
        for data in cols:
            enlaces = data.find_all("a")
            for enlace in enlaces:
                terminos[enlace.text] = enlace["href"]
    else:
        print("ERROR DE ACCESO")
    break

for k, v in terminos.items():
    newsoup = apply_soup(dominio, v)
    if newsoup:
        significado = ""
        palabra = newsoup.find("span", {"class": "palabra"})
        apliregex = re.split("\((\w|\.|\s|;|\/)*\)", palabra.parent.text, 5)
        if apliregex.__len__() == 1:
            list_text = apliregex[0].split(",")
            if list_text.__len__() == 1:
                significado = list_text[0]
            elif list_text.__len__() > 1:
                significado = list_text[1]
        elif apliregex.__len__() > 1:
            significado = apliregex[2]
        significado = significado.replace('"', '').replace('1)', '')
        newregex = re.split(
            "(\)|\(| y | o | aunque | \W|\W )",  significado, 5)
        print(k, " --> ", significado, " :: ",newregex[0].strip())
        print("&&&&&&&&&&&&&&&&&&&&")
    else:
        print("ERROR DE ACCESO")