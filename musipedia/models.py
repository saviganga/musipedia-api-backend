from django.db import models
from django.db.models.lookups import In

from users.models import MyUser


class Info(models.Model):

    ''' Descritions for Artists, Albums and Songs '''

    info = models.TextField()

    def __str__(self):
        return self.info




class Image(models.Model):

    '''Images for Artists, Albums and Songs'''

    name = models.CharField(max_length=100, blank=False)
    image = models.ImageField(upload_to='image/')

    def __str__(self):
        return self.name




class Artist(models.Model):

    ''' model for Artists'''

    first_name = models.CharField(max_length=50, null=False, blank=False)
    last_name = models.CharField(max_length=50, null=False, blank=False)
    stage_name = models.CharField(max_length=50, null=False, blank=False)
    record_label = models.CharField(max_length=50, null=False, blank=False)
    DOB = models.DateField()
    DOD = models.DateField(blank=True, null=True)
    info = models.ForeignKey(Info, blank=True, null=True, on_delete=models.SET_NULL, related_name='artist')
    image = models.ForeignKey(Image, blank=True, null=True, on_delete=models.SET_NULL, related_name='artist')

    def __str__(self):
        return self.stage_name


class Album(models.Model):

    '''model for albums'''

    title = models.CharField(max_length=50, blank=False, null=False)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, blank=False, related_name='albums')
    year_released = models.CharField(max_length=4)
    featured_artists = models.CharField(max_length=50, blank=True)
    producers = models.CharField(max_length=50, blank=True)
    info = models.ForeignKey(Info, null=True, blank=True, on_delete=models.SET_NULL, related_name='album')
    image = models.ForeignKey(Image, blank=True, null=True, on_delete=models.SET_NULL, related_name='album')

    def __str__(self):
        return self.title


class Song(models.Model):

    ''' model for Songs '''

    title = models.CharField(max_length=50, blank=False, null=False)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, blank=False, related_name='songs')
    album = models.ForeignKey(Album, on_delete=models.CASCADE, blank=True, null=True, related_name='songs')
    featured_artists = models.CharField(max_length=50, blank=True)
    info = models.ForeignKey(Info, blank=True, null=True, on_delete=models.SET_NULL, related_name='song')
    image = models.ForeignKey(Image, blank=True, null=True, on_delete=models.SET_NULL, related_name='song')

    def __str__(self):
        return self.title



class Rating(models.Model):

    ''' ratings for Artists, Albums, Songs '''

    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, blank=True, null=True, related_name='ratings')
    album = models.ForeignKey(Album, on_delete=models.CASCADE, blank=True, null=True, related_name='ratings')
    song = models.ForeignKey(Song, on_delete=models.CASCADE, blank=True, null=True, related_name='ratings')
    rating = models.SmallIntegerField()
    