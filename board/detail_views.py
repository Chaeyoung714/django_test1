from .models import MovieDetail, Staff
from .serializers import MovieDetailSerializer
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, RetrieveAPIView, ListAPIView
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny
import requests

@api_view(["GET"])
def init_db(request):
    url = "https://api.hufs-likelion-movie.kro.kr/movies?format=json"
    res = requests.get(url)
    movies = res.json()['movies']
    for movie in movies:
        movie1 = MovieDetail()
        movie1.title_kor = movie['title_kor']
        movie1.title_eng = movie['title_eng']
        movie1.poster_url = movie['poster_url']
        movie1.rating_aud = movie['rating_aud']
        movie1.rating_net = movie['rating_net']
        movie1.genre = movie['genre']
        movie1.showtimes = movie['showtimes']
        movie1.release_date = movie['release_date']
        movie1.rate = movie['rate']
        movie1.summary = movie['summary']
        
        movie1.save()

        staffs = movie['staff']
        for staff in staffs:
            staff1 = Staff()
            # staff1.movie_id = movie['id']
            staff1.name = staff['name']
            staff1.role = staff['role']
            staff1.image_url = staff['image_url']
            staff1.save()

    return Response(status=status.HTTP_200_OK)

class MovieDetailView(RetrieveAPIView):
    queryset = MovieDetail.objects.all()
    serializer_class = MovieDetailSerializer
    authentication_classes = [BasicAuthentication, SessionAuthentication]
    permission_classes = [AllowAny]