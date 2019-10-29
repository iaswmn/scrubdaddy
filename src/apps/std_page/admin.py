from django.utils.translation import ugettext_lazy as _
from attachable_blocks.admin import AttachedBlocksStackedInline
from seo.admin import SeoModelAdminMixin


class PageBlocksInline(AttachedBlocksStackedInline):
    """ Подключаемые блоки """
    suit_classes = 'suit-tab suit-tab-blocks'


class StdPageAdmin(SeoModelAdminMixin):
    fieldsets = (
        (None, {
            'classes': ('suit-tab', 'suit-tab-general'),
            'fields': (
                'header',
            ),
        }),
    )
    inlines = (PageBlocksInline, )
    suit_form_tabs = (
        ('general', _('General')),
        ('blocks', _('Blocks')),
    )