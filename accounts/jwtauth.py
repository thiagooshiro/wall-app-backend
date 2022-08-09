from rest_framework.authentication import BaseAuthentication, get_authorization_header
from .models import User
from rest_framework import exceptions

import jwt
from django.conf import settings

class JWTAuthentication(BaseAuthentication):
    
    def authenticate(self, request):
        auth_header = get_authorization_header(request)
        auth_data = auth_header.decode('utf-8')

        if not auth_data:
            raise exceptions.AuthenticationFailed('Invalid Token')

        token = auth_data

        try:
            user_data = jwt.decode(token, settings.SECRET_KEY, algorithms='HS256')
            username = user_data['username']

            user = User.objects.get(username=username)

            return (user, token)
        except jwt.ExpiredSignatureError as expired:
            raise exceptions.AuthenticationFailed(
                'Token has expired, please login again')

        except jwt.DecodeError as invalid:
            raise exceptions.AuthenticationFailed(
                'Invalid Token')        

        except User.DoesNotExist as no_user:
            raise exceptions.AuthenticationFailed(
                'This user does not exists')
