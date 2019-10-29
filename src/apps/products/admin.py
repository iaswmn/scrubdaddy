from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from solo.admin import SingletonModelAdmin
from suit.admin import SortableModelAdmin

from attachable_blocks.admin import AttachedBlocksStackedInline, AttachableBlockAdmin
from seo.admin import SeoModelAdminMixin
from std_page.admin import StdPageAdmin
from .models import (ProductConfig, ProductCategory, Product, ProductVideoBlock, ProductFeatureBlock,
                     ProductTwoFeaturesBlock, )


class PageBlocksInline(AttachedBlocksStackedInline):
    suit_classes = 'suit-tab suit-tab-blocks'


@admin.register(ProductConfig)
class ProductConfigAdmin(StdPageAdmin, SingletonModelAdmin):
    fieldsets = StdPageAdmin.fieldsets + (
        (None, {
            'classes': ('suit-tab', 'suit-tab-general'),
            'fields': (
                'text',
            ),
        }),
    )


@admin.register(ProductCategory)
class ProductCategoryAdmin(SeoModelAdminMixin, SortableModelAdmin):
    fieldsets = (
        (None, {
            'classes': ('suit-tab', 'suit-tab-general'),
            'fields': (
                'title', 'slug', 'description', 'preview', 'preview_alt', 'background_color', 'show_on_faq_page',
            ),
        }),
    )
    sortable = 'sort_order'
    prepopulated_fields = {
        'slug': ('title', ),
    }
    suit_form_tabs = (
        ('general', _('General')),
    )


@admin.register(Product)
class ProductAdmin(SeoModelAdminMixin, SortableModelAdmin):
    fieldsets = (
        (None, {
            'classes': ('suit-tab', 'suit-tab-general'),
            'fields': (
                'title', 'text', 'background', 'preview', 'slug', 'show_button', 'category', 'link', 'description', 'available_in_usa',
                'available_in_canada', 'additional_text',
            ),
        }),
    )
    sortable = 'sort_order'
    inlines = (PageBlocksInline, )
    list_display = ('title', 'category',)
    prepopulated_fields = {
        'slug': ('title', ),
    }
    suit_form_tabs = (
        ('general', _('General')),
        ('blocks', _('Blocks')),
    )


@admin.register(ProductVideoBlock)
class ProductVideoBlockAdmin(AttachableBlockAdmin):
    fieldsets = AttachableBlockAdmin.fieldsets + (
        (_('Customization'), {
            'classes': ('suit-tab', 'suit-tab-general'),
            'fields': ('video',),
        }),
    )


@admin.register(ProductFeatureBlock)
class ProductFeatureBlockAdmin(AttachableBlockAdmin):
    fieldsets = AttachableBlockAdmin.fieldsets + (
        (_('Customization'), {
            'classes': ('suit-tab', 'suit-tab-general'),
            'fields': (
                'title', 'text', 'text_position', 'background',
            ),
        }),
    )


@admin.register(ProductTwoFeaturesBlock)
class ProductTwoFeaturesBlockAdmin(AttachableBlockAdmin):
    fieldsets = AttachableBlockAdmin.fieldsets + (
        (_('Customization'), {
            'classes': ('suit-tab', 'suit-tab-general'),
            'fields': (
                'title', 'text', 'preview', 'title_second', 'text_second', 'preview_second',
            ),
        }),
    )