from multiprocessing import context
from turtle import title
from django.shortcuts import render
from django.http import HttpResponse
from .models import Neighbor
from django.contrib.auth.decorators import login_required




# Create your views here.
def home(request) :

  context = {
      
      'title': 'Nyumbakumi'
    }

    
  return render(request, 'neighbor/home.html', context)


@login_required
def neighbor(request) :

  context = {
      'n_posts': Neighbor.objects.all(),
      'title': 'Neighbor'
    }

  return render(request, 'neighbor/neighbor.html', context)


@login_required
def agency(request) :

  context = {
      'title': 'Agency'
    }

  return render(request, 'neighbor/agency.html', context)


@login_required
def business(request) :

  context = {
      'title': 'Business'
    }

  return render(request, 'neighbor/business.html', context)