from django.db.models import fields
from rest_framework import serializers
from .models import Artist, Album, Rating, Song, Image, Info



class RatingSerializer(serializers.ModelSerializer):

    rating = serializers.IntegerField(min_value=1, max_value=10)
    class Meta:
        model = Rating
        fields = ('artist', 'album', 'song', 'rating',)


class ImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Image
        fields = ('name', 'image',)




class InfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Info
        fields = ('info',)




class StringSerializer(serializers.StringRelatedField):

    def to_internal_value(self, data):
        return super().to_internal_value(data)




class ArtistSerializer(serializers.ModelSerializer):

    image = ImageSerializer(read_only=True)
    info = InfoSerializer(read_only=True)

    class Meta:
        model = Artist
        fields = ('first_name', 'last_name', 'stage_name', 'image', 'DOB', 'DOD', 'info')




class AlbumSerializer(serializers.ModelSerializer):
    
    image = ImageSerializer(read_only=True)
    info = InfoSerializer(read_only=True)

    class Meta:
        model = Album 
        fields = ('title', 'image', 'artist', 'featured_artists', 'producers', 'year_released', 'info',)



class SongSerializer(serializers.ModelSerializer):

    
    class Meta:
        model = Song
        fields = ('artist', 'title', 'featured_artists', 'album', 'image', 'info')





class SongDetailSerializer(serializers.ModelSerializer):

    artist = StringSerializer()
    ratings = serializers.SerializerMethodField()
    image = StringSerializer()
    info = StringSerializer()

    class Meta:
        model = Song
        fields = ('artist', 'title', 'featured_artists', 'album', 'image', 'info', 'ratings')

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

    artist = StringSerializer() #serializers.SerializerMethodField()
    songs = serializers.SerializerMethodField()
    ratings = serializers.SerializerMethodField()
    image = StringSerializer()
    info = StringSerializer()
    

    class Meta:
        model = Album
        fields = ('title', 'image', 'artist', 'featured_artists', 'producers', 'year_released', 'info', 'songs', 'ratings',)

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
    image = StringSerializer()
    info = StringSerializer()

    class Meta:
        model = Artist
        fields = ('first_name', 'last_name', 'stage_name', 'image', 'DOB', 'DOD', 'info', 'songs', 'albums', 'ratings')

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

 