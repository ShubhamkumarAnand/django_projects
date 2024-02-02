from django.shortcuts import render

from links.models import Link


# Create your views here.
def index(request):
    links = Link.objects.all()
    print(links)
    context = {"links": links}
    return render(request, "links/index.html", context)
