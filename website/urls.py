from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('check/', views.check_message, name='check_message'),
    path('scam-academy/', views.scam_academy, name='scam_academy'),
    path('emergency/', views.emergency_help, name='emergency_help'),
    path('family-link/', views.family_link, name='family_link'),
    path('official-numbers/', views.official_verification, name='official_verification'),
]
