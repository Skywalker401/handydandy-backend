from pprint import pprint

import django.contrib.auth
from django.test import TestCase
from .models import User, Competencies
from django.test import Client
from django.urls import reverse
from .views import UserList, UserDetail
from . import views


class BackendTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        user = User()
        user.sid = "123"
        user.name = "Max"
        user.address = "1234 Main St."
        user.city = "Schenectady"
        user.zip = "12345"

        user.save()

        competencies = Competencies()
        competencies.owner = user
        competencies.hvac = True

        competencies.save()

    def test_get_user_address(self):
        user123 = User.objects.get(sid="123")
        assert user123.name == "Max"
        assert user123.address == "1234 Main St."
        assert user123.city == "Schenectady"
        assert user123.zip == "12345"
        assert str(user123) == "Max"

    def test_user_competencies(self):
        user123 = User.objects.get(sid="123")
        assert user123.competencies.hvac
        assert not user123.competencies.plumbing
        assert not user123.competencies.carpentry
        assert not user123.competencies.electrical

    def test_user_two_competencies(self):
        user123 = User.objects.get(sid="123")
        user123.competencies.carpentry = True
        user123.competencies.save()

        assert User.objects.get(sid="123").competencies.hvac
        assert not User.objects.get(sid="123").competencies.plumbing
        assert User.objects.get(sid="123").competencies.carpentry
        assert not User.objects.get(sid="123").competencies.electrical

    def test_user_serializer_create(self):
        pass


class URLTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        user = User()
        user.sid = "123"
        user.name = "Max"
        user.address = "1234 Main St."
        user.city = "Schenectady"
        user.zip = "12345"

        user.save()

        competencies = Competencies()
        competencies.owner = user
        competencies.hvac = True

        competencies.save()

        user_model = django.contrib.auth.get_user_model()
        auth_user = user_model.objects.create(username="testUser",
                                              is_active=True)
        auth_user.set_password('Hello')
        auth_user.save()

    def test_user_list(self):
        # Log in.
        client = Client()
        response = client.login(username='testUser', password='Hello')
        assert response

        response = client.get(reverse('user_list'))
        self.assertEqual(response.status_code, 200)
        # Used for helping create assertions to test.
        # pprint(response.json())

        assert len(response.json()) == 1

        resp_user = response.json()[0]

        assert resp_user['name'] == 'Max'
        assert resp_user['address'] == '1234 Main St.'
        assert resp_user['competencies']['hvac'] is True
        assert not resp_user['competencies']['carpentry']

    def test_user_detail(self):
        client = Client()
        response = client.login(username='testUser', password='Hello')
        assert response

        response = client.get(reverse('user_detail', args=[1]))
        self.assertEqual(response.status_code, 200)
        pprint(response.json())

