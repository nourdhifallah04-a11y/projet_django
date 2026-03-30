from django.contrib.auth import get_user_model
from django.test import Client, TestCase
from django.urls import reverse

from .models import ProfilNutritionnel


class ProfilNutritionnelViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = get_user_model().objects.create_user(
            username="alice",
            password="strong-password-123",
        )

    def test_login_required_for_profile_list(self):
        response = self.client.get(reverse("profil_list"))

        self.assertEqual(response.status_code, 302)
        self.assertIn(reverse("login"), response.url)

    def test_profile_create_and_list_flow(self):
        self.client.force_login(self.user)

        response = self.client.post(
            reverse("profil_create"),
            {
                "age": 30,
                "poids": 68.5,
                "taille": 172,
                "objectif": "Maintien",
                "regime": "Equilibre",
            },
            follow=True,
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(ProfilNutritionnel.objects.count(), 1)
        self.assertContains(response, "Maintien")

    def test_user_cannot_edit_another_users_profile(self):
        other_user = get_user_model().objects.create_user(
            username="bob",
            password="strong-password-456",
        )
        profile = ProfilNutritionnel.objects.create(
            user=other_user,
            age=28,
            poids=70,
            taille=180,
            objectif="Performance",
            regime="Sportif",
        )
        self.client.force_login(self.user)

        response = self.client.get(reverse("profil_update", args=[profile.pk]))

        self.assertEqual(response.status_code, 404)
