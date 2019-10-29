from django.shortcuts import resolve_url
from django.views.generic import TemplateView

from blog.models import BlogPost
from libs.views import CachedViewMixin
from seo.seo import Seo
from .models import QuestionsConfig, Question
from products.models import Product


class IndexView(CachedViewMixin, TemplateView):
    template_name = 'questions/index.html'
    config = None

    def last_modified(self, *args, **kwargs):
        self.config = QuestionsConfig.get_solo()
        return self.config.updated

    def get(self, request, *args, **kwargs):
        seo = Seo()
        seo.set_data(self.config)
        seo.save(request)
        request.breadcrumbs.add('FAQs', resolve_url('support:faq'))

        return self.render_to_response({
            'country': request.META.get('GEOIP_COUNTRY'),
            'page_data': self.config,
            'questions': Question.objects.filter(visible=True),
            'posts': BlogPost.objects.filter(visible=True).exists(),
            'products': Product.objects.filter(category__show_on_faq_page=True),
        })
