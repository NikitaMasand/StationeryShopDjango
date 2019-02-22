from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse('hello world') #returned plain text to the browser..to let django know about this function, we add a
    #path or mapping in urls list in urls.py


def new(request):
    return HttpResponse('new product')
