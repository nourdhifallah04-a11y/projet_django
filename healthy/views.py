from django.shortcuts import render, get_object_or_404, redirect
from .models import ProfilNutritionnel
from .forms import ProfilNutritionnelForm
from django.contrib.auth.decorators import login_required

# Liste des profils (optionnel)
@login_required
def profil_list(request):
    profils = ProfilNutritionnel.objects.filter(user=request.user)
    return render(request, 'nutrition/profil_list.html', {'profils': profils})

# Ajouter un profil
@login_required
def profil_create(request):
    if request.method == 'POST':
        form = ProfilNutritionnelForm(request.POST)
        if form.is_valid():
            profil = form.save(commit=False)
            profil.user = request.user
            profil.save()
            return redirect('profil_list')
    else:
        form = ProfilNutritionnelForm()
    return render(request, 'nutrition/profil_form.html', {'form': form})

# Modifier un profil
@login_required
def profil_update(request, pk):
    profil = get_object_or_404(ProfilNutritionnel, pk=pk, user=request.user)
    if request.method == 'POST':
        form = ProfilNutritionnelForm(request.POST, instance=profil)
        if form.is_valid():
            form.save()
            return redirect('profil_list')
    else:
        form = ProfilNutritionnelForm(instance=profil)
    return render(request, 'nutrition/profil_form.html', {'form': form})

# Supprimer un profil
@login_required
def profil_delete(request, pk):
    profil = get_object_or_404(ProfilNutritionnel, pk=pk, user=request.user)
    if request.method == 'POST':
        profil.delete()
        return redirect('profil_list')
    return render(request, 'nutrition/profil_confirm_delete.html', {'profil': profil})
