from django import forms

from demo.apps.note.models import Note


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['text', ]

    def __init__(self, *args, **kwargs):
        super(NoteForm, self).__init__(*args, **kwargs)
        self.fields['text'].widget.attrs['placeholder'] = 'Enter a message'
