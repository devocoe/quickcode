from django.shortcuts import render
from .models import Code, Language

# Create your views here.


def index(request):
    return render(request, "index.html")


def explore(request):
    languages = Language.objects.all()
    return render(request, "explore.html", {"languages": languages})


def language(request, slug):
    language = Language.objects.get(slug=slug)
    languages = Language.objects.all()
    codes = Code.objects.filter(language=language)
    return render(request, "language.html", {"codes": codes, "language": language, "languages": languages})
