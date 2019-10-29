from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from solo.admin import SingletonModelAdmin
from suit.admin import SortableModelAdmin

from project.admin import ModelAdminMixin, ModelAdminInlineMixin

from std_page.admin import StdPageAdmin
from .models import AboutConfig, Event, Hint


@admin.register(AboutConfig)
class AboutConfigAdmin(StdPageAdmin, SingletonModelAdmin):
    fieldsets = StdPageAdmin.fieldsets + (
        (None, {
            'classes': ('suit-tab', 'suit-tab-general'),
            'fields': (
                'text',
            ),
        }),
    )


class HintInline(ModelAdminInlineMixin, admin.TabularInline):
    model = Hint
    extra = 0
    suit_classes = 'suit-tab suit-tab-general'


@admin.register(Event)
class EventAdmin(ModelAdminMixin, SortableModelAdmin):
    fieldsets = (
        (None, {
            'classes': ('suit-tab', 'suit-tab-general'),
            'fields': (
                'year', 'title', 'text', 'image',
            ),
        }),
    )
    sortable = 'sort_order'
    inlines = (HintInline, )
    suit_form_tabs = (
        ('general', _('General')),
    )
