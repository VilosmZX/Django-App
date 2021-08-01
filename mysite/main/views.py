from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(response):
    return HttpResponse("Hello")


def v1(response):
    return HttpResponse("Hello2")