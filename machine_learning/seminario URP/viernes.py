# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 17:02:22 2017

@author: jorge.alvarado
"""

import nltk
from nltk.book import *
import unicodedata


def clean_dirt(s):
    return ''.join((c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) == 'Ll'))

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


#predictor(generator, "vieja")

"""PROBLEMAS LEXICO- MORFOLOGICOS"""

"""TOKENIZADOR"""
""" saco solo las palabras"""
fichas = nltk.tokenize.word_tokenize(base, language="spanish")
""" es una lista. Debo volverlo texto de NLTK"""
libro1 = nltk.Text(fichas)

"""hacer algunas cositas"""
"""set me saca solo las palabras que tiene el texto (sin duplicados)"""
#print(len(set(libro1)))
"""contar palabras"""
#print(libro1.count("virrey"))
"lexical diversity"""
#print(len(set(libro1)) / len(libro1))


#mayus = sorted(x for x in set(libro1) if x.istitle())
#print(mayus)

#mayus = sorted(x for x in set(libro1) if x.endswith("ción"))
#print(mayus)

#mayus = sorted(x for x in set(libro1) if x.startswith("des"))
#print(mayus)

mayus = sorted(x.lower() for x in set(libro1) if x.isalpha())
#print(mayus, mayus.__len__())

from nltk.stem.snowball import SnowballStemmer

raices = SnowballStemmer("spanish", ignore_stopwords=True)

rr = {raices.stem(t) for t in mayus}
#print(rr, rr.__len__())

#STOPWORDS:::el problema
freqrp = nltk.FreqDist(libro1)
ff = freqrp.most_common(50)

#print(ff)

from nltk.corpus import stopwords
st = stopwords.words("spanish")
#print(st, st.__len__())
st.append("paz")
"""
def filtrado(texto):
    return {w for w in texto} - set(st)


def filtrado2(texto):
    return [w for w in texto if w not in st]
"""


#rp1 = filtrado(candido)
#rp2 = filtrado2(libro1)
#fre = nltk.FreqDist(rp2)
#print(fre.most_common(50))

#POST TAGGING

#es = nltk.pos_tag(libro1)
#print(es)

#nltk.help.upenn_tagset()

#nombre = [i for i in es if i[1] == "NN"]
#print(nombre)

#TOPIC DETECTION
#print(freqrp.hapaxes())  #palabras que solo se usan una vez / forense aracteristicas unicas

#print(libro1.collocations()) #bigramas
coll = libro1.collocations()
#collo = [w for w in coll if w]
#print(collo)


freqwords = nltk.FreqDist(len(w) for w in libro1)
print("/////////////")
print(freqwords.most_common(50))

sacar = [w for w in libro1 if len(w) == 14]

print("@@@@@@@@@@@")
print(sacar)


condf = nltk.ConditionalFreqDist(
    (libro, palabra)
    for libro in corpusesp.fileids()
    for palabra in corpusesp.words(libro)
)

print("##################")
print(condf["candido-de-voltaire.txt"].most_common(20))

print("·////")
ss = condf.tabulate(samples=["el", "ella"])
print(ss, type(ss))

#TDF-IDF
import math


def tf(palabra, libro):
    return libro.count(palabra) / libro.__len__()


def n_contiene(palabra, libros):
    return sum(1 for libro in libros if palabra in libro)


def idf(palabra, libros):
    return math.log(libros.__len__() / 1 + n_contiene(palabra, libros))


def tdf_idf(palabra, libro, libros):
    return tf(palabra, libro) * idf(palabra, libros)


print(type(libro1))
print(type(candido))

abre = open(
    "/home/villacorta/Documentos/CURSO NLP URP/corpora/elquijote.txt",
    encoding="UTF-8"
)
""" lo leo en string"""
base2 = abre.read()
"""saco solo el libro"""
base2.find("hidalgo")
base2.find("LICENSE")

base2 = base2[685:2100176]


fichasq = nltk.tokenize.word_tokenize(base2, language="spanish")
""" es una lista. Debo volverlo texto de NLTK"""
libro2 = nltk.Text(fichasq)

print(type(libro1))
print(type(libro2))

librolist = [libro1, libro2]

print(n_contiene("hidalgo", librolist))
print("////////////////////////////")
print(tf("hidalgo", libro1))
print(tf("hidalgo", libro2))
print("############################")
print(tdf_idf("hidalgo", libro1, librolist))
print(tdf_idf("hidalgo", libro2, librolist))


#SENTIMENT BASIC
cls = open(
    "/home/villacorta/Documentos/CURSO NLP URP/13_CLS_Final.txt",
    encoding="UTF-8"
)

sentimientos = {}

for line in cls:
    palabra, valor = line.split("\t")
    sentimientos[palabra] = valor

print(sentimientos["paz"])
print(sentimientos["odio"])


ww = sum(int(sentimientos.get(palabra, "0").replace("\n", "")) for palabra
         in libro1)
print(ww)
sent_frases = []

frases = nltk.tokenize.sent_tokenize(base)
for i, oracion in enumerate(frases):
    palabras = nltk.word_tokenize(oracion, language="spanish")
    valsent = sum(int(sentimientos.get(palabra, "0").replace("\n", ""))
                  for palabra in palabras)
    sent_frases.append((i, valsent, palabras))


for i, val, palabras in sent_frases[:500]:
    print(i, val, palabras[:10])


def formato(tuit):
    return {palabra: True for palabra in nltk.tokenize.word_tokenize(tuit)}

pos = []
neg = []
tpos = open(
    "/home/villacorta/Documentos/CURSO NLP URP/tass14pos.txt",
    encoding="latin-1"
)
tneg = open(
    "/home/villacorta/Documentos/CURSO NLP URP/tass14neg.txt",
    encoding="latin-1"
)
print("LISTO")

for line in tpos:
    pos.append((formato(line), "pos"))

for line in tneg:
    neg.append((formato(line), "neg"))


#bases de entrenamiento
print("@@@@@@@@@@@@@@@@@@@@")
print(pos.__len__())
print(neg.__len__())

ent = pos[:1280] + neg[:1280]
test = pos[1280:] + neg[1280:]

from nltk.classify import NaiveBayesClassifier

model = NaiveBayesClassifier.train(ent)

print(model.classify(formato("Que alegria encontrar amigos")))
print(model.classify(formato("Los politico son corruptos")))
print(model.classify(formato("Ninguno de los politico es corrupto")))
print(model.classify(formato("Estoy en contra de los corruptos")))
print(model.classify(formato(
    "Pero si todos los politicos son unos angeles maravillosos")
))
print(model.classify(formato(
    "todos los profesores son unos angeles maravillosos")
))

from nltk.classify.util import accuracy

print("PRECISION ", accuracy(model, test))









