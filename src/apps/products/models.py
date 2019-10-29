from django.db import models
from django.shortcuts import resolve_url
from django.utils.translation import ugettext_lazy as _, ugettext
from solo.models import SingletonModel

from attachable_blocks.models import AttachableBlock
from ckeditor.fields import CKEditorField, CKEditorUploadField
from libs.autoslug import AutoSlugField
from libs.color_field.fields import ColorField
from libs.stdimage.fields import StdImageField
from libs.storages.media_storage import MediaStorage
from libs.videolink_field.fields import VideoLinkField
from std_page.models import StdPage


class ProductConfig(StdPage, SingletonModel):
    text = CKEditorField(_('text'), blank=True)

    class Meta(StdPage.Meta):
        pass

    def get_absolute_url(self):
        return resolve_url('products:index')

    def __str__(self):
        return ugettext('Product')


class ProductCategory(models.Model):
    title = models.TextField(_('title'), max_length=255)
    description = CKEditorUploadField(_('Description'), blank=True)
    slug = AutoSlugField(_('slug'), populate_from='title', unique=True)
    preview = StdImageField(
        _('preview'),
        storage=MediaStorage('product/previews'),
        min_dimensions=(340, 370),
        admin_variation='admin',
        crop_area=True,
        variations=dict(
            normal=dict(
                size=(340, 370),
                crop=True
            ),
            admin=dict(
                size=(170, 185),
                crop=False
            ),
        ),
    )
    preview_alt = models.CharField(_('preview img alt'), blank=True, max_length=255)
    background_color = ColorField(_('background color'), blank=True, default='#FF0000')
    show_on_faq_page = models.BooleanField(_('show on FAQ page'), default=True)
    sort_order = models.PositiveIntegerField(_('order'), default=0)
    updated = models.DateTimeField(_('change date'), auto_now=True)

    class Meta:
        verbose_name = _('category')
        verbose_name_plural = _('categories')
        ordering = ('sort_order', )

    def get_absolute_url(self):
        return resolve_url('root_router', slug=self.slug)

    def __str__(self):
        return self.title


class Product(models.Model):
    category = models.ForeignKey(
        to=ProductCategory,
        verbose_name=_('category'),
        related_name='products',
    )
    title = models.CharField(_('title'), max_length=255)
    description = models.CharField(_('description'), max_length=255)
    show_button = models.BooleanField(_('show shop me button'), default=True)
    text = models.TextField(_('text'), blank=True)
    available_in_usa = models.BooleanField(_('available in usa'), default=True)
    available_in_canada = models.BooleanField(_('available in canada'), default=True)
    preview = StdImageField(
        _('image'),
        storage=MediaStorage('product/images'),
        min_dimensions=(280, 0),
        admin_variation='admin',
        crop_area=True,
        variations=dict(
            normal=dict(
                size=(280, 0),
                crop=False
            ),
            admin=dict(
                size=(100, 0),
                crop=False
            ),
        ),
    )
    background = StdImageField(
        _('background image'),
        storage=MediaStorage('product/features'),
        min_dimensions=(1180, 0),
        admin_variation='admin',
        crop_area=True,
        variations=dict(
            normal=dict(
                size=(1180, 0),
                crop=False
            ),
            tablet=dict(
                size=(768, 326),
                crop=False
            ),
            mobile=dict(
                size=(500, 213),
                crop=False
            ),
            admin=dict(
                size=(200, 0),
                crop=False
            ),
        ),
    )
    link = models.URLField(_('shop url'))
    slug = AutoSlugField(_('slug'), populate_from='title', unique=True)
    additional_text = CKEditorField(_('additional text'), blank=True)

    sort_order = models.PositiveIntegerField(_('order'), default=0)
    updated = models.DateTimeField(_('change date'), auto_now=True)

    class Meta:
        verbose_name = _('product')
        verbose_name_plural = _('products')
        ordering = ('sort_order', )

    def get_absolute_url(self):
        return resolve_url('root_router', slug=self.slug)

    def __str__(self):
        return self.title


class ProductVideoBlock(AttachableBlock):
    BLOCK_VIEW = 'products.views.product_video_block_render'

    video = VideoLinkField(_('video'), providers=('youtube',))

    class Meta:
        verbose_name = _('Product video block')
        verbose_name_plural = _('Product video blocks')


class ProductFeatureBlock(AttachableBlock):
    BLOCK_VIEW = 'products.views.product_feature_block_render'

    LEFT = 'left'
    RIGHT = 'right'
    TEXT_BLOCK_POSITION = (
        (LEFT, 'left'),
        (RIGHT, 'right'),
    )
    title = models.CharField(_('feature title'), max_length=255, blank=True)
    text = CKEditorField(_('feature text'), blank=True)
    text_position = models.CharField(_('feature text position'), choices=TEXT_BLOCK_POSITION, default=LEFT, max_length=64)
    background = StdImageField(
        _('background image'),
        storage=MediaStorage('product/features'),
        min_dimensions=(1180, 0),
        admin_variation='admin',
        crop_area=True,
        variations=dict(
            normal=dict(
                size=(1180, 0),
                crop=False
            ),
            tablet=dict(
                size=(768, 326),
                crop=False
            ),
            mobile=dict(
                size=(500, 213),
                crop=False
            ),
            admin=dict(
                size=(200, 0),
                crop=False
            ),
        ),
    )

    class Meta:
        verbose_name = _('Product feature block')
        verbose_name_plural = _('Product feature blocks')


class ProductTwoFeaturesBlock(AttachableBlock):
    BLOCK_VIEW = 'products.views.product_two_features_block_render'

    title = models.CharField(_('feature title'), max_length=255, blank=True)
    text = CKEditorField(_('feature text'), blank=True)
    preview = StdImageField(
        _('feature image'),
        storage=MediaStorage('product/features'),
        min_dimensions=(580, 0),
        admin_variation='admin',
        crop_area=True,
        variations=dict(
            normal=dict(
                size=(580, 0),
                crop=False,
            ),
            tablet=dict(
                size=(380, 470),
                crop=False,
            ),
            mobile=dict(
                size=(400, 495),
                crop=False,
            ),
            admin=dict(
                size=(100, 100),
                crop=False,
            ),
        ),
    )

    title_second = models.CharField(_('second feature title'), max_length=255, blank=True)
    text_second = CKEditorField(_('second feature text'), blank=True)
    preview_second = StdImageField(
        _('second feature image'),
        storage=MediaStorage('product/features'),
        min_dimensions=(580, 720),
        admin_variation='admin',
        crop_area=True,
        variations=dict(
            normal=dict(
                size=(580, 0),
                crop=False,
            ),
            tablet=dict(
                size=(380, 470),
                crop=False,
            ),
            mobile=dict(
                size=(400, 495),
                crop=False,
            ),
            admin=dict(
                size=(100, 100),
                crop=False,
            ),
        ),
    )

    class Meta:
        verbose_name = _('Product two features block')
        verbose_name_plural = _('Product two features blocks')
