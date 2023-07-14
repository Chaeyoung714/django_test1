from rest_framework import serializers
from .models import *

class MovieListSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieDetail
        fields = ['title_kor', 'poster_url']


class CommentSerializer(serializers.ModelSerializer):
    # user = serializers.CharField(source='user.nickname', read_only=True)
    
    class Meta:
        model = Comment
        fields = ['id', 'user', 'created_at', 'comment']

class StaffSerializer(serializers.ModelSerializer):
    movie_id = serializers.ReadOnlyField(source="movie_id.title_kor")

    class Meta:
        model = Staff
        fields = ['id', 'movie_id', 'name', 'role', 'image_url']

class MovieDetailSerializer(serializers.ModelSerializer):
    staffs = StaffSerializer(many=True)
    # comments = CommentSerializer(many=True)

    class Meta:
        model = MovieDetail
        fields = ['id', 'title_kor', 'title_eng', 'poster_url', 'rating_aud', 'rating_cri', 'rating_net', 'genre', 'showtimes', 'release_date', 'rate', 'summary', 'staffs']    #'staffs', 'comments' 안넣음
        # read_only_fields = ['user']   #읽는 것만 가능





