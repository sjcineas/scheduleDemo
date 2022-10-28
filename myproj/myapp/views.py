from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(index):
    return HttpResponse('<h1>hello yall</h1>')