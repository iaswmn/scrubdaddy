from django.db import models
from django.shortcuts import resolve_url
from django.utils.timezone import now
from django.utils.translation import ugettext_lazy as _
from solo.models import SingletonModel

from libs.file_field.fields import ImageField
from libs.storages.media_storage import MediaStorage


class GetInTouchConfig(SingletonModel):
    header = models.CharField(_('header'), max_length=128)
    updated = models.DateTimeField(_('change date'), auto_now=True)

    class Meta:
        default_permissions = ('change', )
        verbose_name = _('settings')

    def get_absolute_url(self):
        return resolve_url('get_in_touch:index')

    def __str__(self):
        return self.header


class GetInTouchMessage(models.Model):
    REACH_TYPE = (
        ('Phone', 'Phone'),
        ('Email', 'Email'),
    )
    TIME_ZONE = (
        ('ET', 'ET'),
        ('MT', 'MT'),
        ('CT', 'CT'),
        ('PT', 'PT'),
    )
    BEST_TIME = (
        ('8am-11am', '8am-11am'),
        ('11am-2pm', '11am-2pm'),
        ('2pm-5pm', '2pm-5pm'),
        ('5pm-8pm', '5pm-8pm'),
    )
    name = models.CharField(_('name'), max_length=128)
    location = models.CharField(_('Where are you located?'), max_length=64, blank=True)
    phone = models.CharField(_('phone number'), max_length=32, blank=True)
    email = models.EmailField(_('e-mail'))
    comments = models.TextField(_('your comments'), max_length=2048)
    reach_type = models.CharField(_('How can we reach you?'), choices=REACH_TYPE, max_length=128, help_text='Hint: Inquiries are best answered with a quick chat!', default=REACH_TYPE[1],)
    reach_time = models.CharField(_('Best time to reach you?'), choices=BEST_TIME, max_length=32, blank=True)
    time_zone = models.CharField(_('time zone'), choices=TIME_ZONE, max_length=128, blank=True)
    date = models.DateTimeField(_('date sent'), default=now, editable=False)
    referer = models.CharField(_('from page'), max_length=512, blank=True, editable=False)

    class Meta:
        default_permissions = ('delete', )
        verbose_name = _('message')
        verbose_name_plural = _('messages')
        ordering = ('-date',)

    def __str__(self):
        return self.name


class GetInTouchMessageImage(models.Model):
    message = models.ForeignKey(GetInTouchMessage, related_name='images')
    file = ImageField(
        verbose_name=_('image'),
        storage=MediaStorage('contacts/images'),
    )

    created = models.DateTimeField(_('created'), default=now, editable=False)

    class Meta:
        ordering = ('-created',)
        default_permissions = ('delete',)
        verbose_name = _('get in touch image')
        verbose_name_plural = _('get in touch images')
