from rest_framework import routers
from .viewsets import reportViewSet



router = routers.SimpleRouter()
router.register('report',reportViewSet)
urlpatterns = router.urls
