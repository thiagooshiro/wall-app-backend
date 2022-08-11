from accounts.views import AuthUserViewSet, LoginViewSet, UserViewSet
from django.urls import path

from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'user', UserViewSet)

urlpatterns = [
    path('login/', LoginViewSet.as_view(), name='login'),
    path('auth/', AuthUserViewSet.as_view(), name='auth'),
]

urlpatterns += router.urls
