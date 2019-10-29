from django.utils.translation import ugettext_lazy as _
from .base import Menu, MenuItem
from config.models import Config
from django.conf import settings


def main(request):
    menu = Menu()
    menu.append(
        MenuItem(
            item_id='products',
            title=_('product family'),
            url='products:index',
        ),
        MenuItem(
            title=_('where to buy'),
            url='where_to_buy:index',
        ),
    )
    country = request.META.get('GEOIP_COUNTRY')
    if country == 'IL':
        menu.append(
            MenuItem(
                title=_('FAQs'),
                url='support:faq',
            )
        )
    else:
        menu.append(
            MenuItem(
                title=_('support & discover'),
                url='support:index',
            )
        )
    menu.append(
        MenuItem(
            title=_('about us'),
            url='about:index',
        ),
        MenuItem(
            title=_('open a business account'),
            url='business_account:index',
        ),
    )

    if country:
        if country != 'CA' and country != 'IL':
            menu.append(
                MenuItem(
                    title=_('smile shop'),
                    url=Config.get_solo().shop_link,
                    attrs={'target': '_blank'}
                ),
            )

    return menu


def footer_menu(request):
    menu = Menu()
    menu.append(
        MenuItem(
            title=_('product family'),
            url='products:index',
        ),
        MenuItem(
            title=_('where to buy'),
            url='where_to_buy:index',
        ),
        MenuItem(
            title=_('support & discover'),
            url='support:index',
        ),
        MenuItem(
            title=_('about us'),
            url='about:index',
        ),
    )

    country = request.META.get('GEOIP_COUNTRY')
    if country:
        if country != 'CA' and country != 'IL':
            menu.append(
                MenuItem(
                    title=_('smile shop'),
                    url=Config.get_solo().shop_link,
                    attrs={'target': '_blank'}
                ),
            )

    menu.append(
        MenuItem(
            title=_('Open A Business Account'),
            url='business_account:index',
        ),
        MenuItem(
            title=_('Employment Opportunities'),
            url='employment_opportunities:index',
        ),
        MenuItem(
            title=_('Get In Touch'),
            url='get_in_touch:index',
        ),
    )

    return menu
