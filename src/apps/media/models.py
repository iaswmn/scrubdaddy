from django.db import models
from django.shortcuts import resolve_url
from django.utils.translation import ugettext_lazy as _, ugettext
from solo.models import SingletonModel

from std_page.models import StdPage
from libs.stdimage.fields import StdImageField
from libs.storages.media_storage import MediaStorage


class MediaConfig(StdPage, SingletonModel):

    class Meta(StdPage.Meta):
        pass

    def get_absolute_url(self):
        return resolve_url('support:media')

    def __str__(self):
        return ugettext('Media')


class MediaLink(models.Model):
    MEDIA_TYPE = (
        ('VI', 'Video'),
        ('AU', 'Audio'),
        ('AR', 'Article'),
    )
    title = models.CharField(_('title'), max_length=255)
    type = models.CharField(_('type'), choices=MEDIA_TYPE, max_length=255)
    link = models.URLField(_('url'))
    preview = StdImageField(
        _('preview'),
        storage=MediaStorage('media/previews'),
        min_dimensions=(280, 180),
        admin_variation='admin',
        crop_area=True,
        variations=dict(
            normal=dict(
                size=(280, 180),
                crop=True
            ),
            admin=dict(
                size=(140, 90),
                crop=False
            ),
        ),
    )
    sort_order = models.PositiveIntegerField(_('order'), default=0)
    updated = models.DateTimeField(_('change date'), auto_now=True)

    class Meta:
        verbose_name = _('media link')
        verbose_name_plural = _('media links')
        ordering = ('sort_order', )

    def __str__(self):
        return self.title
