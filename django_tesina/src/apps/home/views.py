from django.shortcuts import render


def index(request):
    msje_initial = "MI PRIMER RENDER ..yeshhhhhhhhhh"
    print("locals ", locals())
    return render(request, "home/index.html", locals())
