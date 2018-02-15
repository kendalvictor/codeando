import re
from os import listdir, path, walk
from io import TextIOWrapper, StringIO
import glob
from lxml import etree

from django_bulk_update.helper import bulk_update
from django.http import JsonResponse, HttpResponse
from rest_framework.views import APIView
from django.db import transaction
from django.conf import settings

from ..models import PalabraDialecto, DirectorioAncora, PalabraCorpus, TagCorpus
from ..utils import (apply_soup, parser_iter_clean, extract_word,
                     clean_word, show_parse_xml, clean_phrase,
                     extract_significado)


class ExtraerAPIView(APIView):
    def put(self, request):
        data = {'proceso': None}
        error, status = '', 200
        print(request.__dir__())
        bulk_terminos = []
        try:
            if request.is_ajax():
                dominio = "http://www.jergasdehablahispana.org/"

                # DETECTO LOS TERMINOS YA GUARDADOS
                terminos_guardados = PalabraDialecto.objects.values(
                    "palabra", "significado")
                dicc_terminos = {
                    d["palabra"]: d["significado"]
                    for d in terminos_guardados
                }
                print("TERMINOS YA EXISTENTES", dicc_terminos.__len__())

                # INICIO DEL SCRAPEO DE LA WEB
                terminos = {}
                for letra in list(map(chr, range(65, 91))):
                    busqueda = "?pais=Per%FA&tipobusqueda=1&inicial="\
                               + letra + "&Submit=Mostrar"
                    soup = apply_soup(dominio, busqueda, 'html.parser')
                    lista_de_palabras = soup.find(
                        "div", {"id": "lista_de_palabras"}) if soup else None

                    if lista_de_palabras:
                        print("////////// ", letra, "////////// ")
                        cols = lista_de_palabras.table.tr
                        for datac in cols:
                            for enlace in datac.find_all("a"):
                                if enlace.text not in dicc_terminos:
                                    terminos[enlace.text] = enlace["href"]

                # INICIO DEL GUARDADO DE LOS TERMINOS NUEVOS
                print("INICIO DE EXTRACCION DE SIGNIFICADOS:::::: ")
                for k, v in terminos.items():
                    newsoup = apply_soup(dominio, v, 'html.parser')
                    palabra = newsoup.find(
                        "span", {"class": "palabra"}) if newsoup else None
                    if palabra:
                        significado = extract_significado(
                            re.split("\((\w|\.|\s|;|\/)*\)",
                                     palabra.parent.text, 5)
                        )
                        newregex = re.split(
                            "(\)|\(| y | o | aunque | \W|\W )",
                            significado, 5)
                        signifi = newregex[0].strip()
                        if signifi.__len__() > 100:
                            signifi = signifi[:100]

                        if newregex[0].strip():
                            set_select = {k, clean_phrase(k)}
                            for palabro in set_select:
                                bulk_terminos.append(
                                    PalabraDialecto(
                                        palabra=palabro,
                                        significado=signifi
                                    )
                                )
                                print(palabro, " --> ", signifi)
                            print("&&&&&&&&&&&&&&&&&&&&")

                print("COMENZARA EL BULK")
                with transaction.atomic():
                    if bulk_terminos:
                        PalabraDialecto.objects.bulk_create(bulk_terminos)

                data["proceso"] = True
        except Exception as e:
            error = str(e) + " (SE INTENTARA GUARDAR LOS DATOS YA CAPTADOS) "
            if bulk_terminos:
                PalabraDialecto.objects.bulk_create(
                    bulk_terminos
                )
            print("ERROR::: ", error)

        status = 500 if error else 200
        return JsonResponse(data, status=status, reason=error)


class SyncAPIView(APIView):
    tup_tags = (
        ("n", "noun"),
        ("a", "adj"),
        ("d", "det"),
        ("v", "verb"),
        ("c", "conj"),
        ("i", "inter"),
        ("p", "pron"),
        ("r", "adv"),
        ("s", "prep"),
        ("f", "adv"),
        ("z", "noun"),
        ("w", "noun"),
    )

    def put(self, request):
        data = {'proceso': None, 'msje': ''}
        error, status = '', 200
        print(request.__dir__())
        try:
            if request.is_ajax():
                media_root = settings.MEDIA_ROOT
                ruta = media_root + "/xml/ancora/"
                subdirrs = [dirr for dirr in listdir(ruta)
                            if path.isdir(path.join(ruta, dirr))]

                print("()()()()()()()()INICIOOOOOOOOOOO()()()()()()()")
                cant = 1
                tags_select = set(el[1] for el in self.tup_tags)

                for subdirr in subdirrs:
                    dicc_words = {}
                    dicc_transicion = {
                        tag: {_: 0 for _ in tags_select}
                        for tag in tags_select
                    }
                    ancor, boool = DirectorioAncora.objects.get_or_create(
                        nombre=subdirr)
                    print("GET OR CREATE", ancor, boool)
                    print("##########################")
                    print("########## ", subdirr)

                    if not ancor.procesado:
                        print("##########################")
                        for root in glob.iglob(path.join(
                                ruta, subdirr, "*.xml"), recursive=True):
                            workfile = open(root, "rb").read()
                            xml_text = etree.XML(workfile)
                            context = etree.iterwalk(
                                xml_text,
                                events=('start', 'end')
                            )
                            parser_iter_clean(
                                context, dicc_words,
                                self.tup_tags,
                                dicc_transicion
                            )
                            xml_text.clear()
                            print(cant, root)
                            cant += 1

                        with transaction.atomic():
                            self._save_emision(dicc_words)
                            self._save_transicion(dicc_transicion)
                            ancor.procesado = True
                            ancor.save() 

                    else:
                        data['msje'] += 'Directorio ' \
                                        + subdirr + 'ya procesado'

        except Exception as e:
            error = str(e)
            print("ERROR::::: ", error)
        else:
            print("()()()()()()()()FINNNNNNNNNNNNNN")
            print(data['msje'])

        status = 500 if error else 200
        return JsonResponse(data, status=status, reason=error)

    def _save_emision(self, dicc_words):
        list_bulk = []
        palabras = PalabraCorpus.objects.values_list("nombre", flat=True)
        palabras_existen = PalabraCorpus.objects.filter(nombre__in=dicc_words)
        palabras_nuevas = {k: v for k, v in dicc_words.items() if k not in
                           palabras}

        for p in palabras_existen:
            for tag, val in dicc_words[p.nombre].items():
                if tag != "nombre":
                    setattr(p, tag, getattr(p, tag) + val)
                else:
                    print("palabra existente: ", val)

        bulk_update(palabras_existen, exclude_fields=['nombre'])
        print("----------------------------------------------")
        print("TERMINO ACTUALIZACION  DE PALABRAS EXISTENTES")

        print(dicc_words.__len__())
        for palabro, dicc in palabras_nuevas.items():
            dicc["nombre"] = palabro
            list_bulk.append(PalabraCorpus(**dicc))

        if list_bulk:
            PalabraCorpus.objects.bulk_create(list_bulk)

        print("----------------------------------------------")
        print("TERMINO CREACION  DE PALABRAS NUEVAS")

    def _save_transicion(self, dicc_transicion):
        dicc_nombres = {
            "noun": "sustantivo",
            "adj": "adjetivo",
            "det": "determinante",
            "verb": "verbo",
            "conj": "conjuncion",
            "inter": "interseccion",
            "pron": "pronombre",
            "adv": "adverbio",
            "prep": "preposicion"
        }
        list_bulk = []
        tagss = TagCorpus.objects.values_list("codigo", flat=True)
        tag_existen = TagCorpus.objects.filter(codigo__in=dicc_transicion)
        tag_nuevos = {k: v for k, v in dicc_transicion.items() if k not in
                      tagss}

        for p in tag_existen:
            for tag, val in dicc_transicion[p.codigo].items():
                if tag not in ["nombre", "codigo"]:
                    setattr(p, tag, getattr(p, tag) + val)

        bulk_update(tag_existen, exclude_fields=['nombre', "codigo"])

        for tag, dicc in tag_nuevos.items():
            dicc["codigo"] = tag
            dicc["nombre"] = dicc_nombres[tag]
            list_bulk.append(TagCorpus(**dicc))

        if list_bulk:
            TagCorpus.objects.bulk_create(list_bulk)




