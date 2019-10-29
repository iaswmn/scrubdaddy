from django.db import models
from django.shortcuts import resolve_url
from django.utils.dates import WEEKDAYS
from django.utils.formats import time_format
from django.utils.functional import cached_property
from django.utils.timezone import now
from django.utils.translation import ugettext_lazy as _
from solo.models import SingletonModel

from attachable_blocks.models import AttachableBlock
from google_maps.fields import GoogleCoordsField
from libs.multiselect_field.fields import MultiSelectField


class ContactsConfig(SingletonModel):
    """ Главная страница """
    header = models.CharField(_('header'), max_length=128)
    updated = models.DateTimeField(_('change date'), auto_now=True)

    class Meta:
        default_permissions = ('change', )
        verbose_name = _('settings')

    def get_absolute_url(self):
        return resolve_url('contacts:index')

    def __str__(self):
        return self.header


class Address(models.Model):
    """ Адрес """
    address = models.CharField(_('address'), max_length=255)
    city = models.CharField(_('city'), max_length=255)
    region = models.CharField(_('region'), max_length=64, blank=True)
    zip = models.CharField(_('zip'), max_length=32, blank=True)
    coords = GoogleCoordsField(_('coords'), blank=True)

    sort_order = models.PositiveIntegerField(_('sort order'))
    updated = models.DateTimeField(_('change date'), auto_now=True)

    class Meta:
        verbose_name = _('address')
        verbose_name_plural = _('addresses')
        ordering = ('sort_order', )

    @cached_property
    def phones(self):
        return tuple(PhoneNumber.objects.filter(address_id=self.id).values_list('number', flat=True))

    def __str__(self):
        return ', '.join(filter(bool, (self.city, self.address)))


class PhoneNumber(models.Model):
    address = models.ForeignKey(Address, related_name='+')
    number = models.CharField(_('number'), max_length=255, blank=True)
    phone_word = models.CharField(_('phone word'), max_length=16, blank=True)
    sort_order = models.PositiveIntegerField(_('sort order'))

    class Meta:
        verbose_name = _('phone')
        verbose_name_plural = _('phones')
        ordering = ('sort_order',)

    def __str__(self):
        return self.number


class OpeningHours(models.Model):
    WEEKDAYS_ABBR = tuple([
        _('Mo'), _('Tu'), _('We'), _('Th'), _('Fr'), _('Sa'), _('Su')
    ])
    WEEKDAYS_CHOICES = tuple(
        (key, value)
        for key, value in sorted(WEEKDAYS.items())
    )

    address = models.ForeignKey(Address, related_name='hours')
    weekdays = MultiSelectField(_('weekdays'), choices=WEEKDAYS_CHOICES)
    start_time = models.TimeField(_('from'), null=True)
    end_time = models.TimeField(_('to'), null=True)

    class Meta:
        verbose_name = _('opening hours sequence')
        verbose_name_plural = _('opening hours sequences')
        ordering = ('weekdays',)

    @cached_property
    def day_abbrs(self):
        days = (self.WEEKDAYS_ABBR[index] for index in sorted(self.weekdays))
        return tuple(map(str, days))

    @cached_property
    def day_names(self):
        days = (WEEKDAYS.get(index) for index in sorted(self.weekdays))
        return tuple(map(str, days))

    def __str__(self):
        days = list(self.weekdays)
        days_len = len(days)
        if days_len == 1:
            return '%s %s-%s' % (
                self.WEEKDAYS_ABBR[days[0]],
                time_format(self.start_time, 'H:i'),
                time_format(self.end_time, 'H:i'),
            )
        else:
            return '%s-%s %s-%s' % (
                self.WEEKDAYS_ABBR[days[0]],
                self.WEEKDAYS_ABBR[days[days_len - 1]],
                time_format(self.start_time, 'H:i'),
                time_format(self.end_time, 'H:i'),
            )


class NotificationReceiver(models.Model):
    """ Получатели писем с информацией о отправленных сообщениях """
    config = models.ForeignKey(ContactsConfig, related_name='receivers')
    email = models.EmailField(_('e-mail'))

    class Meta:
        verbose_name = _('notification receiver')
        verbose_name_plural = _('notification receivers')

    def __str__(self):
        return self.email


class NotificationReceiverCanada(models.Model):
    config = models.ForeignKey(ContactsConfig, related_name='receivers_canada')
    email = models.EmailField(_('e-mail'))

    class Meta:
        verbose_name = _('notification receiver Canada')
        verbose_name_plural = _('notification receivers Canada')

    def __str__(self):
        return self.email


class NotificationReceiverJobs(models.Model):
    config = models.ForeignKey(ContactsConfig, related_name='receivers_jobs')
    email = models.EmailField(_('e-mail'))

    class Meta:
        verbose_name = _('notification receiver jobs')
        verbose_name_plural = _('notification receivers jobs')

    def __str__(self):
        return self.email


class Message(models.Model):
    """ Сообщение """
    name = models.CharField(_('name'), max_length=128)
    phone = models.CharField(_('phone'), max_length=32, blank=True)
    email = models.EmailField(_('e-mail'), blank=True)
    message = models.TextField(_('message'), max_length=2048)
    date = models.DateTimeField(_('date sent'), default=now, editable=False)
    referer = models.CharField(_('from page'), max_length=512, blank=True, editable=False)

    class Meta:
        default_permissions = ('delete', )
        verbose_name = _('message')
        verbose_name_plural = _('messages')
        ordering = ('-date',)

    def __str__(self):
        return self.name


class GetInTouchMessage(models.Model):
    REACH_TYPE = (
        ('Phone', 'Phone'),
        ('Email', 'Email'),
    )
    TIME_ZONE = (
        ('ET', 'ET'),
        ('MT', 'MT'),
        ('CT', 'CT'),
    )
    name = models.CharField(_('name'), max_length=128)
    phone = models.CharField(_('phone number'), max_length=32, blank=True)
    email = models.EmailField(_('e-mail'), blank=True)
    comments = models.TextField(_('your comments'), max_length=2048)
    reach_type = models.CharField(
        _('How can we reach you?'),
        choices=REACH_TYPE,
        max_length=128,
        help_text='Hint: Inquiries are best answered with a quick chat!',
    )
    reach_time = models.CharField(_('Best time to reach you?'), max_length=128)
    time_zone = models.CharField(
        _('time zone'),
        choices=TIME_ZONE,
        max_length=128,
    )
    date = models.DateTimeField(_('date sent'), default=now, editable=False)
    referer = models.CharField(_('from page'), max_length=512, blank=True, editable=False)

    class Meta:
        default_permissions = ('delete', )
        verbose_name = _('message')
        verbose_name_plural = _('messages')
        ordering = ('-date',)

    def __str__(self):
        return self.name


class ContactBlock(AttachableBlock):
    """ Подключаемый блок с контактной формой """
    BLOCK_VIEW = 'contacts.views.contact_block_render'

    header = models.CharField(_('header'), max_length=128, blank=True)

    class Meta:
        verbose_name = _('Contact block')
        verbose_name_plural = _('Contact blocks')
