from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse

from accounts.models import User


class UserModelTests(APITestCase):
    testuser = {'username': 'testuser',
                'email': 'testmail@email.com', 'password': 'password1'}

    # same as postwall test def
    def authenticate(self, user):
        self.client.post(reverse('user-list'), user)
        response = self.client.post(reverse('login'), user)
        self.client.credentials(HTTP_AUTHORIZATION=response.data['token'])

    def test_create_user(self):
        email = 'banana@email.com'

        user = User.objects.create_user('banana', email, 'password')
        self.assertIsInstance(user, User)
        self.assertFalse(user.is_staff)
        self.assertEqual(user.email, email)

    def test_create_superuser(self):
        email = 'super@email.com'

        user = User.objects.create_superuser('super', email, 'password')
        self.assertIsInstance(user, User)
        self.assertTrue(user.is_staff)
        self.assertEqual(user.email, email)

    def test_raises_error_with_no_user(self):
        email = 'erro@erro.com'
        # With no username provided
        self.assertRaises(TypeError,
                          User.objects.create_user,
                          email=email, password='password')
        # With username=NOne
        self.assertRaises(ValueError,
                          User.objects.create_user,
                          username=None, email=email, password='password')

    def test_raises_error_message_with_no_username(self):
        email = 'message@message.com'
        with self.assertRaisesMessage(
                ValueError, 'The given username must be set'):
            User.objects.create_user(
                username=None, email=email, password='password')

    def test_raises_error_with_no_email(self):
        user = 'user'
        # With no email provided
        self.assertRaises(
            TypeError, User.objects.create_user,
            username=user, password='password')
        # With email=None
        self.assertRaises(
            ValueError, User.objects.create_user,
            username=user, email=None, password='password')

    def test_raises_error_message_with_no_email(self):
        user = 'user'
        with self.assertRaisesMessage(
                ValueError, 'The given email must be set'):
            User.objects.create_user(
                username=user, email=None, password='password')

    def test_create_superuser_raises_error_if_not_is_staff(self):
        user = 'user'
        with self.assertRaisesMessage(
                ValueError, 'Superuser must have is_staff=True'):
            User.objects.create_superuser(
                username=user, email=None, password='password', is_staff=False)

    def test_create_superuser_raises_error_if_not_is_superuser(self):
        user = 'user'
        with self.assertRaisesMessage(
                ValueError, 'Superuser must have is_superuser=True.'):
            User.objects.create_superuser(
                username=user, email=None,
                password='password',
                is_superuser=False)

    def test_auth_endpoint_should_return_user_info(self):
        user = self.testuser
        self.authenticate(user)
        response = self.client.get(reverse('auth'))
        username = response.data['username']
        email = response.data['email']
        self.assertEqual(username, user['username'])
        self.assertEqual(email, user['email'])

    def test_login_with_wrong_credentials_fails(self):
        user = self.testuser
        self.client.post(reverse('user-list'), user)
        response = self.client.post(
            reverse('login'), {'username': 'anotheruser', 'password': 'anotheruserp'})
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_token_decode_should_fail_if_token_is_invalid(self):
        self.client.credentials(HTTP_AUTHORIZATION='invalid')
        response = self.client.get(reverse('auth'))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(response.data, {'detail': 'Invalid Token'})

    def test_token_expired_should_fail_to_login(self):
        token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6IkFib2JvcmEiLCJlbWFpbCI6ImFib2JvcmFAZW1haWwuY29tIiwiZXhwIjoxNjYwMjM0NjMwfQ.AjiyzIOo0rYX84uTkqYtaGG_m6vwyzXt0MOOL9JcGzA'
        self.client.credentials(HTTP_AUTHORIZATION=token)
        response = self.client.get(reverse('auth'))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(
            response.data, {'detail': 'Token has expired, please login again'})
