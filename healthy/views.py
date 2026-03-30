from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from .forms import ProfilNutritionnelForm
from .models import ProfilNutritionnel


@login_required
def profil_list(request):
    profil = ProfilNutritionnel.objects.filter(user=request.user).first()
    return render(request, "healthy/profil_list.html", {"profil": profil})


@login_required
def profil_create(request):
    existing_profile = ProfilNutritionnel.objects.filter(user=request.user).first()
    if existing_profile:
        messages.info(request, "Votre profil nutritionnel existe deja.")
        return redirect("profil_update", pk=existing_profile.pk)

    if request.method == 'POST':
        form = ProfilNutritionnelForm(request.POST)
        if form.is_valid():
            profil = form.save(commit=False)
            profil.user = request.user
            profil.save()
            messages.success(request, "Profil nutritionnel cree avec succes.")
            return redirect("profil_list")
    else:
        form = ProfilNutritionnelForm()
    return render(request, "healthy/profil_form.html", {"form": form, "page_title": "Ajouter un profil"})


@login_required
def profil_update(request, pk):
    profil = get_object_or_404(ProfilNutritionnel, pk=pk, user=request.user)
    if request.method == 'POST':
        form = ProfilNutritionnelForm(request.POST, instance=profil)
        if form.is_valid():
            form.save()
            messages.success(request, "Profil nutritionnel mis a jour.")
            return redirect("profil_list")
    else:
        form = ProfilNutritionnelForm(instance=profil)
    return render(request, "healthy/profil_form.html", {"form": form, "page_title": "Modifier le profil"})


@login_required
def profil_delete(request, pk):
    profil = get_object_or_404(ProfilNutritionnel, pk=pk, user=request.user)
    if request.method == 'POST':
        profil.delete()
        messages.success(request, "Profil nutritionnel supprime.")
        return redirect("profil_list")
    return render(request, "healthy/profil_confirm_delete.html", {"profil": profil})
