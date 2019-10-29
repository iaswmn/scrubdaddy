from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^news/$', views.IndexView.as_view(), name='media'),
]