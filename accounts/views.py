from rest_framework.generics import GenericAPIView, mixins
from rest_framework import viewsets
from accounts.jwtauth import JWTAuthentication
from accounts.models import User
from rest_framework import status, response, permissions
from django.contrib.auth import authenticate

from accounts.serializers import LoginSerializer, UserSerializer


class UserViewSet(
    viewsets.GenericViewSet, 
    mixins.CreateModelMixin, 
    mixins.ListModelMixin, 
    mixins.RetrieveModelMixin):
    serializer_class = UserSerializer
    queryset = User.objects.all()

class LoginViewSet(GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        email = request.data.get('email', None)
        password = request.data.get('password', None)
        
        user = authenticate(username=email, password=password)

        if user:
            serializer = self.serializer_class(user)

            return response.Response(serializer.data, status=status.HTTP_200_OK)
        return response.Response(
            {'message': 'Invalid credentials, please try again'},
            status=status.HTTP_401_UNAUTHORIZED)


class AuthUserViewSet(GenericAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = (JWTAuthentication,)

    def get(self, request):
        user = request.user
        serializer = UserSerializer(user)
        return response.Response({'user': serializer.data})
