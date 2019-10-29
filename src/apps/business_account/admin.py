from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from solo.admin import SingletonModelAdmin

from project.admin import ModelAdminInlineMixin
from project.admin import ModelAdminMixin
from std_page.admin import StdPageAdmin
from .models import BusinessAccountConfig, BusinessAccountMessage, BusinessAccountMessageSignature, ThanksPageConfig


@admin.register(BusinessAccountConfig)
class SupportConfigAdmin(StdPageAdmin, SingletonModelAdmin):
    fieldsets = StdPageAdmin.fieldsets + (
        (None, {
            'classes': ('suit-tab', 'suit-tab-general'),
            'fields': (
            ),
        }),
    )


class BusinessAccountMessageSignatureInline(ModelAdminInlineMixin, admin.TabularInline):
    model = BusinessAccountMessageSignature
    extra = 0
    suit_classes = 'suit-tab suit-tab-general'
    readonly_fields = (
        'file',
    )

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(ThanksPageConfig)
class ThanksPageConfigAdmin(ModelAdminMixin, SingletonModelAdmin):
    fieldsets = (
        (None, {
            'classes': ('suit-tab', 'suit-tab-general'),
            'fields': (
                'header', 'page_content',
            )
        }),
    )
    suit_form_tabs = (
        ('general', _('General')),
    )

@admin.register(BusinessAccountMessage)
class BusinessAccountMessageAdmin(ModelAdminMixin, admin.ModelAdmin):
    fieldsets = (
        (None, {
            'classes': ('suit-tab', 'suit-tab-general'),
            'fields': (
                'name', 'last_name', 'title', 'company_name', 'date_of_commencement',
                'registered_company_address', 'company_street_address_2', 'company_city',
                'company_state', 'company_zip', 'company_country', 'phone', 'email', 'fax',
                'website', 'wholesale', 'distributor', 'retailer', 'broker',
            ),
        }),
        ('Trade reference', {
            'classes': ('suit-tab', 'suit-tab-general'),
            'fields': (
                'trade_reference_company_name', 'trade_reference_street_address',
                'trade_reference_street_address_2', 'trade_reference_city',
                'trade_reference_state', 'trade_reference_zip', 'trade_reference_country',
                'trade_reference_phone', 'trade_reference_email', 'trade_reference_fax',
            ),
        }),
        ('Trade reference 2', {
            'classes': ('suit-tab', 'suit-tab-general'),
            'fields': (
                'trade_reference_2_company_name', 'trade_reference_2_street_address',
                'trade_reference_2_street_address_2', 'trade_reference_2_city',
                'trade_reference_2_state', 'trade_reference_2_zip', 'trade_reference_2_country',
                'trade_reference_2_phone', 'trade_reference_2_email', 'trade_reference_2_fax',
            ),
        }),
    )
    readonly_fields = (
        'name', 'last_name', 'title', 'company_name', 'date_of_commencement',
        'registered_company_address', 'company_street_address_2', 'company_city',
        'company_state', 'company_zip', 'company_country', 'phone', 'email', 'fax',
        'website', 'wholesale', 'distributor', 'retailer', 'broker',
        'trade_reference_company_name', 'trade_reference_street_address',
        'trade_reference_street_address_2', 'trade_reference_city',
        'trade_reference_state', 'trade_reference_zip', 'trade_reference_country',
        'trade_reference_phone', 'trade_reference_email', 'trade_reference_fax',
        'trade_reference_2_company_name', 'trade_reference_2_street_address',
        'trade_reference_2_street_address_2', 'trade_reference_2_city',
        'trade_reference_2_state', 'trade_reference_2_zip', 'trade_reference_2_country',
        'trade_reference_2_phone', 'trade_reference_2_email', 'trade_reference_2_fax',
    )
    inlines = (
        BusinessAccountMessageSignatureInline,
    )
    suit_form_tabs = (
        ('general', _('General')),
    )
