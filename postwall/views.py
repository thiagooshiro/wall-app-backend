from rest_framework.generics import CreateAPIView, mixins
from rest_framework import viewsets
from rest_framework import permissions

from accounts.jwtauth import JWTAuthentication
from postwall.models import PostWall
from postwall.serializers import PostWallSerializer


class PostContentViewSet(CreateAPIView):
    serializer_class=PostWallSerializer
    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = (JWTAuthentication,)

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)


class RetrievePostWallViewSet(
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin):

    serializer_class=PostWallSerializer
    queryset=PostWall.objects.all()
    