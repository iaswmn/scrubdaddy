from django import forms
from django.utils.translation import ugettext_lazy as _
from libs.form_helper.forms import FormHelperMixin
from libs.widgets import PhoneWidget
from .models import EmploymentOpportunitiesMessage


class EmploymentOpportunitiesForm(FormHelperMixin, forms.ModelForm):
    default_field_template = 'form_helper/field.html'
    render_help_text = True
    signature = forms.CharField(widget=forms.HiddenInput())

    class Meta:
        model = EmploymentOpportunitiesMessage
        fields = '__all__'

