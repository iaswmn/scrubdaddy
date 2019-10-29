from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class Config(AppConfig):
    name = 'libs.geoip2'
    verbose_name = _('geoip2')
