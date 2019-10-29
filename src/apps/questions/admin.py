from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from solo.admin import SingletonModelAdmin
from suit.admin import SortableModelAdmin

from project.admin import ModelAdminMixin
from std_page.admin import StdPageAdmin
from .models import QuestionsConfig, Question


@admin.register(QuestionsConfig)
class SupportConfigAdmin(StdPageAdmin, SingletonModelAdmin):
    fieldsets = StdPageAdmin.fieldsets + (
        (None, {
            'classes': ('suit-tab', 'suit-tab-general'),
            'fields': (
            ),
        }),
    )


@admin.register(Question)
class ProductAdmin(ModelAdminMixin, SortableModelAdmin):
    fieldsets = (
        (None, {
            'classes': ('suit-tab', 'suit-tab-general'),
            'fields': (
                'title', 'text', 'image', 'product', 'visible', 'active',
            ),
        }),
    )
    filter_horizontal = ('product',)
    sortable = 'sort_order'
    suit_form_tabs = (
        ('general', _('General')),
    )
