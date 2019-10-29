from django import forms
from django.conf import settings
from django.contrib import admin
from django.core.exceptions import ValidationError
from django.utils import dateformat
from django.utils.timezone import localtime
from django.utils.translation import ugettext_lazy as _
from solo.admin import SingletonModelAdmin
from suit.admin import SortableModelAdmin, SortableTabularInline

from attachable_blocks.admin import AttachableBlockAdmin, AttachedBlocksStackedInline
from libs.description import description
from project.admin import ModelAdminMixin, ModelAdminInlineMixin
from seo.admin import SeoModelAdminMixin
from .models import (
    ContactsConfig, Address, PhoneNumber, OpeningHours,
    NotificationReceiver, NotificationReceiverCanada, NotificationReceiverJobs,
    ContactBlock, Message,
)


class ContactsConfigBlocksInline(AttachedBlocksStackedInline):
    """ Подключаемые блоки """
    suit_classes = 'suit-tab suit-tab-blocks'


class NotificationReceiverAdmin(ModelAdminInlineMixin, admin.TabularInline):
    """ Получатели сообщений """
    model = NotificationReceiver
    extra = 0
    min_num = 1
    suit_classes = 'suit-tab suit-tab-notify'


class NotificationReceiverCanadaAdmin(ModelAdminInlineMixin, admin.TabularInline):
    """ Получатели сообщений """
    model = NotificationReceiverCanada
    extra = 0
    min_num = 1
    suit_classes = 'suit-tab suit-tab-notify-canada'


class NotificationReceiverJobsAdmin(ModelAdminInlineMixin, admin.TabularInline):
    """ Получатели сообщений """
    model = NotificationReceiverJobs
    extra = 0
    min_num = 1
    suit_classes = 'suit-tab suit-tab-notify-jobs'


@admin.register(ContactsConfig)
class ContactsConfigAdmin(SeoModelAdminMixin, SingletonModelAdmin):
    """ Главная страница """
    fieldsets = (
        (None, {
            'classes': ('suit-tab', 'suit-tab-general'),
            'fields': (
                'header',
            ),
        }),
    )
    inlines = (NotificationReceiverAdmin, NotificationReceiverCanadaAdmin, NotificationReceiverJobsAdmin,
               ContactsConfigBlocksInline)
    suit_form_tabs = (
        ('general', _('General')),
        ('notify', _('Notifications')),
        ('notify-canada', _('Notifications Canada')),
        ('notify-jobs', _('Notifications Jobs')),
        ('blocks', _('Blocks')),
    )


@admin.register(Message)
class ContactUsMessageAdmin(ModelAdminMixin, admin.ModelAdmin):
    """ Сообщение """
    fieldsets = (
        (None, {
            'classes': ('suit-tab', 'suit-tab-general'),
            'fields': (
                'name', 'phone', 'email',
            ),
        }),
        (_('Text'), {
            'classes': ('suit-tab', 'suit-tab-general'),
            'fields': (
                'message',
            ),
        }),
        (_('Info'), {
            'classes': ('suit-tab', 'suit-tab-general'),
            'fields': (
                'date_fmt',
                'referer',
            ),
        }),
    )
    readonly_fields = (
        'name', 'phone', 'email', 'message', 'date_fmt', 'referer')
    list_display = ('name', 'date_fmt')
    # inlines = (MessageImageInline,)
    suit_form_tabs = (
        ('general', _('General')),
    )

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return True

    def message_fmt(self, obj):
        return description(obj.message, 60, 80)

    def date_fmt(self, obj):
        return dateformat.format(localtime(obj.date), settings.DATETIME_FORMAT)

    date_fmt.short_description = _('Date')
    date_fmt.admin_order_field = 'date'

    message_fmt.short_description = _('Message')
    message_fmt.admin_order_field = 'message'


class PhoneNumberAdmin(ModelAdminInlineMixin, SortableTabularInline):
    model = PhoneNumber
    extra = 0
    sortable = 'sort_order'
    suit_classes = 'suit-tab suit-tab-phones'


class OpeningHoursForms(forms.ModelForm):
    class Meta:
        model = OpeningHours
        fields = '__all__'

    def clean_weekdays(self):
        value = tuple(sorted(self.cleaned_data['weekdays']))
        current = value[0]
        for day in value[1:]:
            if day != current + 1:
                raise ValidationError(_('the sequence must be continuous'))
            else:
                current = day
        return value


class OpeningHoursAdmin(ModelAdminInlineMixin, admin.StackedInline):
    model = OpeningHours
    form = OpeningHoursForms
    extra = 0
    sortable = 'sort_order'
    suit_classes = 'suit-tab suit-tab-hours'


@admin.register(Address)
class AddressAdmin(ModelAdminMixin, SortableModelAdmin):
    """ Адрес """
    fieldsets = (
        (None, {
            'classes': ('suit-tab', 'suit-tab-general'),
            'fields': (
                'address', 'city', 'region', 'zip', 'coords'
            ),
        }),
    )
    list_display = ('city', 'address',)
    sortable = 'sort_order'
    inlines = (PhoneNumberAdmin, OpeningHoursAdmin)
    suit_form_tabs = (
        ('general', _('General')),
        ('phones', _('Phones')),
        ('hours', _('Opening hours')),
    )

    class Media:
        js = (
            'contacts/admin/js/coords.js',
        )


@admin.register(ContactBlock)
class ContactBlockAdmin(AttachableBlockAdmin):
    """ Подключаемый блок с контактной формой """
    fieldsets = AttachableBlockAdmin.fieldsets + (
        (_('Customization'), {
            'classes': ('suit-tab', 'suit-tab-general'),
            'fields': ('header',),
        }),
    )
