from django.shortcuts import resolve_url
from django.views.generic import TemplateView
from libs.views import CachedViewMixin
from seo.seo import Seo
from .models import AboutConfig, Event


class IndexView(CachedViewMixin, TemplateView):
    template_name = 'about/index.html'
    config = None

    def last_modified(self, *args, **kwargs):
        self.config = AboutConfig.get_solo()
        return self.config.updated

    def get(self, request, *args, **kwargs):
        seo = Seo()
        seo.set_data(self.config)
        seo.save(request)
        request.breadcrumbs.add(self.config.header, resolve_url('about:index'))

        return self.render_to_response({
            'page_data': self.config,
            'events': Event.objects.all(),
            'is_about_page': True,
        })