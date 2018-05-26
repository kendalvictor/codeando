# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from textblob import TextBlob as tb
from .tfidf import tfidf
from .models import Curriculum, DataCurriculum
from .utils import clean_word


def home(request):
    print ('hola mundo')
    curriculums = DataCurriculum.objects.all()
    # curriculum.tokenized_job_section = ''.join([curriculum.tokenized_job_section for curriculum in curriculums])
    bloblist = [tb(''.join(curriculum.tokenized_job_section)) for curriculum in curriculums]
    for i, blob in enumerate(bloblist):
        print("Top words in document {}".format(i + 1))
        scores = {word: tfidf(word, blob, bloblist) for word in blob.words}
        sorted_words = sorted(scores.items(), key=lambda x: x[1], reverse=True)
        for word, score in sorted_words[:20]:
            print("\tWord: {}, TF-IDF: {}".format(word, round(score, 5)))
    return render(request, 'home.html', locals())


def clean(request):
    curriculums = Curriculum.objects.all()[:5]
    clean_list = [clean_word(curriculum.algoritmo_texto) for curriculum in curriculums]
    for i, list in enumerate(clean_list):
        print("Words in documents {0}::::::::::::::".format(i + 1))
        print(list)

    return render(request, 'clean.html', locals())


def generate_tokenized_words(request):
    curriculums = DataCurriculum.objects.all()
    clean_list = [clean_word(curriculum.seccion_laboral) for curriculum in curriculums]
    for curriculum in curriculums:
        curriculum.tokenized_job_section = clean_word(curriculum.seccion_laboral)
        print ('clean_word(curriculum.seccion_laboral)', clean_word(curriculum.seccion_laboral))
        curriculum.save()
    return render(request, 'clean.html', locals())


def generate_new_text(request):
    curriculums = DataCurriculum.objects.all()
    for curriculum in curriculums:
        curriculum.new_job_text = ' '.join(eval(curriculum.tokenized_job_section))
        curriculum.save()
    return render(request, 'clean.html', locals())



def find_most_similar_document(request):
    '''
        Encontraremos el documento mas similar
    '''
    name_document = 'alejand.doc'







