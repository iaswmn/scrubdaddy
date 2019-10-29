from django.db import models
from django.shortcuts import resolve_url
from django.utils.translation import ugettext_lazy as _, ugettext
from django_countries.fields import CountryField
from solo.models import SingletonModel
from ckeditor.fields import CKEditorField
from std_page.models import StdPage


class RetailConfig(StdPage, SingletonModel):
    text_content = CKEditorField(_('page content USA'), blank=True)
    text_content_canada = CKEditorField(_('page content Canada'), blank=True)
    note = models.TextField(_('note'), blank=True)

    class Meta(StdPage.Meta):
        verbose_name = _('Retail')

    def get_absolute_url(self):
        return resolve_url('where_to_buy:retail')

    def __str__(self):
        return ugettext('Where to buy')


class OnlineShopConfig(StdPage, SingletonModel):

    class Meta(StdPage.Meta):
        verbose_name = _('Online Smile Shop')

    def get_absolute_url(self):
        return resolve_url('where_to_buy:shop')

    def __str__(self):
        return ugettext('Where to buy')


class InternationalConfig(StdPage, SingletonModel):

    class Meta(StdPage.Meta):
        verbose_name = _('International')

    def get_absolute_url(self):
        return resolve_url('where_to_buy:international')

    def __str__(self):
        return ugettext('Where to buy')


class RetailShop(models.Model):
    title = models.CharField(_('title'), max_length=255)
    available_in_usa = models.BooleanField(_('available in usa'), default=True)
    available_in_canada = models.BooleanField(_('available in canada'), default=True)
    updated = models.DateTimeField(_('change date'), auto_now=True)

    class Meta:
        verbose_name = _('shop')
        verbose_name_plural = _('shops')

    def __str__(self):
        return self.title


class Country(models.Model):
    country = CountryField(_('country'))
    link = models.URLField(_('link'), blank=True)
    sort_order = models.PositiveIntegerField(_('order'), default=0)
    updated = models.DateTimeField(_('change date'), auto_now=True)

    class Meta:
        verbose_name = _('county')
        verbose_name_plural = _('countries')
        ordering = ('sort_order', )

    def __str__(self):
        return self.country.name
