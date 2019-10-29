from django.shortcuts import resolve_url
from django.views.generic import TemplateView

from blog.models import BlogPost
from libs.views import CachedViewMixin
from seo.seo import Seo
from .models import MediaConfig, MediaLink


class IndexView(CachedViewMixin, TemplateView):
    template_name = 'media/index.html'
    config = None

    def last_modified(self, *args, **kwargs):
        self.config = MediaConfig.get_solo()
        return self.config.updated

    def get(self, request, *args, **kwargs):
        seo = Seo()
        seo.set_data(self.config)
        seo.save(request)
        request.breadcrumbs.add('Media', resolve_url('support:media'))

        return self.render_to_response({
            'page_data': self.config,
            'links': MediaLink.objects.all(),
            'posts': BlogPost.objects.filter(visible=True).exists(),
        })