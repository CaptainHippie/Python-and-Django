from django import views
from django.urls import path
from . import views

urlpatterns = [
    path('edit/<int:id>', views.markedit, name="edit"),
    path('delete/<int:id>', views.delete, name="del"),
    path('update/<int:id>', views.update, name="update"),
    path('submit_marks/',views.add_student, name="add"),
    path('student_data/',views.view_all_data, name="view"),
    path('search/',views.search_student, name="search")
]
