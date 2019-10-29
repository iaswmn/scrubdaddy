from django.db import models
from django.shortcuts import resolve_url
from django.views.generic import TemplateView

from config.models import Config
from libs.views import CachedViewMixin
from seo.seo import Seo
from .models import RetailConfig, OnlineShopConfig, InternationalConfig, Country


class RetailView(CachedViewMixin, TemplateView):
    template_name = 'where_to_buy/retail.html'
    config = None
    shops = None
    country = None

    def last_modified(self, request, *args, **kwargs):
        self.config = RetailConfig.get_solo()
        return self.config.updated

    def get(self, request, *args, **kwargs):
        seo = Seo()
        seo.set_data(self.config)
        seo.save(request)
        request.breadcrumbs.add('Retail', resolve_url('where_to_buy:retail'))
        country = request.META.get('GEOIP_COUNTRY')
        print(country)
        if country == 'CA':
            self.country = 'CA'

        if country == 'IL':
            self.country = 'IL'

        return self.render_to_response({
            'page_data': self.config,
            'country': self.country
        })


class OnlineShopView(CachedViewMixin, TemplateView):
    template_name = 'where_to_buy/online_shop.html'
    config = None

    def last_modified(self, *args, **kwargs):
        self.config = OnlineShopConfig.get_solo()
        return self.config.updated

    def get(self, request, *args, **kwargs):
        seo = Seo()
        seo.set_data(self.config)
        seo.save(request)
        request.breadcrumbs.add('Online Smile Shop', resolve_url('where_to_buy:shop'))

        return self.render_to_response({
            'page_data': self.config,
            'site_config': Config.get_solo(),
            'country': request.META.get('GEOIP_COUNTRY'),
        })


class InternationalView(CachedViewMixin, TemplateView):
    template_name = 'where_to_buy/international.html'
    config = None
    countries = None

    def last_modified(self, *args, **kwargs):
        self.config = InternationalConfig.get_solo()
        self.countries = Country.objects.all()
        return self.config.updated, self.countries.aggregate(models.Max('updated'))['updated__max']

    def get(self, request, *args, **kwargs):
        seo = Seo()
        seo.set_data(self.config)
        seo.save(request)
        request.breadcrumbs.add('International', resolve_url('where_to_buy:international'))

        return self.render_to_response({
            'page_data': self.config,
            'countries': self.countries,
        })
