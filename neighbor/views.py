from django.shortcuts import render
from django.http import HttpResponse



# Create your views here.
def home(request) :

  return render(request, 'neighbor/home.html')



def neighbor(request) :

  return render(request, 'neighbor/neighbor.html')



def agency(request) :

  return render(request, 'neighbor/agency.html')



def business(request) :

  return render(request, 'neighbor/business.html')