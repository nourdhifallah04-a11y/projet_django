from django.conf import settings
from django.core.validators import MinValueValidator
from django.db import models


class ProfilNutritionnel(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="profil_nutritionnel",
    )
    age = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    poids = models.DecimalField(max_digits=5, decimal_places=2, validators=[MinValueValidator(1)])
    taille = models.DecimalField(max_digits=5, decimal_places=2, validators=[MinValueValidator(1)])
    objectif = models.CharField(max_length=100)
    regime = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["user__username"]
        verbose_name = "profil nutritionnel"
        verbose_name_plural = "profils nutritionnels"

    def __str__(self):
        return f"{self.user.username} - Profil nutritionnel"
