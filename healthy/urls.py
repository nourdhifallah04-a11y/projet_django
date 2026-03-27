from django.urls import path
from . import views

urlpatterns = [
    path('', views.profil_list, name='profil_list'),
    path('ajouter/', views.profil_create, name='profil_create'),
    path('modifier/<int:pk>/', views.profil_update, name='profil_update'),
    path('supprimer/<int:pk>/', views.profil_delete, name='profil_delete'),
]
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('nutrition/', include('nutrition.urls')),
]