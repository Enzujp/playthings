from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
#from django.views import view

# Create your views here.


def index(request):
    return HttpResponse("Hi there, and welcome to Exodus!")