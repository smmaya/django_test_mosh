from django.core.management import templates
from django.shortcuts import render
from django.http import HttpResponse


def calculate():
    x = 1
    y = 2
    return x + y


# Create your views here.
def index(request):
    return render(request, 'index.html')

def page1(request):
    return render(request, 'page1.html')

def page2(request):
    return render(request, 'page2.html')

def say_hello(request):
    return render(request, 'hello.html', {
        'name': 'Sławek',
        'calc': calculate()
    })
