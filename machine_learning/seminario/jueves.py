# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal
"""
import nltk

abre = open("/home/villacorta/Documentos/CURSO NLP URP/corpora/tradiciones_peruanas_ricardo_palma.txt", encoding="UTF-8")
base = abre.read()
base.find("INDICE")
base.find("FIN")
base = base[649:280370]

from nltk import *
from nltk.corpus import PlaintextCorpusReader

corpus_root = "/home/villacorta/Documentos/CURSO NLP URP/corpora/"
corpusesp = PlaintextCorpusReader(corpus_root, ".*")
corpusesp.fileids()
candido = corpusesp.words("candido-de-voltaire.txt")

pares = nltk.bigrams(candido)
generator = nltk.ConditionalFreqDist(pares)


def predictor(dist, palabra, num=15):
    for i in range(num):
        print(palabra, end=" ")
        palabra = dist[palabra].max()


predictor(generator, "amigo")
fichas = nltk.tokenize.word_tokenize(base)

fichas2 = nltk.tokenize.word_tokenize(base, language="spanish")

"para que el texto lo vuelevo libro nltk"
libro1 = nltk.Text(fichas2)
len(set(libro1))
libro1.count("virrey")
libro1.concordance("perú")

"tokenizar frases"
frases = nltk.tokenize.sent_tokenize(base)
len(libro1) / len(frases)

"palabras similares en el contexto"
libro1.similar("perú")

"posicion en el libro"
libro1.dispersion_plot(["Perú", "virrey"])