from postwall.views import (
    PostContentViewSet, RetrievePostWallViewSet, PostWallDetailsViewSet)

from django.urls import path
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'feed', RetrievePostWallViewSet, basename="feed")
router.register(r'', PostContentViewSet, basename="create-post")




urlpatterns = [
    path('details/<int:id>', PostWallDetailsViewSet.as_view(), name="details"),
]

urlpatterns += router.urls