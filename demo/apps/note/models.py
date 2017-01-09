from django.db import models
from django.utils.translation import ugettext_lazy as _


class Note(models.Model):
    text = models.CharField(max_length=128, verbose_name=_('Text'))
    created = models.DateTimeField(auto_now_add=True, verbose_name=_('Creation date'))

    class Meta:
        verbose_name = _('Note')
        verbose_name_plural = _('Notes')
