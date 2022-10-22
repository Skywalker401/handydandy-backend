from .models import User
from django.test import SimpleTestCase


class UserTests(SimpleTestCase):

    def test_model_self_name(self):
        user = User()
        user.name = "Joey"
        user.address = "123 Main St."
        user.city = "Schenectady"
        user.zip = "12345"

        actual = str(user)
        expected = "Joey"
        assert actual == expected

        actual = str(user)
        expected = "Marni"
        assert actual != expected

