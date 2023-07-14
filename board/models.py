from django.db import models

# Create your models here.

class MovieList(models.Model):
    title_kor = models.CharField(max_length=100)
    title_eng = models.CharField(max_length=100)
    poster_url = models.CharField(max_length=200, blank = False)

    def __str__(self):
        return self.title_kor