from django.urls import path
from .views import CreateNoteView, NoteDetailView, note_list, delete_note, filter_notes, search_notes

urlpatterns = [
    path('', note_list, name='note_list'),
    path('create/', CreateNoteView.as_view(), name='create_note'),
    path('note/<int:pk>/', NoteDetailView.as_view(), name='note_detail'),
    path('note/<int:pk>/delete/', delete_note, name='delete_note'),
    path('filter/', filter_notes, name='filter_notes'),
    path('search/', search_notes, name='search_notes'),
]