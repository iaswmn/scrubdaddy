from django.db import models
from django.shortcuts import get_object_or_404, resolve_url
from django.views.generic import TemplateView
from libs.description import description
from libs.views import CachedViewMixin
from seo.seo import Seo
from social_networks.models import SocialLinks
from .models import BlogConfig, BlogPost, Tag


class IndexView(CachedViewMixin, TemplateView):
    template_name = 'blog/index.html'
    config = None
    posts = None
    tag = None

    def last_modified(self, *args, tag_slug=None, **kwargs):
        self.config = BlogConfig.get_solo()

        if tag_slug:
            self.tag = get_object_or_404(Tag, slug=tag_slug)
            self.posts = BlogPost.objects.filter(visible=True, tags=self.tag)
        else:
            self.posts = BlogPost.objects.filter(visible=True)

        return self.config.updated, self.posts.aggregate(models.Max('updated'))['updated__max']

    def get(self, request, *args, tag_slug=None, **kwargs):
        seo = Seo()
        seo.set_data(self.config)
        seo.save(request)
        request.breadcrumbs.add('Blog', resolve_url('support:blog'))

        return self.render_to_response({
            'page_data': self.config,
            'tags': Tag.objects.active(),
            'current_tag': self.tag,
            'posts': self.posts
        })


class DetailView(CachedViewMixin, TemplateView):
    template_name = 'blog/detail.html'
    config = None
    post = None

    def last_modified(self, *args, slug=None, **kwargs):
        self.config = BlogConfig.get_solo()
        self.post = get_object_or_404(BlogPost, slug=slug)
        return self.config.updated, self.post.updated

    def get(self, request, *args, slug=None, **kwargs):
        seo = Seo()
        seo.set_title(self.config, default=self.config.header)
        seo.set_data(self.post, defaults={
            'title': self.post.header,
            'description': description(self.post.note, 50, 160),
            'og_title': self.post.header,
            'og_image': self.post.preview,
            'og_description': self.post.note,
        })
        seo.save(request)
        request.breadcrumbs.add('Blog', resolve_url('support:blog'))
        request.breadcrumbs.add(self.post.header, self.post.get_absolute_url())

        return self.render_to_response({
            'page_data': self.config,
            'post': self.post,
            'instagram': SocialLinks.get_solo().social_instagram
        })
