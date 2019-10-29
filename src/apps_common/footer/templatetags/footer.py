from django.template import Library, loader
from .. import conf
from contacts.models import Address, PhoneNumber

register = Library()


@register.simple_tag(takes_context=True)
def footer(context, template='footer/footer.html'):
    """ Футер """

    addr = Address.objects.first()
    phone_number = PhoneNumber.objects.first()

    request = context.get('request')

    return loader.render_to_string(template, {
        'country': request.META.get('GEOIP_COUNTRY'),
        'is_main_page': context.get('is_main_page'),
        'addr': addr,
        'phone_number': phone_number,
    }, request=request)


@register.simple_tag(takes_context=True)
def dl_link(context, template='footer/dl_link.html'):
    request = context.get('request')
    if not request:
        return ''

    rule = conf.RULES.get(request.path_info)
    if rule:
        return loader.render_to_string(template, rule, request=request)

    return loader.render_to_string(template, {
        'url': 'https://directlinedev.com/',
        'title': 'Web Development',
        'fallback': True,
    }, request=request)
