from django.http.response import Http404
from django.shortcuts import render
from .models import Comment
from .serializers import CommentSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import Http404



# Create your views here.
class CommentList(APIView):
    def get(self, request):
        comment = Comment.objects.all()
        serializer = CommentSerializer(comment, many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer = CommentSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class CommentDetail(APIView):
    def get_object(self, song_id):
        try:
            return Comment.objects.filter(song_id = song_id)
        except Comment.DoesNotExist:
            raise Http404

    def get(self, request, song_id):
        print(song_id)
        comment = Comment.objects.filter(song_id = song_id)
        serializer = CommentSerializer(comment, many=True)
        return Response(serializer.data)

    def delete(self, request, pk):
        comment = Comment.objects.filter(pk = pk)
        comment.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)

class CommentLike(APIView):
        def get_object(self, pk):
            try:
                return Comment.objects.get(pk = pk)
            except Comment.DoesNotExist:
                raise Http404

        def get(self, request, pk):
            comment = self.get_object(pk)
            serializer = CommentSerializer(comment, data=request.data)
            return Response(serializer.data)

        def patch(self, request, pk):
            comment = self.get_object(pk)
            data = {"likes": comment.likes + int(1)}
            serializer = CommentSerializer(comment, data=data, partial = True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CommentDislike(APIView):
        def get_object(self, pk):
            try:
                return Comment.objects.get(pk = pk)
            except Comment.DoesNotExist:
                raise Http404

        def get(self, request, pk):
            comment = self.get_object(pk)
            serializer = CommentSerializer(comment, data=request.data)
            return Response(serializer.data)

        def patch(self, request, pk):
            comment = self.get_object(pk)
            data = {"dislikes": comment.dislikes + int(1)}
            serializer = CommentSerializer(comment, data=data, partial = True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)