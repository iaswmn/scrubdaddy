from django.conf.urls import url
from django.shortcuts import resolve_url
from django.views.generic.base import RedirectView

from . import views, views_ajax

urlpatterns = [
    url(r'^online-smile-shop/ajax/shop/$', views_ajax.ShopView.as_view(), name='ajax_shop'),


    url(r'^$', RedirectView.as_view(pattern_name='where_to_buy:retail', permanent=False), name='index'),
    url(r'^retail/$', views.RetailView.as_view(), name='retail'),
    url(r'^online-smile-shop/$', views.OnlineShopView.as_view(), name='shop'),
    url(r'^international/$', views.InternationalView.as_view(), name='international'),
]