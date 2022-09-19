from rest_framework.generics import GenericAPIView, mixins
from rest_framework import viewsets
from rest_framework import status, response, permissions
from django.contrib.auth import authenticate

import os

from sendgrid.helpers.mail import Mail, Email, To, Content
from sendgrid import SendGridAPIClient

from accounts.jwtauth import JWTAuthentication
from accounts.models import User
from accounts.serializers import LoginSerializer, UserSerializer


class UserViewSet(
        viewsets.GenericViewSet,
        mixins.CreateModelMixin,
        mixins.ListModelMixin,
        mixins.RetrieveModelMixin):

    def register_send_email(self, username, email):
        try:
            sg = SendGridAPIClient(api_key=os.environ.get('SENDGRID_API_KEY'))
            from_email = Email(os.getenv('DEFAULT_FROM_EMAIL'))
            to_email = To(email)
            subject = "Account Sucessfuly Created!"
            content = Content("text/plain", f'Wecome to WallApp, {username}')
            mail = Mail(from_email, to_email, subject, content)
            response = sg.client.mail.send.post(request_body=mail.get())
            print(response.status_code)
            print(response.body)
            print(response.headers)
        except Exception as e:
            print(e.to_dict)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        username = serializer.validated_data['username']
        email = serializer.validated_data['email']
        # self.register_send_email(username, email)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return response.Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers)

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
        return response.Response(serializer.data)
