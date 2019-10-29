from django.db import models
from django.shortcuts import resolve_url
from django.utils.translation import ugettext_lazy as _, ugettext
from solo.models import SingletonModel

from ckeditor.fields import CKEditorUploadField
from libs.stdimage.fields import StdImageField
from libs.storages.media_storage import MediaStorage
from products.models import Product
from std_page.models import StdPage


class QuestionsConfig(StdPage, SingletonModel):

    class Meta(StdPage.Meta):
        pass

    def get_absolute_url(self):
        return resolve_url('support:faq')

    def __str__(self):
        return ugettext('Questions')


class Question(models.Model):
    title = models.CharField(_('title'), max_length=255)
    text = CKEditorUploadField(_('text'))
    product = models.ManyToManyField(
        to=Product,
        verbose_name=_('product'),
        blank=True,
    )
    active = models.BooleanField(_('active'), default=False)
    visible = models.BooleanField(_('visible'), default=True)
    image = StdImageField(
        _('image'),
        null=True,
        blank=True,
        storage=MediaStorage('questions/images'),
        min_dimensions=(650, 0),
        admin_variation='admin',
        crop_area=True,
        variations=dict(
            normal=dict(
                size=(650, 0),
                crop=False
            ),
            admin=dict(
                size=(200, 0),
                crop=False
            ),
        ),
    )
    sort_order = models.PositiveIntegerField(_('order'), default=0)
    updated = models.DateTimeField(_('change date'), auto_now=True)

    class Meta:
        verbose_name = _('question')
        verbose_name_plural = _('questions')
        ordering = ('sort_order', )

    def __str__(self):
        return self.title
