from django.shortcuts import render
from django.http import HttpResponse



# Create your views here.
def home(request) :

  return HttpResponse('<h1>Home Page</h1>')



def neighbor(request) :

  return HttpResponse('<h1>Neighbors Page</h1>')



def agency(request) :

  return HttpResponse('<h1>Agency Page</h1>')



def business(request) :

  return HttpResponse('<h1>Business Page</h1>')