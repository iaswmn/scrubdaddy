from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class Config(AppConfig):
    name = 'employment_opportunities'
    verbose_name = _('Employment Opportunities')
