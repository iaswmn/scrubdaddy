from django.contrib import admin
from solo.admin import SingletonModelAdmin
from std_page.admin import StdPageAdmin
from .models import SupportConfig


@admin.register(SupportConfig)
class SupportConfigAdmin(StdPageAdmin, SingletonModelAdmin):
    fieldsets = StdPageAdmin.fieldsets + (
        (None, {
            'classes': ('suit-tab', 'suit-tab-general'),
            'fields': (
            ),
        }),
    )