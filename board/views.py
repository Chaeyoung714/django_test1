from rest_framework.response import Response
from rest_framework import status
import requests

def init_db(request):
    url = "https://api.hufs-likelion-movie.kro.kr/movies?format=json"
    res = requests.get(url)
    movies = res.json()['movies']
    for movie in movies:
        title_kor = movie['title_kor']
        title_eng = movie['title_eng']
        poster_url = movie['poster_url']
        rating_aud = movie['rating_aud']
        rating_net = movie['rating_net']
        genre = movie['genre']
        showtimes = movie['showtimes']
        release_date = movie['release_date']
        rate = movie['rate']
        summary = movie['summary']
        staffs = movie.json()['staff']
        for staff in staffs:
            name = staff['name']
            role = staff['role']
            image_url = staff['image_url']

    return Response(status=status.HTTP_200_OK)
