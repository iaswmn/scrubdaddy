from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class Config(AppConfig):
    name = 'libs.ipinfo'
    verbose_name = _('IpInfo')
