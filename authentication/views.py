import re
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def register(request):
    print(request)
    return HttpResponse('This is my response')

def login(request):
    return HttpResponse('This is my login message')
