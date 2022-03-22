from multiprocessing import context
from turtle import title
from django.shortcuts import render
from django.http import HttpResponse
from .models import Neighbor
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView



# Create your views here.
def home(request) :

  context = {
      
      'title': 'Nyumbakumi'
    }

    
  return render(request, 'neighbor/home.html', context)


class PostListView(ListView) :
  model = Neighbor

  # <app>/<model>_<viewtype>.html
  template_name = 'neighbor/neighbor.html'

  context_object_name = 'n_posts'

  title = 'Neighbor'

  ordering = ['-n_date_posted']


# @login_required
# def neighbor(request) :

#   context = {
#       'n_posts': Neighbor.objects.all(),
#       'title': 'Neighbor'
#     }

#   return render(request, 'neighbor/neighbor.html', context)


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