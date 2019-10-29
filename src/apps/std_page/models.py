from django.db import models
from django.utils.translation import ugettext_lazy as _


class StdPage(models.Model):
    header = models.CharField(_('header'), max_length=255)
    
    updated = models.DateTimeField(_('change date'), auto_now=True)

    class Meta:
        abstract = True
        default_permissions = ('change',)
        verbose_name = _('settings')

    def __str__(self):
        return self.header