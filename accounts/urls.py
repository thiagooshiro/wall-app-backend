from accounts.views import LoginViewSet, UserViewSet
from django.urls import path

from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'account', UserViewSet)


urlpatterns = [ 
  path('login', LoginViewSet.as_view(), name='login')
]

urlpatterns += router.urls