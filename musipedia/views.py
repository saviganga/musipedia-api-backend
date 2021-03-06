from django.shortcuts import render
from rest_framework import generics, viewsets, status, filters
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Artist, Album, Rating, Song, Image, Info
from .serializers import ArtistSerializer, AlbumSerializer, SongSerializer, ArtistDetailSerializer, RatingSerializer, AlbumDetailSerializer, SongDetailSerializer,ImageSerializer, InfoSerializer

from drf_multiple_model.viewsets import ObjectMultipleModelAPIViewSet

# Create your views here.

class ArtistViewSet(viewsets.ModelViewSet):

    ''' view and edit artist instances '''

    serializer_class = ArtistSerializer
    queryset = Artist.objects.all()

    def get_serializer_class(self):

        if self.action == 'retrieve':
            return ArtistDetailSerializer
        else:
            return ArtistSerializer




class AlbumViewSet(viewsets.ModelViewSet):

    ''' view and edit album instances '''

    serializer_class = AlbumSerializer
    queryset = Album.objects.all()

    def get_serializer_class(self):

        if self.action == 'retrieve':
            return AlbumDetailSerializer
        else:
            return AlbumSerializer




class SongViewSet(viewsets.ModelViewSet):

    ''' view and edit song instances '''

    serializer_class = SongSerializer
    queryset = Song.objects.all()

    def get_serializer_class(self):

        if self.action == 'retrieve':
            return SongDetailSerializer
        else:
            return SongSerializer




class RatingViewSet(viewsets.ModelViewSet):

    ''' view and edit ratings '''

    serializer_class = RatingSerializer
    queryset = Rating.objects.all()




class ImageViewSet(viewsets.ModelViewSet):

    ''' view and edit images '''

    serializer_class = ImageSerializer
    queryset = Image.objects.all()


 

class InfoViewSet(viewsets.ModelViewSet):

    ''' view and edit album info descriptions '''

    serializer_class = InfoSerializer
    queryset = Info.objects.all()




class HomeAPIView(ObjectMultipleModelAPIViewSet):

    ''' homepage '''

    pagination_class = None
    querylist = [
        {'queryset': Artist.objects.order_by('id')[:5], 'serializer_class': ArtistSerializer},
        {'queryset': Album.objects.order_by('id')[:5], 'serializer_class': AlbumSerializer},
        {'queryset': Song.objects.order_by('id')[:5], 'serializer_class': SongSerializer},
    ]

