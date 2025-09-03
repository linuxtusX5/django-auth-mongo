from django.urls import path
from . import views

urlpatterns = [
    path('notes/', views.NoteListCreate.as_view(), name='note-list'), # Route for listing and creating notes 【2774.8, type: source】 
    path('notes/delete/<int:pk>/', views.NoteDelete.as_view(), name='delete-note'), # Route for deleting a specific note 【2774.8, type: source】 
]