from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from solo.admin import SingletonModelAdmin
from suit.admin import SortableModelAdmin

from project.admin import ModelAdminMixin
from std_page.admin import StdPageAdmin
from .models import MediaConfig, MediaLink


@admin.register(MediaConfig)
class SupportConfigAdmin(StdPageAdmin, SingletonModelAdmin):
    fieldsets = StdPageAdmin.fieldsets + (
        (None, {
            'classes': ('suit-tab', 'suit-tab-general'),
            'fields': (
            ),
        }),
    )


@admin.register(MediaLink)
class MediaLinkAdmin(ModelAdminMixin, SortableModelAdmin):
    fieldsets = (
        (None, {
            'classes': ('suit-tab', 'suit-tab-general'),
            'fields': (
                'title', 'link', 'type', 'preview',
            ),
        }),
    )
    sortable = 'sort_order'
    suit_form_tabs = (
        ('general', _('General')),
    )
