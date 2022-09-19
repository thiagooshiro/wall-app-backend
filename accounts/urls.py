from django.urls import path
from rest_framework import routers

from accounts.views import AuthUserViewSet, LoginViewSet, UserViewSet


router = routers.SimpleRouter()
router.register(r'user', UserViewSet, basename='user')

urlpatterns = [
    path('login/', LoginViewSet.as_view(), name='login'),
    path('auth/', AuthUserViewSet.as_view(), name='auth'),
]

urlpatterns += router.urls
