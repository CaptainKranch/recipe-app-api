from django.test import TestCase
from django.contrib.auth import get_user_model
from core import models

def sample_user(email = 'idk@test.com', password = 'testpass'):
    #Creates a sample user
    return get_user_model().objects.create_user(email, password)

class ModelTest(TestCase):
    def test_create_user_with_eamil_successfful(self):
        email = "testing@email.com"
        password = "Testpass1234#"

        user = get_user_model().objects.create_user(
            email = email,
            password = password,
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))
    
    def test_new_user_email_normalized(self):
        #Test the email for a new user is normalized
        email = 'idk@GMAIL.com'
        user = get_user_model().objects.create_user(email, 'test123')

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        #No email = error
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'Test123')
    
    def test_create_new_superuser(self):
        user = get_user_model().objects.create_superuser(
            'test@ggggg.com',
            'test123'
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    def test_tat_str(self):
        #Test the tag str representation
        tag = models.Tag.objects.create(
            user = sample_user(),
            name = 'vegan'
        )

        self.assertEqual(str(tag), tag.name)
    