from django.db import models

class Comment(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    comment = models.TextField()

class Staff(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    image_url = models.CharField(max_length=256)

class MovieDetail(models.Model):
    # user = models.ForeignKey(CustomUser, null=True, on_delete=models.CASCADE)
    title_kor = models.CharField(max_length=100)
    title_eng = models.CharField(max_length=100)
    poster_url = models.CharField(max_length=256)
    rating_aud = models.CharField(max_length=100)
    rating_cri = models.CharField(max_length=100)
    rating_net = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    showtimes = models.CharField(max_length=100)
    release_date = models.CharField(max_length=100)
    rate = models.CharField(max_length=100)
    summary = models.TextField()

    def __str__(self):
        return self.title_kor
    
