from rest_framework.generics import GenericAPIView, mixins
from rest_framework import viewsets
from accounts.models import User
from rest_framework import status, response
from django.contrib.auth import authenticate

from accounts.serializers import LoginSerializer, UserSerializer

# Create your views here.

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

