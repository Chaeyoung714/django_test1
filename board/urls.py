from django.urls import path
from . import views
from .movielist_views import *

app_name = 'board'

urlpatterns = [
    path('', MovieListGet.as_view())
]