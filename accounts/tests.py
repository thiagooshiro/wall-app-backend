from rest_framework.test import APITestCase
from accounts.models import User

# Create your tests here.

class UserTests(APITestCase):

    def test_create_user(self):
        email = 'banana@email.com'

        user = User.objects.create_user('banana', email, 'password')
        self.assertIsInstance(user, User)
        self.assertFalse(user.is_staff)
        self.assertEqual(user.email, email)
