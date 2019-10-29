from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class Config(AppConfig):
    name = 'where_to_buy'
    verbose_name = _('Where to buy')