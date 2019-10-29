from django.db import models
from django.utils.translation import ugettext_lazy as _
from solo.models import SingletonModel


class Config(SingletonModel):
    shop_link = models.URLField(_('smile shop link'))
    updated = models.DateTimeField(_('change date'), auto_now=True)

    class Meta:
        default_permissions = ('change', )
        verbose_name = _('settings')
