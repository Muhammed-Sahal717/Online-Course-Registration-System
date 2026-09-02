from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('registrations/', views.registrations, name='registrations'),
    path('registrations/<int:pk>/', views.registration_detail, name='registration_detail'),
]