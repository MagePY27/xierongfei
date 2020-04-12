from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("<p1>hello,django xrf</p1>")
def index2(request):
    return HttpResponse("<p1>hello,django xrf 2</p1>")