from django.shortcuts import render
from rest_framework import viewsets

from .models import Artist, Album, Rating, Song
from .serializers import ArtistSerializer, AlbumSerializer, SongSerializer, ArtistDetailSerializer, RatingSerializer, AlbumDetailSerializer, SongDetailSerializer

# Create your views here.

class ArtistViewSet(viewsets.ModelViewSet):

    serializer_class = ArtistSerializer
    queryset = Artist.objects.all()

    def get_serializer_class(self):

        if self.action == 'retrieve':
            return ArtistDetailSerializer
        else:
            return ArtistSerializer
        




class AlbumViewSet(viewsets.ModelViewSet):

    serializer_class = AlbumSerializer
    queryset = Album.objects.all()

    def get_serializer_class(self):

        if self.action == 'retrieve':
            return AlbumDetailSerializer
        else:
            return AlbumSerializer




class SongViewSet(viewsets.ModelViewSet):

    serializer_class = SongSerializer
    queryset = Song.objects.all()

    def get_serializer_class(self):

        if self.action == 'retrieve':
            return SongDetailSerializer
        else:
            return SongSerializer




class RatingViewSet(viewsets.ModelViewSet):

    serializer_class = RatingSerializer
    queryset = Rating.objects.all()
