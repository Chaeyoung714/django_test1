from rest_framework import serializers
from .models import MovieList

class MovieListSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieList
        fields = ['title_kor', 'poster_url']