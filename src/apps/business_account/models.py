from django.db import models
from django.shortcuts import resolve_url
from django.utils.timezone import now
from django.utils.translation import ugettext_lazy as _, ugettext
from solo.models import SingletonModel

from libs.file_field.fields import FileField
from std_page.models import StdPage


class ThanksPageConfig(SingletonModel):
    header = models.TextField(_('Page header'), max_length=64, blank=True)
    page_content = models.TextField(_('Page content'), max_length=512, blank=True)
    updated = models.DateTimeField(_('change date'), auto_now=True)

    class Meta:
        default_permissions = ('change',)
        verbose_name = _('Thank you page settings')

    def get_absolute_url(self):
        return resolve_url('business_account:thanks')

    def __str__(self):
        return ugettext('Open a business account thank you page')


class BusinessAccountConfig(StdPage, SingletonModel):

    class Meta(StdPage.Meta):
        pass

    def get_absolute_url(self):
        return resolve_url('business_account:index')

    def __str__(self):
        return ugettext('Open a business account')


class BusinessAccountMessage(models.Model):
    name = models.CharField(
        verbose_name=_('name'),
        max_length=128,
        help_text='First',
    )
    last_name = models.CharField(
        verbose_name=_('last name'),
        max_length=128,
        help_text='Last',
    )
    title = models.CharField(
        verbose_name=_('title'),
        max_length=128,
    )
    company_name = models.CharField(
        verbose_name=_('company name'),
        max_length=128,
    )
    date_of_commencement = models.DateTimeField(
        verbose_name=_('date of commencement'),
    )
    registered_company_address = models.CharField(
        verbose_name=_('registered street address'),
        max_length=128,
        help_text='Street Address',
    )
    company_street_address_2 = models.CharField(
        verbose_name=_('street address 2'),
        max_length=128,
        help_text='Street Address 2',
        blank=True,
    )
    company_city = models.CharField(
        verbose_name=_('city'),
        max_length=128,
        help_text='City',
    )
    company_state = models.CharField(
        verbose_name=_('state'),
        max_length=128,
        help_text='State / Province / Region',
    )
    company_zip = models.CharField(
        verbose_name=_('zip'),
        max_length=128,
        help_text='Zip Code',
    )
    company_country = models.CharField(
        verbose_name=_('country'),
        max_length=128,
        help_text='Country',
    )
    phone = models.CharField(
        verbose_name=_('phone'),
        max_length=32,
    )
    email = models.EmailField(
        verbose_name=_('Email'),
    )
    fax = models.CharField(
        verbose_name=_('fax'),
        max_length=32,
        blank=True,
    )
    website = models.CharField(
        verbose_name=_('website'),
        max_length=32,
    )

    wholesale = models.BooleanField(
        verbose_name=_('wholesale'),
        default=False,
    )
    distributor = models.BooleanField(
        verbose_name=_('distributor'),
        default=False,
    )
    retailer = models.BooleanField(
        verbose_name=_('retailer'),
        default=False,
    )
    broker = models.BooleanField(
        verbose_name=_('broker'),
        default=False,
    )

    trade_reference_company_name = models.CharField(
        verbose_name=_('Company name'),
        max_length=128,
    )
    trade_reference_street_address = models.CharField(
        verbose_name=_('Address'),
        max_length=128,
        help_text='Street Address',
    )
    trade_reference_street_address_2 = models.CharField(
        verbose_name=_('trade reference street address 2'),
        max_length=128,
        help_text='Street Address 2',
        blank = True,
    )
    trade_reference_city = models.CharField(
        verbose_name=_('trade reference city'),
        max_length=128,
        help_text='City',
    )
    trade_reference_state = models.CharField(
        verbose_name=_('trade reference state'),
        max_length=128,
        help_text='State / Province / Region',
    )
    trade_reference_zip = models.CharField(
        verbose_name=_('trade reference zip'),
        max_length=128,
        help_text='Zip Code',
    )
    trade_reference_country = models.CharField(
        verbose_name=_('trade reference country'),
        max_length=128,
        help_text='Country',
    )
    trade_reference_phone = models.CharField(
        verbose_name=_('Phone'),
        max_length=32,
    )
    trade_reference_email = models.EmailField(
        verbose_name=_('Email'),
    )
    trade_reference_fax = models.CharField(
        verbose_name=_('Fax'),
        max_length=32,
        blank=True,
    )

    trade_reference_2_company_name = models.CharField(
        verbose_name=_('Company name'),
        max_length=128,
    )
    trade_reference_2_street_address = models.CharField(
        verbose_name=_('Address'),
        max_length=128,
        help_text='Street Address',
    )
    trade_reference_2_street_address_2 = models.CharField(
        verbose_name=_('Address 2'),
        max_length=128,
        help_text='Street Address 2',
        blank=True,
    )
    trade_reference_2_city = models.CharField(
        verbose_name=_('City'),
        max_length=128,
        help_text='City',
    )
    trade_reference_2_state = models.CharField(
        verbose_name=_('State'),
        max_length=128,
        help_text='State / Province / Region',
    )
    trade_reference_2_zip = models.CharField(
        verbose_name=_('Zip'),
        max_length=128,
        help_text='Zip Code',
    )
    trade_reference_2_country = models.CharField(
        verbose_name=_('Country'),
        max_length=128,
        help_text='Country',
    )
    trade_reference_2_phone = models.CharField(
        verbose_name=_('Phone'),
        max_length=32,
    )
    trade_reference_2_email = models.EmailField(
        verbose_name=_('Email'),
    )
    trade_reference_2_fax = models.CharField(
        verbose_name=_('Fax'),
        max_length=32,
        blank=True,
    )
    date = models.DateTimeField(
        verbose_name=_('date sent'),
        default=now,
        editable=False,
    )

    class Meta:
        default_permissions = ('delete', )
        verbose_name = _('message')
        verbose_name_plural = _('messages')
        ordering = ('-date',)

    def __str__(self):
        return self.company_name


class BusinessAccountMessageSignature(models.Model):
    message = models.ForeignKey(BusinessAccountMessage, related_name='signatures')
    file = FileField(
        verbose_name=_('signature'),
        upload_to='business_account/signatures',
    )

    created = models.DateTimeField(_('created'), default=now, editable=False)

    class Meta:
        ordering = ('-created',)
        default_permissions = ('delete',)
        verbose_name = _('Signature')
        verbose_name_plural = _('Signatures')