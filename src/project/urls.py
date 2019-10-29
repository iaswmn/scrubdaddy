from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.http import Http404

from admin_honeypot.admin import honeypot_site
from libs.autoslug import ALIAS_REGEXP
from main import views as main_views
from contacts import views as contact_views
from .sitemaps import site_sitemaps


def root_router(request, *args, **kwargs):
    """
        Роутер для страниц вида /slug/
    """
    from products.models import ProductCategory, Product
    from products.views import CategoryView, DetailView

    slug = kwargs.get('slug')
    if ProductCategory.objects.filter(slug=slug).exists():
        return CategoryView.as_view()(request, *args, **kwargs)
    elif Product.objects.filter(slug=slug).exists():
        return DetailView.as_view()(request, *args, **kwargs)
    else:
        raise Http404


urlpatterns = [
    url(r'^admin/', include(honeypot_site.urls)),
    url(r'^dladmin/social/', include('social_networks.admin_urls', namespace='admin_social_networks')),
    url(r'^dladmin/autocomplete/', include('libs.autocomplete.urls', namespace='autocomplete')),
    url(r'^dladmin/ckeditor/', include('ckeditor.admin_urls', namespace='admin_ckeditor')),
    url(r'^dladmin/gallery/', include('gallery.admin_urls', namespace='admin_gallery')),
    url(r'^dladmin/users/', include('users.admin_urls', namespace='admin_users')),
    url(r'^dladmin/ctr/', include('admin_ctr.urls', namespace='admin_ctr')),
    url(r'^dladmin/', include(admin.site.urls)),

    url(r'^$', main_views.IndexView.as_view(), name='index'),
    url(r'^404/$', 'django.views.defaults.page_not_found'),
    url(r'^500/$', 'django.views.defaults.server_error'),
    url(r'^away/$', 'libs.away.views.away', name='away'),
    url(r'^jsi18n/$', 'project.views.cached_javascript_catalog', name='jsi18n'),
    url(r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': site_sitemaps}),
    url(r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': site_sitemaps}),

    url(r'^ckeditor/', include('ckeditor.urls', namespace='ckeditor')),
    url(r'^blocks/', include('attachable_blocks.urls', namespace='blocks')),
    url(r'^placeholder/', include('placeholder.urls', namespace='placeholder')),
    url(r'^social/', include('social_networks.urls', namespace='social_networks')),
    url(r'^rating/', include('rating.urls', namespace='rating')),

    url(r'^about/', include('about.urls', namespace='about')),
    url(r'^products/', include('products.urls', namespace='products')),
    url(r'^support-and-discover/', include('support.urls', namespace='support')),
    url(r'^media/', include('media.urls', namespace='media')),
    url(r'^where-to-buy/', include('where_to_buy.urls', namespace='where_to_buy')),
    url(r'^open-a-business-account/', include('business_account.urls', namespace='business_account')),
    url(r'^employment-opportunities-retailer/', include('employment_opportunities.urls', namespace='employment_opportunities')),
    url(r'^contact/', include('contacts.urls', namespace='contacts')),

    url(r'^thank-you/$', contact_views.ThanksView.as_view(), name='thanks'),

    url(r'^get_in_touch/', include('get_in_touch.urls', namespace='get_in_touch')),

    url(r'^(?P<slug>{})/$'.format(ALIAS_REGEXP), root_router, name='root_router'),
]


if settings.DEBUG:
    urlpatterns += [
        # Для доступа к MEDIA-файлам при разработке
        url(
            r'^media/(?P<path>.*)$',
            'django.views.static.serve',
            kwargs={'document_root': settings.MEDIA_ROOT}
        ),
        url(
            r'^static/(?P<path>.*)$',
            'django.views.static.serve',
            kwargs={'document_root': settings.STATIC_ROOT}
        ),
    ]
