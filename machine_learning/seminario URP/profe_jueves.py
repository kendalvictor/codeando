# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 17:02:22 2017

@author: jorge.alvarado
"""

import nltk
from nltk.book import *

"""CREACION DE CORPORAS"""
"ojo con el encoding y el decoding para español"
abre = open("/home/villacorta/Documentos/CURSO NLP URP/corpora/tradiciones_peruanas_ricardo_palma.txt", encoding="UTF-8")
""" lo leo en string"""
base = abre.read()
"""saco solo el libro"""
base.find("INDICE")
base.find("FIN")
base = base[649:280370]

"""vamos a crear un corpus"""
from nltk.corpus import PlaintextCorpusReader

corpus_root = "/home/villacorta/Documentos/CURSO NLP URP/corpora/"
corpusesp = PlaintextCorpusReader(corpus_root, ".*")
"""para ver que archivos quedaron"""
corpusesp.fileids()
"""traer el texto de uno"""
candido = corpusesp.words("candido-de-voltaire.txt")

"""FONETICO Y DE GENERACION"""
"generar texto aleatorio, o mejor, crear un predictor de texto"
pares = nltk.bigrams(candido)
generator = nltk.ConditionalFreqDist(pares)

"de pronto cambiar a 3 para hablar de predictor de texto"


def predictor(dist, palabra, num=15):
    for i in range(num):
        print(palabra, end=" ")
        palabra = dist[palabra].max()


predictor(generator, "vieja")

"""PROBLEMAS LEXICO- MORFOLOGICOS"""

"""TOKENIZADOR"""
""" saco solo las palabras"""
fichas = nltk.tokenize.word_tokenize(base)
fichas2 = nltk.tokenize.word_tokenize(base, language="spanish")
""" es una lista. Debo volverlo texto de NLTK"""
libro1 = nltk.Text(fichas)

"""hacer algunas cositas"""
"""set me saca solo las palabras que tiene el texto (sin duplicados)"""
len(set(libro1))
"""contar palabras"""
libro1.count("virrey")
"lexical diversity"""
len(set(libro1)) / len(libro1)

"tokenizar frases. Ojo, toca usar el string, no la lista"""
frases = nltk.tokenize.sent_tokenize(base)
len(libro1) / len(frases)

"""ahora si hacer más cositas. Encontrar citas"""
libro1.concordance("perú")
"""ahora miremos palabras similares en el contexto"""
libro1.similar("perú")
libro1.similar("virrey", num=10)
"""posiciones en el libro"""
libro1.dispersion_plot(["Perú", "virrey"])
