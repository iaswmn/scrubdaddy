from django.conf.urls import urlfrom . import views, views_ajaxurlpatterns = [    url(r'^upload/$', views_ajax.UploadView.as_view(), name='upload'),    url(r'^$', views.IndexView.as_view(), name='index'),]