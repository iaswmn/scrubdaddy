from django.template import Library, loader
from contacts.models import PhoneNumber
from django.conf import settings

register = Library()


@register.simple_tag(takes_context=True)
def header(context, template='header/header.html'):
    """ Шапка """
    request = context.get('request')

    return loader.render_to_string(template, {
        'country': request.META.get('GEOIP_COUNTRY'),
        'is_main_page': context.get('is_main_page'),
        'phone_number': PhoneNumber.objects.first(),
    }, request=context.get('request'))
