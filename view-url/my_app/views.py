from django.http import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse("Hello World")


def about(request):
    return HttpResponse("I'll get a job in 10 days!")


def hello(request, first_name):
    return HttpResponse(f"Hello, {first_name}")


def addTwoNum(request, num1, num2):
    return HttpResponse(f"Sum: {num1 + num2}")
