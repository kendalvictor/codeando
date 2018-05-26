# -*- coding: utf-8 -*-
import re
import nltk
import unicodedata


def clean_dirt(s):
    return ''.join((c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) == 'Ll'))


def clean_word(texto):
    patron_alf_num = re.compile(r'\w+')
    salto_linea = re.compile('[\n]')
    patron_espacios = re.compile('[\s]')
    generator_texto = [clean_dirt(palabra.lower()) for palabra in nltk.word_tokenize(texto.replace("\\n", ""))
                       if patron_alf_num.search(palabra) and clean_dirt(palabra.lower()).__len__() > 3]
    return generator_texto


"""
def clean_word2(texto):
    patron_alf_num = re.compile(r'\w+')
    salto_linea = re.compile('[\n]')
    patron_espacios = re.compile('[\s]')
    generator_texto = [palabra.lower() for palabra in texto.replace("\\n", "").split()
                       if patron_alf_num.search(palabra) and palabra.lower().__len__() > 3]
    return generator_texto


def clean_word3(texto):
    patron_alf_num = re.compile(r'\w+')
    salto_linea = re.compile('[\n]')
    generator_texto = (clean_dirt(palabra.lower()) for palabra in nltk.word_tokenize(salto_linea.sub("", texto))
                       if patron_alf_num.search(palabra) and clean_dirt(palabra.lower()).__len__() > 3)
    return generator_texto
"""

