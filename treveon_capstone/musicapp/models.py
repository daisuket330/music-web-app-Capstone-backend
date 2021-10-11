from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Song(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    artist = models.CharField(max_length=50)
    album = models.CharField(max_length=50)
    release_date = models.DateTimeField()
    genre = models.CharField(max_length=50)
    likes = models.IntegerField(default=0)
    song_id= models.TextField(blank=True, null=True, max_length=500)
    
    def __str__(self):
        return self.Song