from rest_framework import routers
from .views import ArtistViewSet, AlbumViewSet, RatingViewSet, SongViewSet

router = routers.DefaultRouter()
router.register(r'artists', ArtistViewSet)
router.register(r'albums', AlbumViewSet)
router.register(r'songs', SongViewSet)
router.register(r'ratings', RatingViewSet)

urlpatterns = router.urls