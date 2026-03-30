from django.conf import settings
from django.db import migrations, models
import django.core.validators
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="ProfilNutritionnel",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("age", models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1)])),
                ("poids", models.DecimalField(decimal_places=2, max_digits=5, validators=[django.core.validators.MinValueValidator(1)])),
                ("taille", models.DecimalField(decimal_places=2, max_digits=5, validators=[django.core.validators.MinValueValidator(1)])),
                ("objectif", models.CharField(max_length=100)),
                ("regime", models.CharField(blank=True, max_length=100)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="profil_nutritionnel",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "profil nutritionnel",
                "verbose_name_plural": "profils nutritionnels",
                "ordering": ["user__username"],
            },
        ),
    ]
