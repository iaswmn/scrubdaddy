from django.db import models
from django.shortcuts import get_object_or_404
from django.shortcuts import resolve_url
from django.template import loader
from django.views.generic import TemplateView

from libs.views import CachedViewMixin
from menu.utils import activate_menu
from seo.seo import Seo
from .models import ProductConfig, ProductCategory, Product


class IndexView(CachedViewMixin, TemplateView):
    template_name = 'products/index.html'
    config = None
    categories = None

    def last_modified(self, request, *args, **kwargs):
        self.config = ProductConfig.get_solo()
        country = request.META.get('GEOIP_COUNTRY')
        if country == 'CA':
            self.categories = ProductCategory.objects.filter(
                products__available_in_canada=True,
            ).distinct()[0:5]
        else:
            self.categories = ProductCategory.objects.filter(
                products__available_in_usa=True,
            ).distinct()[0:5]
        return self.config.updated, self.categories.aggregate(models.Max('updated'))['updated__max']

    def get(self, request, *args, **kwargs):
        seo = Seo()
        seo.set_data(self.config)
        seo.save(request)
        request.breadcrumbs.add('Product Family', resolve_url('products:index'))

        return self.render_to_response({
            'page_data': self.config,
            'categories': self.categories,
        })


class CategoryView(CachedViewMixin, TemplateView):
    template_name = 'products/category.html'
    config = None
    category = None
    categories = None
    products = None

    def last_modified(self, request, *args, slug=None, **kwargs):
        self.config = ProductConfig.get_solo()
        self.category = get_object_or_404(ProductCategory, slug=slug) if slug else None
        country = request.META.get('GEOIP_COUNTRY')
        if country == 'CA':
            self.products = Product.objects.filter(
                category=self.category,
                available_in_canada=True,
            )
            self.categories = ProductCategory.objects.filter(
                products__available_in_canada=True,
            ).distinct()[:5]
        else:
            self.products = Product.objects.filter(
                category=self.category,
                available_in_usa=True,
            )
            self.categories = ProductCategory.objects.filter(
                products__available_in_usa=True,
            ).distinct()[:5]
        return self.category.updated, self.products.aggregate(models.Max('updated'))['updated__max']

    def get(self, request, *args, **kwargs):
        seo = Seo()
        seo.set_data(self.category, defaults={
            'title': self.category.title,
        })
        seo.save(request)

        activate_menu(request, 'products')

        request.breadcrumbs.add(self.category.title, self.category.get_absolute_url())

        return self.render_to_response({
            'page_data': self.config,
            'products': self.products,
            'categories': self.categories,
            'current_category': self.category,
            'is_product_category_page': True,
        })


class DetailView(CachedViewMixin, TemplateView):
    template_name = 'products/detail.html'
    config = None
    product = None
    related_products = None

    def last_modified(self, *args, slug=None, **kwargs):
        self.config = ProductConfig.get_solo()
        self.product = get_object_or_404(Product, slug=slug)
        return self.config.updated, self.product.updated

    def get(self, request, *args, **kwargs):
        seo = Seo()
        seo.set_data(self.product, defaults={
            'title': self.product.title,
        })
        seo.save(request)

        activate_menu(request, 'products')

        request.breadcrumbs.add(self.product.category.title, self.product.category.get_absolute_url())
        request.breadcrumbs.add(self.product.title, self.product.get_absolute_url())

        country = request.META.get('GEOIP_COUNTRY')
        if country == 'CA':
            self.related_products = Product.objects.filter(
                available_in_canada=True,
            ).exclude(
                pk=self.product.pk
            )
        else:
            self.related_products = Product.objects.filter(
                available_in_usa=True,
            ).exclude(
                pk=self.product.pk
            )

        return self.render_to_response({
            'page_data': self.config,
            'product': self.product,
            'related_products': self.related_products,
            'is_product_page': True,
        })


def product_video_block_render(context, block, **kwargs):
    return loader.render_to_string('products/video_block.html', {
        'block': block,
    }, request=context.get('request'))


def product_feature_block_render(context, block, **kwargs):
    return loader.render_to_string('products/feature_block.html', {
        'block': block,
    }, request=context.get('request'))


def product_two_features_block_render(context, block, **kwargs):
    return loader.render_to_string('products/two_features_block.html', {
        'block': block,
    }, request=context.get('request'))
