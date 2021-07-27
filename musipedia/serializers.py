from django.db.models import fields
from rest_framework import serializers
from .models import Artist, Album, Rating, Song, Image, Info




class RatingSerializer(serializers.ModelSerializer):

    ''' serializer for Rating model '''

    rating = serializers.IntegerField(min_value=1, max_value=10)
    class Meta:
        model = Rating
        fields = ('artist', 'album', 'song', 'rating',)




class ImageSerializer(serializers.ModelSerializer):

    ''' serializer for Image model '''

    class Meta:
        model = Image
        fields = ('name', 'image',)




class InfoSerializer(serializers.ModelSerializer):

    ''' serializer for Info model '''

    class Meta:
        model = Info
        fields = ('info',)




class StringSerializer(serializers.StringRelatedField):

    ''' returns the string representation of models '''

    def to_internal_value(self, data):
        return super().to_internal_value(data)




class ArtistSerializer(serializers.ModelSerializer):

    ''' serializer for Artist model '''

    image = ImageSerializer(read_only=True)
    info = InfoSerializer(read_only=True)

    class Meta:
        model = Artist
        fields = ('first_name', 'last_name', 'stage_name', 'image', 'DOB', 'DOD', 'info')




class AlbumSerializer(serializers.ModelSerializer):

    ''' serializer for Album model '''
    
    image = ImageSerializer(read_only=True)
    info = InfoSerializer(read_only=True)

    class Meta:
        model = Album 
        fields = ('title', 'image', 'artist', 'featured_artists', 'producers', 'year_released', 'info',)




class SongSerializer(serializers.ModelSerializer):

    ''' serializer for Song model '''
    
    class Meta:
        model = Song
        fields = ('artist', 'title', 'featured_artists', 'album', 'image', 'info')




class SongDetailSerializer(serializers.ModelSerializer):

    ''' returns view with song details '''

    artist = StringSerializer()
    ratings = serializers.SerializerMethodField()
    image = StringSerializer()
    info = StringSerializer()

    class Meta:
        model = Song
        fields = ('artist', 'title', 'featured_artists', 'album', 'image', 'info', 'ratings')

    def get_ratings(self, obj):

        ''' returns a list of all song ratings and average song rating '''

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

    ''' returns view with album details '''

    artist = StringSerializer()
    songs = serializers.SerializerMethodField()
    ratings = serializers.SerializerMethodField()
    image = StringSerializer()
    info = StringSerializer()

    class Meta:
        model = Album
        fields = ('title', 'image', 'artist', 'featured_artists', 'producers', 'year_released', 'info', 'songs', 'ratings',)

    def get_artist(self, obj):

        ''' returns string component of artist '''

        artist = ArtistSerializer(obj.artist).data
        return artist

    def get_songs(self, obj):

        ''' returns a list of songs and number of songs in an album '''

        songs = SongSerializer(obj.songs.all(), many=True).data
        num_songs = len(songs)
        ssongs = [{'num_songs': num_songs}, {'songs': songs}]
        return ssongs

    def get_ratings(self, obj):

        ''' returns a list of all album ratings and average album rating '''

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

    ''' returns view with artist detail '''

    albums = serializers.SerializerMethodField()
    songs = serializers.SerializerMethodField()
    ratings = serializers.SerializerMethodField()
    image = StringSerializer()
    info = StringSerializer()

    class Meta:
        model = Artist
        fields = ('first_name', 'last_name', 'stage_name', 'image', 'DOB', 'DOD', 'info', 'songs', 'albums', 'ratings')

    def get_albums(self, obj):

        ''' returns a list of albums and number of albums for an artist '''

        albums = AlbumSerializer(obj.albums.all(), many=True).data
        num_albums = len(albums)
        aalbums = [{'num_albums': num_albums}, {'albums': albums}]
        return aalbums

    def get_songs(self, obj):

        ''' returns a list of songs and number of songs for an artist '''

        songs = SongSerializer(obj.songs.all(), many=True).data
        num_songs = len(songs)
        ssongs = [{'num_songs': num_songs}, {'songs': songs}]
        return ssongs

    def get_ratings(self, obj):

        ''' returns a list of all artist ratings and average artist rating '''

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

 