from django.urls import path
from . import views 

urlpatterns = [

    path('', views.home, name='neigbor-home'),
    path('neighbor/', views.neighbor, name='neighbor-neighbor'),
    path('agency/', views.agency, name='neigbor-agency'),
    path('business/', views.business, name='neigbor-business'),

]
