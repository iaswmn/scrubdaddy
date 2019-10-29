from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from solo.admin import SingletonModelAdmin
from suit.admin import SortableModelAdmin

from attachable_blocks.admin import AttachedBlocksStackedInline
from project.admin import ModelAdminMixin
from seo.admin import SeoModelAdminMixin
from .models import MainPageConfig, MainSlider, Advantage


class MainPageBlocksInline(AttachedBlocksStackedInline):
    """ Подключаемые блоки """
    suit_classes = 'suit-tab suit-tab-blocks'


@admin.register(MainPageConfig)
class MainPageConfigAdmin(SeoModelAdminMixin, SingletonModelAdmin):
    """ Главная страница """
    fieldsets = (
        (None, {
            'classes': ('suit-tab', 'suit-tab-general'),
            'fields': (
                'advantages_title',
            ),
        }),
    )
    inlines = (MainPageBlocksInline, )
    suit_form_tabs = (
        ('general', _('General')),
        ('blocks', _('Blocks')),
    )


@admin.register(MainSlider)
class MainSliderAdmin(ModelAdminMixin, SortableModelAdmin):
    fieldsets = (
        (None, {
            'classes': ('suit-tab', 'suit-tab-general'),
            'fields': (
              'slide_title', 'title',
              'product', 'description',
              'background', 'is_small_slide',
              'background_alt',
              'learn_more',
            ),
        }),
    )
    suit_form_tabs = (
        ('general', _('General')),
    )


@admin.register(Advantage)
class AdvantageAdmin(ModelAdminMixin, SortableModelAdmin):
    fieldsets = (
        (None, {
            'classes': ('suit-tab', 'suit-tab-general'),
            'fields': (
              'title', 'description', 'preview', 'preview_alt',
            ),
        }),
    )
    sortable = 'sort_order'
    suit_form_tabs = (
        ('general', _('General')),
    )
