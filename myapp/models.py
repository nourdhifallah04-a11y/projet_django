from django.db import models
from django.contrib.auth.models import User

class ProfilNutritionnel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.PositiveIntegerField()
    poids = models.FloatField()
    taille = models.FloatField()
    objectif = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.user.username} - Profil Nutritionnel"