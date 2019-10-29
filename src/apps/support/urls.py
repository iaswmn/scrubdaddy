from django.conf.urls import url

from libs.autoslug import ALIAS_REGEXP

from media import views as media_views
from blog import views as blog_views
from questions import views as question_views
from . import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),

    url(r'^faq/$', question_views.IndexView.as_view(), name='faq'),

    url(r'^blog/$', blog_views.IndexView.as_view(), name='blog'),
    url(r'^blog/by-tag/(?P<tag_slug>{0})/$'.format(ALIAS_REGEXP), blog_views.IndexView.as_view(), name='blog_tag'),
    url(r'^blog/(?P<slug>{0})/$'.format(ALIAS_REGEXP), blog_views.DetailView.as_view(), name='blog_detail'),

    url(r'^news/$', media_views.IndexView.as_view(), name='media'),
]