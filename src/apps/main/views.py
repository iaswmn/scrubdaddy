from django.views.generic import TemplateView
from blog.models import BlogPost
from libs.views import CachedViewMixin
from products.models import ProductCategory
from seo.seo import Seo
from .models import MainPageConfig, MainSlider, Advantage


class IndexView(CachedViewMixin, TemplateView):
    template_name = 'main/index.html'
    config = None

    def last_modified(self, *args, **kwargs):
        self.config = MainPageConfig.get_solo()
        return self.config.updated

    def get(self, request, *args, **kwargs):
        seo = Seo()
        seo.set_data(self.config)
        seo.save(request)

        return self.render_to_response({
            'country': request.META.get('GEOIP_COUNTRY'),
            'config': self.config,
            'slider': MainSlider.objects.all(),
            'blog_posts': BlogPost.objects.filter(visible=True)[:4],
            'product_categories': ProductCategory.objects.all()[:4],
            'advantages': Advantage.objects.all()[:4],
            'is_main_page': True,       # отменяет <noindex> шапки и подвала
        })
