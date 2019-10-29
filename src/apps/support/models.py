from django.db import models
from django.shortcuts import resolve_url
from django.utils.translation import ugettext_lazy as _, ugettext
from solo.models import SingletonModel

from std_page.models import StdPage


class SupportConfig(StdPage, SingletonModel):

    class Meta(StdPage.Meta):
        pass

    def get_absolute_url(self):
        return resolve_url('support:index')

    def __str__(self):
        return ugettext('Support')
