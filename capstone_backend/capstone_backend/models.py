from django.db import models

 
class Song(models.Model):
    title = models.CharField(max_length=50)
    artist = models.CharField(max_length=50)
    album = models.CharField(max_length=50)
    release_date = models.DateTimeField()
    genre = models.CharField(max_length=50)
    likes = models.IntegerField(default=0)
    reviewID=models.IntegerField(default=0)