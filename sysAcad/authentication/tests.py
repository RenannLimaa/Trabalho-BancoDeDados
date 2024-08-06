from datetime import datetime

from django.contrib.auth import get_user_model
from django.test import Client, TestCase
from django.urls import reverse
from professor.models import Professor
from student.models import Student
from users.forms import LoginForm, StudentProfessorForm


class RegisterTestCase(TestCase):

    def setUp(self):
        self.client = Client()

    def test_valid_form(self):
        data = {
            "role": "student",
            "name": "John Doe",
            "email": "john.doe@example.com",
            "cellphone": "1234567890",
            "password": "securepassword",
            "password_confirm": "securepassword",
            "birth_date": "2000-01-01",
        }
        form = StudentProfessorForm(data=data)
        self.assertTrue(form.is_valid())

    def test_invalid_password_confirmation(self):
        data = {
            "role": "student",
            "name": "John Doe",
            "email": "john.doe@example.com",
            "cellphone": "1234567890",
            "password": "securepassword",
            "password_confirm": "differentpassword",
            "birth_date": "2000-01-01",
        }
        form = StudentProfessorForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors["__all__"], ["Passwords do not match"])

    def test_missing_required_field(self):
        data = {
            # Missing email field
            "role": "student",
            "name": "John Doe",
            "cellphone": "1234567890",
            "password": "securepassword",
            "password_confirm": "securepassword",
            "birth_date": "2000-01-01",
        }
        form = StudentProfessorForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertIn("email", form.errors)

    def test_student_registration(self):
        url = reverse("register")

        data = {
            "role": "student",
            "name": "John Doe",
            "email": "john.doe@example.com",
            "cellphone": "1234567890",
            "password": "securepassword",
            "password_confirm": "securepassword",
            "birth_date": "2000-01-01",
        }

        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)

        student = Student.objects.first()
        birth_date = datetime.strptime(data["birth_date"], "%Y-%m-%d").date()

        self.assertEqual(student.email, data["email"])
        self.assertEqual(student.user.username, data["email"])
        self.assertEqual(student.cellphone, data["cellphone"])
        self.assertEqual(student.birth_date, birth_date)

    def test_professor_registration(self):
        url = reverse("register")

        data = {
            "role": "professor",
            "name": "John Doe",
            "email": "john.doe@example.com",
            "cellphone": "1234567890",
            "password": "securepassword",
            "password_confirm": "securepassword",
            "birth_date": "2000-01-01",
        }

        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)

        professor = Professor.objects.first()
        birth_date = datetime.strptime(data["birth_date"], "%Y-%m-%d").date()

        self.assertEqual(professor.email, data["email"])
        self.assertEqual(professor.user.username, data["email"])
        self.assertEqual(professor.cellphone, data["cellphone"])
        self.assertEqual(professor.birth_date, birth_date)


class LoginTestCase(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="studentuser@example.com",
            email="studentuser@example.com",
            password="securepassword",
            is_student=True,
        )

        self.student = Student.objects.create(
            user=self.user,
            email="studentuser@example.com",
            name="John Doe",
            cellphone="1234567890",
            birth_date="2000-01-01",
        )

    def test_valid_form(self):
        data = {
            "role": "student",
            "email": "testuser@example.com",
            "password": "securepassword",
        }

        form = LoginForm(data=data)
        self.assertTrue(form.is_valid())

    def test_user_login(self):
        data = {
            "role": "student",
            "email": "studentuser@example.com",
            "password": "securepassword",
        }

        response = self.client.post(reverse("login"), data)

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("student_home"))
        self.assertRedirects(response, reverse("student_home"))

        user = self.client.get(reverse("student_home"))
        self.assertEqual(user.context["user"], self.user)


class LogoutTestCase(TestCase):
    def setUp(self):
        # Create a test user
        self.username = "studentuser@example.com"
        self.password = "securepassword"
        User = get_user_model()
        self.user = User.objects.create_user(
            username=self.username, email=self.username, password=self.password
        )

        # Log in the user
        self.client.login(email=self.username, password=self.password)

    def test_user_logout(self):
        response = self.client.get(reverse("logout"))

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("login"))

        response = self.client.get(reverse("student_home"))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, f"{reverse('login')}?next={reverse('student_home')}")
