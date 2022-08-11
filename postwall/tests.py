from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse


class PostWallTests(APITestCase):

    def authenticate(self):
        user = {'username': 'novato', 'password': 'novato123',
                'email': 'novo@email.com'}
        self.client.post(reverse('user-list'), user)
        response = self.client.post(reverse('login'), user)
        self.client.credentials(HTTP_AUTHORIZATION=response.data['token'])

    def test_cannot_create_post_without_auth(self):
        data = {'title': 'Today', 'content': 'Today is a fine day'}
        response = self.client.post(reverse('create-post-list'), data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_should_create_post_with_auth(self):
        self.authenticate()
        data = {'title': 'Today', 'content': 'Today is a fine day'}
        response = self.client.post(reverse('create-post-list'), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
