from django.db import models

from users.models import MyUser

class Artist(models.Model):

    first_name = models.CharField(max_length=50, null=False, blank=False)
    last_name = models.CharField(max_length=50, null=False, blank=False)
    stage_name = models.CharField(max_length=50, null=False, blank=False)
    record_label = models.CharField(max_length=50, null=False, blank=False)
    DOB = models.DateField()
    DOD = models.DateField(blank=True, null=True)
    # picture = models.ImageField()

    def __str__(self):
        return self.stage_name


class Album(models.Model):

    title = models.CharField(max_length=50, blank=False, null=False)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, blank=False, related_name='albums')
    # cover_image = models.ImageField()
    year_released = models.CharField(max_length=4)
    featured_artists = models.CharField(max_length=50, blank=True)
    producers = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.title


class Song(models.Model):

    title = models.CharField(max_length=50, blank=False, null=False)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, blank=False, related_name='songs')
    album = models.ForeignKey(Album, on_delete=models.CASCADE, blank=True, null=True, related_name='songs')
    featured_artists = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.title
'''
class Image(models.Model):

    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, blank=True, related_name='picture')
    album = models.ForeignKey(Album, on_delete=models.CASCADE, blank=True, related_name='cover_image')
    song = models.ForeignKey(Song, on_delete=models.CASCADE, blank=True, related_name='cover_art')
    image = models.ImageField()
'''
class Rating(models.Model):

    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, blank=True, null=True, related_name='ratings')
    album = models.ForeignKey(Album, on_delete=models.CASCADE, blank=True, null=True, related_name='ratings')
    song = models.ForeignKey(Song, on_delete=models.CASCADE, blank=True, null=True, related_name='ratings')
    rating = models.SmallIntegerField()
'''
class Info(models.Model):

    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, blank=True, null=True, related_name='info')
    album = models.ForeignKey(Album, on_delete=models.CASCADE, blank=True, null=True, related_name='info')
    song = models.ForeignKey(Song, on_delete=models.CASCADE, blank=True, null=True, related_name='info')
    info = models.TextField()

'''




'''

Song 
    - title
    - artist
    - featured artist(s)
    - ratings

    - producer(s)
    - info 

Album
    - title
    - artist 
    - year released
    - cover image
    - ratings

    - featured artist (s)
    - producer(s)
    - info 

Rating
    - rating(max=10(float))

Picture
    - type 
    - image 

Artist
    - real name
    - stage name 
    - record label 
    - DOB 
    - DOD 
    - picture
    - ratings 

    - info 



Song 
    - title
    - artist
    - featured artist(s)
    - ratings

    - producer(s)
    - info 
'''