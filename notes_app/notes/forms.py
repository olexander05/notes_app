from django import forms
from .models import Note, Category

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'text', 'reminder', 'category']
        widgets = {
            'reminder': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }