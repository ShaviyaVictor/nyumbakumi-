from django.urls import path
from . import views 
from django.contrib.auth.decorators import login_required
from .views import PostListView

urlpatterns = [

    path('neighbor/', login_required(PostListView.as_view()), name='neighbor-neighbor'),

    path('', views.home, name='neighbor-home'),
    # path('neighbor/', views.neighbor, name='neighbor-neighbor'),
    path('agency/', views.agency, name='neighbor-agency'),
    path('business/', views.business, name='neighbor-business'),

]
