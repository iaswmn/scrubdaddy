from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from solo.admin import SingletonModelAdmin
from suit.admin import SortableModelAdmin

from project.admin import ModelAdminMixin
from std_page.admin import StdPageAdmin
from .models import RetailConfig, OnlineShopConfig, InternationalConfig, RetailShop, Country


@admin.register(RetailConfig)
class RetailConfigAdmin(StdPageAdmin, SingletonModelAdmin):
    fieldsets = StdPageAdmin.fieldsets + (
        (None, {
            'classes': ('suit-tab', 'suit-tab-general'),
            'fields': (
                'note', 'text_content', 'text_content_canada',
            ),
        }),
    )


@admin.register(OnlineShopConfig)
class OnlineShopConfigAdmin(StdPageAdmin, SingletonModelAdmin):
    fieldsets = StdPageAdmin.fieldsets + (
        (None, {
            'classes': ('suit-tab', 'suit-tab-general'),
            'fields': (
            ),
        }),
    )


@admin.register(InternationalConfig)
class InternationalConfigAdmin(StdPageAdmin, SingletonModelAdmin):
    fieldsets = StdPageAdmin.fieldsets + (
        (None, {
            'classes': ('suit-tab', 'suit-tab-general'),
            'fields': (
            ),
        }),
    )


@admin.register(RetailShop)
class ReatailShopAdmin(ModelAdminMixin, SortableModelAdmin):
    fieldsets = (
        (None, {
            'classes': ('suit-tab', 'suit-tab-general'),
            'fields': (
                'title', 'available_in_usa', 'available_in_canada',
            ),
        }),
    )
    suit_form_tabs = (
        ('general', _('General')),
    )


@admin.register(Country)
class CountryAdmin(ModelAdminMixin, SortableModelAdmin):
    fieldsets = (
        (None, {
            'classes': ('suit-tab', 'suit-tab-general'),
            'fields': (
                'country', 'link',
            ),
        }),
    )
    sortable = 'sort_order'
    suit_form_tabs = (
        ('general', _('General')),
    )
