from django import forms
from libs.form_helper.forms import FormHelperMixin
from .models import BusinessAccountMessage


class BusinessAccountForm(FormHelperMixin, forms.ModelForm):
    default_field_template = 'form_helper/field.html'
    render_help_text = True
    signature = forms.CharField(widget=forms.HiddenInput())

    class Meta:
        model = BusinessAccountMessage
        fields = '__all__'
