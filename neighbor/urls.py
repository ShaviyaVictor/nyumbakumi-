from django.urls import path
from . import views 
from django.contrib.auth.decorators import login_required
from .views import NeighborListView, NeighborDetailView, NeighborCreateView

urlpatterns = [

    path('neighbor/', login_required(NeighborListView.as_view()), name='neighbor-neighbor'),
    path('neighbor/<int:pk>/', NeighborDetailView.as_view(), name='neighbor-detail'),
    path('neighbor/new/', NeighborCreateView.as_view(), name='neighbor-create'),

    path('', views.home, name='neighbor-home'),
    # path('neighbor/', views.neighbor, name='neighbor-neighbor'),
    path('agency/', views.agency, name='neighbor-agency'),
    path('business/', views.business, name='neighbor-business'),

]
