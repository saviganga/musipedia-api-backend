from rest_framework import routers, urlpatterns
from .views import UserViewSet

router = routers.DefaultRouter()
router.register(r'', UserViewSet)

urlpatterns = router.urls