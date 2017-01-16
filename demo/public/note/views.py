from django.core.urlresolvers import reverse
from django.views.generic import CreateView

from demo.apps.note.models import Note

from .forms import NoteForm


class NoteCreateView(CreateView):
    form_class = NoteForm
    model = Note
    template_name = 'note/create.html'

    def get_context_data(self, **kwargs):
        context = super(NoteCreateView, self).get_context_data(**kwargs)
        context['notes'] = Note.objects.all().order_by('-created')
        return context

    def get_success_url(self):
        return reverse('note:create')
