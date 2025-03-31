from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .models import Note, Category
from .forms import NoteForm
from django.db.models import Q
from django.http import JsonResponse

class CreateNoteView(View):
    def get(self, request):
        form = NoteForm()
        return render(request, 'notes/create_note.html', {'form': form})

    def post(self, request):
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save()
            return JsonResponse({'id': note.id}, status=201)
        return render(request, 'notes/create_note.html', {'form': form})


def note_list(request):
    notes = Note.objects.all()
    return render(request, 'notes/note_list.html', {'notes': notes})


class NoteDetailView(View):
    def put(self, request, pk):
        note = get_object_or_404(Note, pk=pk)
        form = NoteForm(request.PUT, instance=note)
        if form.is_valid():
            form.save()
            return JsonResponse({'id': note.id}, status=200)
        return JsonResponse({'errors': form.errors}, status=400)





def delete_note(request, pk):
    note = get_object_or_404(Note, pk=pk)
    if request.method == 'DELETE':
        note.delete()
        return JsonResponse(status=204)
    return render(request, 'notes/delete_note.html', {'note': note})



def filter_notes(request):
    category = request.GET.get('category')
    reminder = request.GET.get('reminder')
    notes = Note.objects.all()

    if category:
        notes = notes.filter(category__name=category)
    if reminder:
        notes = notes.filter(reminder__date=reminder)

    return render(request, 'notes/note_list.html', {'notes': notes})



def search_notes(request):
    query = request.GET.get('q')
    if query:
        notes = Note.objects.filter(title__icontains=query)
    else:
        notes = Note.objects.all()
    return render(request, 'notes/note_list.html', {'notes': notes})