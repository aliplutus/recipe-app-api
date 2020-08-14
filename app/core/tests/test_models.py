from django.test import TestCase
from django.contrib.auth import get_user_model


class ModerlTests(TestCase):
    def test_create_user_with_email_secc(self):
        """" test creating email """
        email = 'weplutus@gmail.com'
        password = 'testpass123'
        user = get_user_model().objects.create_user(email=email, password=password)

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

#     def test_new_user_normolize(self):
#         """ Test if user's email not case sensetive."""
#         email = 'weplAs.1@gmail.com'
#         user = get_user_model().objects.create_user(email, 'password123')

#         self.assertEqual(user.email, email.lower())

    def test_new_user_vild_email(self):
        """ test user email with no user err"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, "password1122")

    def test_create_new_superUser(self):
        """ Test create new suerUser"""
        user = get_user_model().objects.create_superuser(
            'weplutus.1@gmail.com',
            'password'
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
