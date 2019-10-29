from django.db import models
from django.shortcuts import resolve_url
from django.utils.translation import ugettext_lazy as _, ugettext
from solo.models import SingletonModel

from ckeditor.fields import CKEditorField
from libs.stdimage.fields import StdImageField
from libs.storages.media_storage import MediaStorage
from ckeditor.fields import CKEditorUploadField
from std_page.models import StdPage


class AboutConfig(StdPage, SingletonModel):
    text = CKEditorUploadField(_('text'), blank=True)

    class Meta(StdPage.Meta):
        verbose_name = _('settings')

    def get_absolute_url(self):
        return resolve_url('about:index')

    def __str__(self):
        return ugettext('About')


class Event(models.Model):
    year = models.CharField(_('year'), max_length=255, blank=True)
    title = models.CharField(_('title'), max_length=255, blank=True)
    text = models.TextField(_('text'))
    image = StdImageField(
        _('image'),
        storage=MediaStorage('about/events'),
        min_dimensions=(240, 240),
        admin_variation='admin',
        variations=dict(
            normal=dict(
                size=(240, 0),
                crop=False
            ),
            admin=dict(
                size=(120, 0),
                crop=False
            ),
        ),
    )
    sort_order = models.PositiveIntegerField(_('order'), default=0)
    updated = models.DateTimeField(_('change date'), auto_now=True)

    class Meta:
        verbose_name = _('event')
        verbose_name_plural = _('events')
        ordering = ('sort_order', )

    def __str__(self):
        return self.title


class Hint(models.Model):
    POSITION = (
        ('top-left', 'top left'),
        ('top-center', 'top center'),
        ('top-right', 'top right'),
        ('right', 'right'),
        ('bottom-right', 'bottom right'),
        ('bottom-center', 'bottom center'),
        ('bottom-left', 'bottom left'),
        ('left', 'left'),
    )
    text = models.TextField(
        verbose_name=_('text'),
    )
    event = models.ForeignKey(
        to=Event,
        verbose_name=_('hint'),
        related_name='hints'
    )
    position = models.CharField(
        verbose_name=_('position'),
        choices=POSITION,
        max_length=64,
    )

    class Meta:
        verbose_name = _('hint')
        verbose_name_plural = _('hints')

    def __str__(self):
        return str(self.event)
