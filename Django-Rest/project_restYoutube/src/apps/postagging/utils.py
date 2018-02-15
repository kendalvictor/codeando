# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
from unicodedata import normalize, category


def extract_significado(apliregex):
    significado = ""
    if apliregex.__len__() == 1:
        list_text = apliregex[0].split(",")
        if list_text.__len__() == 1:
            significado = list_text[0]
        elif list_text.__len__() > 1:
            significado = list_text[1]
    elif apliregex.__len__() > 1:
        significado = apliregex[2]

    return significado.replace('"', '').replace('1)', '')


def apply_soup(dominio, busqueda, tipo_parseo):
    url = dominio + busqueda
    page = requests.get(url)
    soup = None
    if page.status_code == 200:
        soup = BeautifulSoup(page.content, tipo_parseo)
        page.close()
    return soup


def clean_phrase(word):
    return ''.join((_ for _ in normalize('NFD', word) if category(_) != 'Mn'))


def clean_word(word):
    return ''.join((_ for _ in normalize('NFD', word) if category(_) == 'Ll'))


def extract_word(elem, dicc_tags):
    if not elem.text and {"wd", "pos", "lem"}.issubset(set(elem.attrib)):
        if elem.attrib["wd"].replace("_", "").isalpha():
            set_words = {elem.attrib["wd"], elem.attrib["lem"]}
            if elem.tag not in ["c", "i", "p", "r", "s"	]:
                try:
                    set_words.update({
                        clean_word(elem.attrib["wd"].lower()),
                        clean_word(elem.attrib["lem"].lower())
                    })
                except:
                    pass
            return dicc_tags[elem.tag[0]], set_words


def parser_iter_clean(context, dicc_words, tup_tags, dicc_transicion):
    previus = None
    dicc_tags = dict(tup_tags)
    for event, elem in context:
        if event == "start" and elem.tag == "sentence":
            previus = None

        tuppla = extract_word(elem, dicc_tags) if event == "end" else None
        if tuppla:
            #CARGANDO DATA PARA LA MATRIZ DE EMISION
            for word in tuppla[1]:
                if word not in dicc_words:
                    dicc_words[word] = {v: 0 for k, v in tup_tags}
                    dicc_words[word]["cant"] = 1
                else:
                    dicc_words[word]["cant"] += 1
                dicc_words[word][tuppla[0]] += 1

            # CARGANDO DATA PARA LA MATRIZ DE TRANSICION
            if previus:
                if "cant" not in dicc_transicion[previus]:
                    dicc_transicion[previus]["cant"] = 1
                else:
                    dicc_transicion[previus]["cant"] += 1
                dicc_transicion[previus][tuppla[0]] += 1
            previus = tuppla[0]

        for ancestor in elem.xpath('ancestor-or-self::*'):
            while ancestor.getprevious() is not None:
                del ancestor.getparent()[0]
    del context


def show_parse_xml(context):
    indent = []
    for action, elem in context:
        if action == 'start':
            print('{0}<{1}{2}>'.format(
                ''.join(indent),
                elem.tag,
                '/' if not len(elem) else ''))
            indent.append('  ')
        else:
            indent.pop()
            if len(elem):
                print('{}</{}>'.format(''.join(indent), elem.tag))

