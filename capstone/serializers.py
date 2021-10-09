from rest_framework import serializers

from .models import CommentSection, Song

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ['id','comment','song_id', 'like', 'dislike']

       
class CommentSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentSection
        fields = ['songcomment']