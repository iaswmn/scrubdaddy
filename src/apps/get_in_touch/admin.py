from django.conf import settings
from django.contrib import admin
from django.utils import dateformat
from django.utils.timezone import localtime
from django.utils.translation import ugettext_lazy as _
from project.admin import ModelAdminMixin, ModelAdminInlineMixin
from solo.admin import SingletonModelAdmin

from seo.admin import SeoModelAdminMixin
from .models import GetInTouchConfig, GetInTouchMessage, GetInTouchMessageImage


@admin.register(GetInTouchConfig)
class GetInTouchConfigAdmin(SeoModelAdminMixin, SingletonModelAdmin):
    fieldsets = (
        (None, {
            'classes': ('suit-tab', 'suit-tab-general'),
            'fields': (
                'header',
            ),
        }),
    )
    suit_form_tabs = (
        ('general', _('General')),
        ('notify', _('Notifications')),
        ('blocks', _('Blocks')),
    )


class MessageImageInline(ModelAdminInlineMixin, admin.TabularInline):
    model = GetInTouchMessageImage
    extra = 0
    suit_classes = 'suit-tab suit-tab-general'
    readonly_fields = (
        'file',
    )

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(GetInTouchMessage)
class GetInTouchMessageAdmin(ModelAdminMixin, admin.ModelAdmin):
    """ Сообщение """
    fieldsets = (
        (None, {
            'classes': ('suit-tab', 'suit-tab-general'),
            'fields': (
                'name', 'location', 'phone', 'email', 'reach_type', 'reach_time', 'time_zone',
            ),
        }),
        (_('Text'), {
            'classes': ('suit-tab', 'suit-tab-general'),
            'fields': (
                'comments',
            ),
        }),
        (_('Info'), {
            'classes': ('suit-tab', 'suit-tab-general'),
            'fields': (
                'date_fmt', 'referer',
            ),
        }),
    )
    readonly_fields = ('name', 'location', 'reach_type', 'reach_time', 'time_zone', 'phone', 'email', 'comments', 'date_fmt', 'referer')
    list_display = ('name', 'date_fmt')
    inlines = (MessageImageInline, )
    suit_form_tabs = (
        ('general', _('General')),
    )

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return True

    def date_fmt(self, obj):
        return dateformat.format(localtime(obj.date), settings.DATETIME_FORMAT)
    date_fmt.short_description = _('Date')
    date_fmt.admin_order_field = 'date'
