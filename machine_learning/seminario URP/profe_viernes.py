# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 17:02:22 2017

@author: jorge.alvarado
"""
from nltk.book import *

import nltk

"""CREACION DE CORPORAS"""
"ojo con el encoding y el decoding para español"
abre = open(
    "/home/villacorta/Documentos/CURSO NLP URP/corpora/tradiciones_peruanas_ricardo_palma.txt",
    encoding="UTF-8")
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
libro1 = nltk.Text(fichas2)

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

"limpieza de tokens"
sorted(x for x in set(libro1) if x.istitle())

sorted(x for x in set(libro1) if x.endswith("ción"))

sorted(x for x in set(libro1) if x.startswith("des"))

set(token.lower() for token in libro1 if token.isalpha())

len(set(token.lower() for token in libro1 if token.isalpha()))
len(set(libro1))

"stemming"
from nltk.stem.snowball import SnowballStemmer

raices = SnowballStemmer("spanish")

raizpalma = [raices.stem(t) for t in fichas2]

comienzos = set(raizpalma)

print(comienzos)

len(comienzos)
len(set(fichas2))

raices = SnowballStemmer("spanish", ignore_stopwords=True)

"STOPWORDS"
"el problema"
freqrp = nltk.FreqDist(libro1)
freqrp.most_common(50)

"soluciones?"

from nltk.corpus import stopwords

stopwords.words("spanish")

len(stopwords.words("spanish"))

"agregar stopword"
misstop = stopwords.words("spanish") + ["paz"]

stopwords.words()

"remover los stopwords"
filtra = [word for word in fichas2 if word not in misstop]


def filtrado(texto):
    filtrados = [word for word in texto if word not in misstop]
    return (filtrados)


rp1 = filtrado(candido)
rp2 = filtrado(libro1)

freqnew = nltk.FreqDist(rp2)
freqnew.most_common(50)

freqnew2 = nltk.FreqDist(rp1)
freqnew2.most_common(50)

"POS- TAGGING"
es = nltk.pos_tag(libro1)
print(es)
nltk.help.upenn_tagset()
nombres = [item for item in es if item[1] == "NN"]
print(set(nombres))

"TOPIC DETECTION- KEYWORDS OPALABRAS IMPORTANTES"

freqnew.hapaxes()

libro1.collocations()

freqwords = nltk.FreqDist(len(w) for w in libro1)
freqwords.most_common(30)
sacar = [word for word in libro1 if len(word) == 14]
print(sacar)

condf = nltk.ConditionalFreqDist(
    (libro, palabra)
    for libro in corpusesp.fileids()
    for palabra in corpusesp.words(libro))

condf["candido-de-voltaire.txt"].most_common(20)
condf.tabulate(samples=["él", "ella"])
type(condf)
