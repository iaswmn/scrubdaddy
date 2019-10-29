from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class Config(AppConfig):
    name = 'business_account'
    verbose_name = _('Open a business account')

