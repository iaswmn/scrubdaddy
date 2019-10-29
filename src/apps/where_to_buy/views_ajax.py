from django.utils.html import escape
from django.utils.translation import ugettext_lazy as _
from django.views.generic.base import View
from libs.views_ajax import AjaxViewMixin


class ShopView(AjaxViewMixin, View):
    def get(self, request):
        return self.json_response({
            'form': self.render_to_string('where_to_buy/popups/shop_online.html', {
                # 'config': config,
                # 'form': form,
            }),
        })

    # def post(self, request):
    #     config = ContactsConfig.get_solo()
    #     form = ContactForm(request.POST, request.FILES)
    #     if form.is_valid():
    #         message = form.save(commit=False)
    #         referer = request.POST.get('referer')
    #         message.referer = escape(referer)
    #         message.save()

    #         receivers = NotificationReceiver.objects.all().values_list('email', flat=True)
    #         send_template(request, receivers,
    #             subject=_('Message from {domain}'),
    #             template='contacts/mails/message.html',
    #             context={
    #                 'message': message,
    #             }
    #         )

    #         return self.json_response({
    #             'success_message': self.render_to_string('contacts/popups/contact_success.html', {
    #                 'config': config,
    #             })
    #         })
    #     else:
    #         return self.json_error({
    #             'errors': form.error_dict_full,
    #             'form': self.render_to_string('contacts/popups/contact_form.html', {
    #                 'config': config,
    #                 'form': form,
    #             }),
    #         })
