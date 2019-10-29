from django import forms

from libs.form_helper.forms import FormHelperMixin
from .models import GetInTouchMessage


class GetInTouchForm(FormHelperMixin, forms.ModelForm):
    default_field_template = 'form_helper/field.html'
    render_help_text = True

    class Meta:
        model = GetInTouchMessage
        fields = '__all__'
        widgets = {
            'comments': forms.Textarea(attrs={
                'rows': 5,
            }),
            'location': forms.HiddenInput()
        }

    def __init__(self, *args, **kwargs):
        super(GetInTouchForm, self).__init__(*args, **kwargs)
        self.fields['reach_time'].choices = GetInTouchMessage.BEST_TIME
        self.fields['time_zone'].choices = GetInTouchMessage.TIME_ZONE

    def clean(self):
        if 'reach_type' in self.cleaned_data and self.cleaned_data.get('reach_type') == 'Email':
            self.cleaned_data['phone'] = ''
            self.cleaned_data['reach_time'] = ''
            self.cleaned_data['time_zone'] = ''

        if 'reach_type' in self.cleaned_data and self.cleaned_data.get('reach_type') == 'Phone':
            if not self.cleaned_data.get('phone'):
                self.add_field_error('phone', 'required')

            if not self.cleaned_data.get('reach_time'):
                self.add_field_error('reach_time', 'required')

            if not self.cleaned_data.get('time_zone'):
                self.add_field_error('time_zone', 'required')

        return super().clean()