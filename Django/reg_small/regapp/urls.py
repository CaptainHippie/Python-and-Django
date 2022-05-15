from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views

urlpatterns = [
    path('register/',views.UserRegistration),
    path('register/login/',views.UserLogin),
]

urlpatterns += staticfiles_urlpatterns()