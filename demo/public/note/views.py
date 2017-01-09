from django.core.urlresolvers import reverse
from django.views.generic import CreateView
from redis import Redis

from demo.apps.note.models import Note


redis = Redis(host='cache', port=6379)


class NoteCreateView(CreateView):
    fields = ['text', ]
    model = Note
    template_name = 'note/create.html'

    def get_context_data(self, **kwargs):
        context = super(NoteCreateView, self).get_context_data(**kwargs)
        context['views_counter'] = redis.incr('views_counter')
        context['notes'] = Note.objects.all().order_by('-created')
        return context

    def get_success_url(self):
        return reverse('note:create')
