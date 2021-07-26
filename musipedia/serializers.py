from django.db.models import fields
from rest_framework import serializers
from .models import Artist, Album, Rating, Song

class ArtistSerializer(serializers.ModelSerializer):

    class Meta:
        model = Artist
        fields = ('__all__')




class AlbumSerializer(serializers.ModelSerializer):

    class Meta:
        model = Album 
        fields = ('__all__')




class SongSerializer(serializers.ModelSerializer):

    class Meta:
        model = Song
        fields = ('artist', 'title', 'featured_artists', 'album')




class RatingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Rating
        fields = ('__all__')



class SongDetailSerializer(serializers.ModelSerializer):

    ratings = serializers.SerializerMethodField()

    class Meta:
        model = Song
        fields = ('__all__')
        
    def get_ratings(self, obj):
        rate = []
        ratings = RatingSerializer(obj.ratings.all(), many=True).data
        for rating in ratings:
            rate.append(rating['rating'])
        try:
            average_rating = sum(rate) / len(rate)
        except ZeroDivisionError:
            average_rating = 0.0
        rratings = [{'average_rating': average_rating}, {'ratings': ratings}]
        return rratings




class AlbumDetailSerializer(serializers.ModelSerializer):

    artist = serializers.SerializerMethodField()
    songs = serializers.SerializerMethodField()
    ratings = serializers.SerializerMethodField()

    class Meta:
        model = Album
        fields = ('__all__')

    def get_artist(self, obj):
        artist = ArtistSerializer(obj.artist).data
        return artist

    def get_songs(self, obj):
        songs = SongSerializer(obj.songs.all(), many=True).data
        num_songs = len(songs)
        ssongs = [{'num_songs': num_songs}, {'songs': songs}]
        return ssongs

    def get_ratings(self, obj):
        rate = []
        ratings = RatingSerializer(obj.ratings.all(), many=True).data
        for rating in ratings:
            rate.append(rating['rating'])
        try:
            average_rating = sum(rate) / len(rate)
        except ZeroDivisionError:
            average_rating = 0.0
        rratings = [{'average_rating': average_rating}, {'ratings': ratings}]
        return rratings




class ArtistDetailSerializer(serializers.ModelSerializer):

    songs = serializers.SerializerMethodField()
    albums = serializers.SerializerMethodField()
    ratings = serializers.SerializerMethodField()

    class Meta:
        model = Artist
        fields = ('__all__')

    def get_albums(self, obj):
        albums = AlbumSerializer(obj.albums.all(), many=True).data
        num_albums = len(albums)
        aalbums = [{'num_albums': num_albums}, {'albums': albums}]
        return aalbums

    def get_songs(self, obj):
        songs = SongSerializer(obj.songs.all(), many=True).data
        num_songs = len(songs)
        ssongs = [{'num_songs': num_songs}, {'songs': songs}]
        return ssongs

    def get_ratings(self, obj):
        rate = []
        ratings = RatingSerializer(obj.ratings.all(), many=True).data
        for rating in ratings:
            rate.append(rating['rating'])
        try:
            average_rating = sum(rate) / len(rate)
        except ZeroDivisionError:
            average_rating = 0.0
        rratings = [{'average_rating': average_rating}, {'ratings': ratings}]
        return rratings

    
           