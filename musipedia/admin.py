from django.contrib import admin

from .models import Artist, Album, Info, Song, Rating, Image

# Register your models here.
admin.site.register(Artist)
admin.site.register(Album)
admin.site.register(Song)
admin.site.register(Rating)
admin.site.register(Info)
admin.site.register(Image)