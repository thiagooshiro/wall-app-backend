from rest_framework.test import APITestCase
from accounts.models import User

# Create your tests here.

class UserModelTests(APITestCase):

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
        self.assertRaises(TypeError, User.objects.create_user, email=email, password='password')
        # With username=NOne
        self.assertRaises(ValueError, User.objects.create_user, username=None, email=email, password='password')

    def test_raises_error_message_with_no_username(self):
        email = 'message@message.com'
        with self.assertRaisesMessage(ValueError, 'The given username must be set'):
            User.objects.create_user(username=None, email=email, password='password')
        
    def test_raises_error_with_no_email(self):
        user='user'
        # With no email provided
        self.assertRaises(TypeError, User.objects.create_user, username=user, password='password')
        # With email=None
        self.assertRaises(ValueError, User.objects.create_user, username=user, email=None, password='password')
    
    def test_raises_error_message_with_no_email(self):
        user = 'user'
        with self.assertRaisesMessage(ValueError, 'The given email must be set'):
            User.objects.create_user(username=user, email=None, password='password')
    
    def test_create_superuser_raises_error_if_not_is_staff(self):
        user = 'user'
        with self.assertRaisesMessage(ValueError, 'Superuser must have is_staff=True'):
            User.objects.create_superuser(
                username=user, email=None, password='password', is_staff=False)
 
 
    def test_create_superuser_raises_error_if_not_is_superuser(self):
        user = 'user'
        with self.assertRaisesMessage(ValueError, 'Superuser must have is_superuser=True.'):
            User.objects.create_superuser(
                username=user, email=None, password='password', is_superuser=False)
