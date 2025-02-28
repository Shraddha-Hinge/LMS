from django.test import TestCase
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient

User = get_user_model()

class UserModelTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.admin = User.objects.create_superuser(username="admin", email="admin@example.com", password="admin123", role="admin")
        self.staff = User.objects.create_user(username="staff", email="staff@example.com", password="staff123", role="staff")
        self.student = User.objects.create_user(username="student", email="student@example.com", password="student123", role="student")

    def test_create_user(self):
        user = User.objects.create_user(username="testuser", email="test@example.com", password="password123")
        self.assertEqual(user.username, "testuser")
        self.assertTrue(user.check_password("password123"))

    def test_login(self):
        response = self.client.post('/api/accounts/login/', {"email": "student@example.com", "password": "student123"})
        self.assertEqual(response.status_code, 200)

    def test_admin_can_suspend_student(self):
        self.client.force_authenticate(user=self.admin)
        response = self.client.patch(f'/api/accounts/profile/', {"is_active": False})
        self.assertEqual(response.status_code, 200)
        self.student.refresh_from_db()
        self.assertFalse(self.student.is_active)
