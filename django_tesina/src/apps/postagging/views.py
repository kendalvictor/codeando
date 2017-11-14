from django.shortcuts import render


def cargar(request):
    return render(request, "postagging/load_words.html", locals())


def listar(request):
    return render(request, "postagging/list_words.html", locals())


def xml_sync(request):
    return render(request, "postagging/xml_sync.html", locals())
