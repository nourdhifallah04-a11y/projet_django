from django import forms

from .models import ProfilNutritionnel


class ProfilNutritionnelForm(forms.ModelForm):
    class Meta:
        model = ProfilNutritionnel
        fields = ["age", "poids", "taille", "objectif", "regime"]
        widgets = {
            "objectif": forms.TextInput(attrs={"placeholder": "Perte de poids, maintien, prise de masse"}),
            "regime": forms.TextInput(attrs={"placeholder": "Vegetarien, sportif, equilibre"}),
        }

    def clean_age(self):
        age = self.cleaned_data["age"]
        if age < 10 or age > 120:
            raise forms.ValidationError("L'age doit etre compris entre 10 et 120 ans.")
        return age
