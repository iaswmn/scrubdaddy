from django.conf.urls import url

from libs.autoslug import ALIAS_REGEXP
from . import views


urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
]
