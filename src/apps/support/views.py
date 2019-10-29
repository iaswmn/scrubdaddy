from django.shortcuts import resolve_url
from django.views.generic import TemplateView

from blog.models import BlogPost
from libs.views import CachedViewMixin
from media.models import MediaLink
from questions.models import Question
from seo.seo import Seo
from .models import SupportConfig


class IndexView(CachedViewMixin, TemplateView):
    template_name = 'support/index.html'
    config = None

    def last_modified(self, *args, **kwargs):
        self.config = SupportConfig.get_solo()
        return self.config.updated

    def get(self, request, *args, **kwargs):
        seo = Seo()
        seo.set_data(self.config)
        seo.save(request)
        request.breadcrumbs.add('Support & Discover', resolve_url('support:index'))

        return self.render_to_response({
            'country': request.META.get('GEOIP_COUNTRY'),
            'page_data': self.config,
            'posts': BlogPost.objects.filter(visible=True).exists(),
            'blog_posts': BlogPost.objects.filter(visible=True)[0:3],
            'questions': Question.objects.all()[0:3],
            'media_links': MediaLink.objects.all()[0:3],
        })
