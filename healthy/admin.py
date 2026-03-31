from django.contrib import admin
from .models import ProfilNutritionnel


@admin.register(ProfilNutritionnel)
class ProfilNutritionnelAdmin(admin.ModelAdmin):
    list_display = ("user", "age", "poids", "taille", "objectif", "regime")
    search_fields = ("user__username", "objectif", "regime")
    list_filter = ("objectif", "regime")
