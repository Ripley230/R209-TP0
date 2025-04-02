from django.urls import path

from . import views

urlpatterns = [
    path('formulaire/', views.formulaire),
    path('fruit/', views.fruit),
    path('sphère/', views.sphère),
    path('traitement/', views.traitement),
]