from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('<center><h1>this is homepage</h1></center>')
