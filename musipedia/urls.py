from rest_framework import routers
from django.urls import path
from .views import ArtistViewSet, AlbumViewSet, RatingViewSet, SongViewSet, ImageViewSet, InfoViewSet, HomeAPIView

router = routers.DefaultRouter()
router.register(r'artists', ArtistViewSet)
router.register(r'albums', AlbumViewSet)
router.register(r'songs', SongViewSet)
router.register(r'ratings', RatingViewSet)
router.register(r'images', ImageViewSet)
router.register(r'info', InfoViewSet)
router.register(r'home', HomeAPIView, basename='home')




urlpatterns = router.urls