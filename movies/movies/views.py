# Create your views here.
from django.shortcuts import render


def index(request):
    context = {"movies": ["dangal", "dhoom", "top-gun"]}
    return render(request, "movies/index.html", context)


def about(request):
    return render(request, "movies/about.html", {})
