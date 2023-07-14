from django.urls import path
from . import views
from .movielist_views import *
# from .moviesearch_views import * 

app_name = 'board'

urlpatterns = [
    path('', MovieListGet.as_view()),
    # path('search/', movie_search, name='search'),
]