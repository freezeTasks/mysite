from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('<center><h1>this is home page</h1></center>')
