import os

from django.core.files.images import ImageFile
from django.shortcuts import redirect
from django.utils.html import escape
from django.utils.translation import ugettext_lazy as _
from django.views.generic import TemplateView

from contacts.models import NotificationReceiver, NotificationReceiverCanada
from libs.email import send_template
from libs.views import CachedViewMixin
from seo.seo import Seo
from .forms import GetInTouchForm
from .models import GetInTouchConfig, GetInTouchMessageImage


class IndexView(CachedViewMixin, TemplateView):
    template_name = 'get_in_touch/index.html'
    config = None

    def last_modified(self, *args, **kwargs):
        self.config = GetInTouchConfig.get_solo()
        return self.config.updated

    def get(self, request, *args, **kwargs):
        form = GetInTouchForm()

        seo = Seo()
        seo.set_data(self.config, defaults={
            'title': self.config.header,
        })
        seo.save(request)

        return self.render_to_response({
            'country': request.META.get('GEOIP_COUNTRY'),
            'page_data': self.config,
            'form': form,
        })

    def post(self, request):
        config = GetInTouchConfig.get_solo()
        form = GetInTouchForm(request.POST, request.FILES)
        if form.is_valid():
            message = form.save(commit=False)
            referer = request.POST.get('referer')
            message.referer = escape(referer)
            country = request.META.get('GEOIP_COUNTRY')
            message.country = country
            message.save()

            file_names = request.POST.getlist('images[][name]')
            file_filenames = request.POST.getlist('images[][file]')
            for name, filepath in zip(file_names, file_filenames):
                if os.path.exists(filepath):
                    message_file = GetInTouchMessageImage(
                        message=message
                    )
                    message_file.save()

                    with open(filepath, 'rb', encoding="utf8") as fp:
                        message_file.file.save(name, ImageFile(fp))

                    os.unlink(filepath)

            attachments = [
                (message_file.file.name, message_file.file.read(), 'application/octet-stream')
                for message_file in message.images.all()
            ]

            receivers = NotificationReceiver.objects.all().values_list('email', flat=True)
            country = request.META.get('GEOIP_COUNTRY')
            if country == 'CA':
                receivers = NotificationReceiverCanada.objects.all().values_list('email', flat=True)
            if country == 'IL':
                receivers = 'israel@scrubdaddy.com'
            send_template(
                request,
                receivers,
                from_email=message.email,
                subject=_('Message from {domain}'),
                template='get_in_touch/mails/message.html',
                context={
                    'message': message,
                },
                attachments=attachments,
                fail_silently=True,
            )
            return redirect('thanks')
        else:
            return self.render_to_response({
                'page_data': config,
                'form': form,
            })
