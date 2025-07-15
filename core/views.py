from django.views.generic import ListView, DetailView
from django.shortcuts import render, redirect
from .models import Note
from .forms import NoteForm

# CBV — список заміток
class NoteListView(ListView):
    model = Note
    template_name = 'notes/note_list.html'  # HTML шаблон для списку

# CBV — детальна замітка
class NoteDetailView(DetailView):
    model = Note
    template_name = 'notes/note_detail.html'  # HTML шаблон для однієї замітки

# FBV — додавання нової замітки
def add_note(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('note-list')
    else:
        form = NoteForm()
    return render(request, 'notes/add_note.html', {'form': form})
