from django.urls import path
from . import views 

urlpatterns = [

    path('', views.home, name='neighbor-home'),
    path('neighbor/', views.neighbor, name='neighbor-neighbor'),
    path('agency/', views.agency, name='neighbor-agency'),
    path('business/', views.business, name='neighbor-business'),

]
