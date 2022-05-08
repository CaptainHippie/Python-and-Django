from django.urls import path
from . import views

urlpatterns = [
    path('regapp/',views.UserRegistration),
]