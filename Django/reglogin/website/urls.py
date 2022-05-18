from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_req, name='log'),
    path('dashboard/', views.logout, name='logout')
]