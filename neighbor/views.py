from multiprocessing import context
from turtle import title
from django.shortcuts import render
from django.http import HttpResponse
from .models import Neighbor



# Creating dummy data for context calling
n_posts = [

  {
    'n_author': 'Victor Shaviya',
    'n_name': 'Danstone',
    'n_location': 'Imara daima',
    # 'n_image': '',
    'n_title': 'Internet upgrade',
    'n_update': 'We are upgrading the internet.',
    'n_date_posted': '19 March, 2022',
  },
  {
    'n_author': 'Josphine Mbaisi',
    'n_name': 'Boulevard',
    'n_location': '14 Street',
    # 'n_image': '',
    'n_title': 'Utilities condition',
    'n_update': 'Utility checks will be done today.',
    'n_date_posted': '28 March, 2022',
  },
  {
    'n_author': 'Norris Ambune',
    'n_name': 'Tel Aviv',
    'n_location': 'Taj Mall',
    # 'n_image': '',
    'n_title': 'Relocation',
    'n_update': 'I am to relocate in a few days.',
    'n_date_posted': '01 April, 2022',
  },

]



# Create your views here.
def home(request) :

  context = {
      
      'title': 'Nyumbakumi'
    }

    
  return render(request, 'neighbor/home.html', context)



def neighbor(request) :

  context = {
      'n_posts': Neighbor.objects.all(),
      'n_posts' : n_posts,
      'title': 'Neighbor'
    }

  return render(request, 'neighbor/neighbor.html', context)



def agency(request) :

  context = {
      'title': 'Agency'
    }

  return render(request, 'neighbor/agency.html', context)



def business(request) :

  context = {
      'title': 'Business'
    }

  return render(request, 'neighbor/business.html', context)