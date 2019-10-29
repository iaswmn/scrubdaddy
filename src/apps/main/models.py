from django.db import models
from django.shortcuts import resolve_url
from django.utils.translation import ugettext_lazy as _, ugettext
from solo.models import SingletonModel

from libs.stdimage.fields import StdImageField
from libs.storages.media_storage import MediaStorage
from products.models import Product
from ckeditor.fields import CKEditorField, CKEditorUploadField


class MainPageConfig(SingletonModel):
    advantages_title = CKEditorField(_('advantages title'))
    updated = models.DateTimeField(_('change date'), auto_now=True)

    class Meta:
        default_permissions = ('change', )
        verbose_name = _('settings')

    def get_absolute_url(self):
        return resolve_url('index')

    def __str__(self):
        return ugettext('Home page')


class MainSlider(models.Model):
    slide_title = models.TextField(_('slide title for inner use'), max_length=255)
    title = models.TextField(_('title'), max_length=255, blank=True)
    description = models.TextField(_('description'), blank=True)
    product = models.ForeignKey(Product, verbose_name=_('product'), related_name='slides', blank=True, null=True)
    background = StdImageField(
        _('background'),
        storage=MediaStorage('main_slider/background'),
        min_dimensions=(400, 400),
        admin_variation='admin',
        crop_area=True,
        variations=dict(
            normal=dict(
                size=(1920, 0),
                crop=True
            ),
            tablet=dict(
                size=(1400, 0),
                crop=False
            ),
            mobile=dict(
                size=(320, 0),
                crop=False
            ),
            admin=dict(
                size=(480, 115),
                crop=False
            ),
        ),
    )

    background_alt = models.CharField(_('background alt'), max_length=255, blank=True, help_text=_('for SEO'))
    is_small_slide = models.BooleanField(_('small picture'), default=False)
    learn_more = models.BooleanField(_('Button Learn More'), default=True)
    order = models.PositiveSmallIntegerField()

    class Meta:
        verbose_name = _('slider')
        verbose_name_plural = _('Slider')
        ordering = ['order']

    def __str__(self):
        return self.slide_title


class Advantage(models.Model):
    title = models.CharField(_('title'), max_length=255)
    description = models.TextField(_('description'))
    preview = StdImageField(
        _('preview'),
        storage=MediaStorage('main/preview'),
        min_dimensions=(160, 160),
        admin_variation='admin',
        crop_area=True,
        variations=dict(
            normal=dict(
                size=(160, 160),
                crop=False
            ),
            admin=dict(
                size=(100, 100),
                crop=False
            ),
        ),
    )
    preview_alt = models.CharField(_('preview alt'), max_length=255, blank=True)
    sort_order = models.PositiveIntegerField(_('order'), default=0)
    updated = models.DateTimeField(_('change date'), auto_now=True)

    class Meta:
        verbose_name = _('advantage')
        verbose_name_plural = _('advantages')
        ordering = ['sort_order']

    def __str__(self):
        return self.title
