from django.db import models
from django.shortcuts import redirect
from django.template import loader
from django.utils.html import escape
from django.utils.translation import ugettext_lazy as _
from django.views.generic import TemplateView

from libs.email import send_template
from libs.views import CachedViewMixin
from seo.seo import Seo
from .forms import ContactForm
from .models import ContactsConfig, Address, NotificationReceiver, PhoneNumber


class IndexView(CachedViewMixin, TemplateView):
    template_name = 'contacts/index.html'
    config = None
    addresses = None

    def last_modified(self, *args, **kwargs):
        self.config = ContactsConfig.get_solo()
        self.addresses = Address.objects.all()
        return self.config.updated, self.addresses.aggregate(models.Max('updated'))['updated__max']

    def get(self, request, *args, **kwargs):
        form = ContactForm()

        # SEO
        seo = Seo()
        seo.set_data(self.config, defaults={
            'title': self.config.header,
        })
        seo.save(request)

        return self.render_to_response({
            'config': self.config,
            'addresses': self.addresses,
            'form': form,
        })

    def post(self, request):
        config = ContactsConfig.get_solo()
        form = ContactForm(request.POST, request.FILES)
        if form.is_valid():
            message = form.save(commit=False)
            referer = request.POST.get('referer', request.build_absolute_uri(request.path_info))
            message.referer = escape(referer)
            message.save()

            receivers = NotificationReceiver.objects.all().values_list('email', flat=True)
            send_template(request, receivers,
                          subject=_('Message from {domain}'),
                          from_email=message.email,
                          template='contacts/mails/message.html',
                          context={
                              'message': message,
                          }
            )

            return redirect('contacts:index')
        else:
            return self.render_to_response({
                'config': config,
                'addresses': Address.objects.all(),
                'form': form,
            })


class ThanksView(CachedViewMixin, TemplateView):
    template_name = 'thank_you.html'

    def get(self, request, *args, **kwargs):

        return self.render_to_response({
            'title': 'Thank you'
        })


def contact_block_render(context, block, **kwargs):
    """ Рендеринг подключаемого блока контактов """
    request = context.get('request')
    return loader.render_to_string('contacts/block.html', {
        'country': request.META.get('GEOIP_COUNTRY'),
        'block': block,
        'form': ContactForm(),
        'phone_number': PhoneNumber.objects.first(),
    }, request=request)
