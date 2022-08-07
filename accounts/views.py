from rest_framework import viewsets
from accounts.models import User

from accounts.serializers import UserSerializer

# Create your views here.
class UserViewSet(
    viewsets.GenericViewSet, 
    mixins.CreateModelMixin, 
    mixins.ListModelMixin, 
    mixins.RetrieveModelMixin):
    serializer_class = UserSerializer
    queryset = User.objects.all()
