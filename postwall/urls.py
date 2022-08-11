from postwall.views import PostContentViewSet, RetrievePostWallViewSet, PostWallDetailsViewSet
from django.urls import path

from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'view', RetrievePostWallViewSet)
router.register(r'', PostContentViewSet)
router.register(r'details', PostWallDetailsViewSet)
urlpatterns = router.urls