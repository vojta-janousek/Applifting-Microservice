from django.test import TestCase
from django.contrib.auth import get_user_model


class UserModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        '''
        Test that creating a new user with an email is successful.
        '''
        email = 'test@email.com'
        password = 'testpass'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        '''
        Test that the email for a new user is normalized.
        '''
        email = 'test@EMAIL.com'
        password = 'testpass'
        user = get_user_model().objects.create_user(
            email=email,
            password=password)
        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        '''
        Test that creating user with no email raises error.
        '''
        with self.assertRaises(ValueError):
            # To pass the test, anything inside here should raise an error
            get_user_model().objects.create_user(None, 'testpass')

    def test_create_new_superuser(self):
        '''
        Test creating new superuser.
        '''
        email = 'test@email.com'
        password = 'testpass'
        user = get_user_model().objects.create_superuser(
            email=email,
            password=password
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
