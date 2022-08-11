from rest_framework.generics import mixins
from rest_framework import viewsets
from rest_framework import permissions

from accounts.jwtauth import JWTAuthentication
from postwall.models import PostWall
from postwall.serializers import PostWallSerializer


class PostContentViewSet(
    viewsets.GenericViewSet,
    mixins.CreateModelMixin,
):
    serializer_class=PostWallSerializer
    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = (JWTAuthentication,)
    queryset=PostWall.objects.all()

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)


class RetrievePostWallViewSet(
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin):

    serializer_class=PostWallSerializer
    queryset=PostWall.objects.all()
    

class PostWallDetailsViewSet(
    viewsets.GenericViewSet,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
):
    # de onde a mensagem "not found"
    serializer_class=PostWallSerializer
    permission_classes=(permissions.IsAuthenticated,)
    authentication_classes=(JWTAuthentication,)
    queryset=PostWall.objects.all()
    
    def get_queryset(self):
        return PostWall.objects.filter(owner=self.request.user)
    