from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from links.forms import LinkForm

from links.models import Link


def index(request):
    links = Link.objects.all()
    print(links)
    context = {"links": links}
    return render(request, "links/index.html", context)


def add_link(request):
    if request.method == "POST":
        form = LinkForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse("home"))
    else:
        form = LinkForm()
    context = {"form": form}
    return render(request, "links/create.html", context)


def root_link(request, link_slug):
    link = get_object_or_404(Link, slug=link_slug)
    link.click()
    return redirect(link.url)
