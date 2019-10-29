import uuid
from base64 import b64decode

from django.core.files.base import ContentFile
from django.shortcuts import redirect
from django.utils.translation import ugettext_lazy as _
from django.views.generic import TemplateView

from contacts.models import NotificationReceiverJobs, NotificationReceiverCanada
from libs.email import send_template
from libs.views import CachedViewMixin
from seo.seo import Seo
from .forms import EmploymentOpportunitiesForm
from .models import EmploymentOpportunitiesConfig, EmploymentOpportunitiesSignature


class IndexView(CachedViewMixin, TemplateView):
    template_name = 'employment_opportunities/index.html'
    config = None

    def last_modified(self, *args, **kwargs):
        self.config = EmploymentOpportunitiesConfig.get_solo()
        return self.config.updated

    def get(self, request, *args, **kwargs):
        form = EmploymentOpportunitiesForm()

        seo = Seo()
        seo.set_data(self.config, defaults={
            'title': self.config.header,
        })
        seo.save(request)

        return self.render_to_response({
            'page_data': self.config,
            'form': form,
        })

    def post(self, request):
        config = EmploymentOpportunitiesConfig.get_solo()
        form = EmploymentOpportunitiesForm(request.POST, request.FILES)
        if form.is_valid():
            message = form.save(commit=False)
            message.save()

            b64_signature = request.POST.get('signature')
            image_data = b64decode(b64_signature)
            message_file = EmploymentOpportunitiesSignature(
                message=message
            )
            message_file.file = ContentFile(image_data, str(uuid.uuid4()) + '.png')
            message_file.save()

            attachments = [
                (message_file.file.name, message_file.file.read(), 'application/octet-stream')
            ]

            receivers = NotificationReceiverJobs.objects.all().values_list('email', flat=True)
            country = request.META.get('GEOIP_COUNTRY')
            if country == 'CA':
                receivers = NotificationReceiverCanada.objects.all().values_list('email', flat=True)
            send_template(
                request,
                receivers,
                subject=_('Message from {domain}'),
                template='employment_opportunities/mails/message.html',
                context={
                    'message': message,
                },
                attachments=attachments,
            )
            return redirect('thanks')
        else:
            return self.render_to_response({
                'page_data': config,
                'form': form,
            })