from django import views
from django.urls import path
from . import views

urlpatterns = [
    path('add_book/',views.add_book, name="add_book"),
    path('view_books/',views.view_book, name="view_book"),
    path('search/',views.search_book, name="search_book")
]
