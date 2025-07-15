from django.urls import path
from .views import NoteListView, NoteDetailView, add_note

urlpatterns = [
    path('', NoteListView.as_view(), name='note-list'),
    path('note/<int:pk>/', NoteDetailView.as_view(), name='note-detail'),
    path('add/', add_note, name='add-note'),
]
