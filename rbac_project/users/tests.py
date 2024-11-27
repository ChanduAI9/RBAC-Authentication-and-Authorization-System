from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from .models import Role, User

class UserAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.role = Role.objects.create(name="Admin", description="full_access")
        self.user = User.objects.create_user(
            username="testuser",
            email="testuser@example.com",
            password="securepassword",
            role=self.role
        )

    def test_register_user(self):
        data = {
            "username": "newuser",
            "email": "newuser@example.com",
            "password": "newpassword",
            "role": self.role.id
        }
        response = self.client.post(reverse("register"), data)
        self.assertEqual(response.status_code, 201)

    def test_protected_endpoint(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get(reverse("protected"))
        self.assertEqual(response.status_code, 200)









