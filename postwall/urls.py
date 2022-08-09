from postwall.views import PostContentViewSet, RetrievePostWallViewSet
from django.urls import path

from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'wall', RetrievePostWallViewSet)

urlpatterns = [ 
    path('new-post/', PostContentViewSet.as_view(), name='login'),
]

urlpatterns += router.urls