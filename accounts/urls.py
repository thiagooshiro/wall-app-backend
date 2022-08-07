from accounts.views import UserViewSet
from django.urls import path

from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'account', UserViewSet)

urlpatterns = router.urls