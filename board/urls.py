from django.urls import path
from .views import *
from .detail_views import *

app_name = 'board'

urlpatterns = [
    path('<int:pk>/', MovieDetailView.as_view()),    #pk값 아닌 movie 이름으로 변경
]