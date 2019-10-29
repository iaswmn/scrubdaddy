from django.db import models
from django.shortcuts import resolve_url
from django.utils.timezone import now
from django.utils.translation import ugettext_lazy as _, ugettext
from solo.models import SingletonModel

from libs.file_field.fields import FileField
from std_page.models import StdPage


class EmploymentOpportunitiesConfig(StdPage, SingletonModel):

    class Meta(StdPage.Meta):
        pass

    def get_absolute_url(self):
        return resolve_url('employment_opportunities:index')

    def __str__(self):
        return ugettext('Employment Opportunities Retailer')


class EmploymentOpportunitiesMessage(models.Model):
    EDUCATION_LEVEL = (
        ('Hight School', 'Hight School'),
        ('Associate Degree', 'Associate Degree'),
        ('Bachelor\'s Degree', 'Bachelor\'s Degree'),
        ('Some College', 'Some College'),
    )

    first_name = models.CharField(
        verbose_name=_('name'),
        max_length=128,
        help_text='First',
    )
    last_name = models.CharField(
        verbose_name=_('last name'),
        max_length=128,
        help_text='Last',
    )
    street_address = models.CharField(
        verbose_name=_('address'),
        max_length=128,
        help_text='Street Address',
    )
    street_address_2 = models.CharField(
        verbose_name=_('street address 2'),
        max_length=128,
        help_text='Street Address 2',
    )
    city = models.CharField(
        verbose_name=_('city'),
        max_length=128,
        help_text='City',
    )
    state = models.CharField(
        verbose_name=_('state'),
        max_length=128,
        help_text='State / Province / Region',
    )
    zip_code = models.CharField(
        verbose_name=_('zip'),
        max_length=128,
        help_text='Zip Code',
    )
    phone = models.CharField(
        verbose_name=_('phone'),
        max_length=32,
    )
    date_available = models.DateTimeField(
        verbose_name=_('date available'),
    )
    desired_salary = models.CharField(
        verbose_name=_('desired salary'),
        max_length=128,
    )
    email = models.EmailField(
        verbose_name=_('email'),
    )
    position = models.CharField(
        verbose_name=_('position applied for'),
        max_length=128,
    )
    about = models.TextField(
        verbose_name=_("tell us about yourself and why you'd be a great fit  for Scrub Daddy"),
    )
    citizen = models.BooleanField(
        verbose_name=_('are you a citizen of the United States?'),
        default=False,
    )
    worked = models.BooleanField(
        verbose_name=_('have you ever worked for this company?'),
        default=False,
    )
    felony = models.BooleanField(
        verbose_name=_('have you ever been convicted of a felony?'),
        default=False,
    )

    education = models.CharField(
        verbose_name=_('education Level'),
        max_length=128,
        choices=EDUCATION_LEVEL,
    )
    school_name = models.CharField(
        verbose_name=_('school name'),
        max_length=128,
    )
    school_street_address = models.CharField(
        verbose_name=_('address'),
        max_length=128,
    )
    school_city = models.CharField(
        verbose_name=_('city'),
        max_length=128,
    )
    school_state = models.CharField(
        verbose_name=_('state'),
        max_length=128,
    )
    school_zip_code = models.CharField(
        verbose_name=_('zip code'),
        max_length=128,
    )
    years_attended = models.CharField(
        verbose_name=_('years attended'),
        max_length=128,
        help_text='What years did you spend working at your previous job? HINT: if you worked between \
                   2010 to 2015, you would enter 2010-2015.'
    )

    company_name = models.CharField(
        verbose_name=_('company name'),
        max_length=128,
    )
    company_phone = models.CharField(
        verbose_name=_('phone'),
        max_length=128,
    )
    company_street_address = models.CharField(
        verbose_name=_('address'),
        max_length=128,
        help_text='Street Address',
    )
    company_street_address_2 = models.CharField(
        verbose_name=_('street address 2'),
        max_length=128,
        help_text='Street Address 2',
    )
    company_city = models.CharField(
        verbose_name=_('city'),
        max_length=128,
        help_text='City',
    )
    company_country = models.CharField(
        verbose_name=_('country'),
        max_length=128,
        help_text='Country',
    )
    company_state = models.CharField(
        verbose_name=_('state'),
        max_length=128,
        help_text='State / Province / Region',
    )
    company_zip_code = models.CharField(
        verbose_name=_('zip'),
        max_length=128,
        help_text='Zip Code',
    )
    supervisor_first_name = models.CharField(
        verbose_name=_('supervisor\'s name'),
        max_length=128,
        help_text='First Name',
    )
    supervisor_last_name = models.CharField(
        verbose_name=_('supervisor name'),
        max_length=128,
        help_text='Last Name',
    )
    job_title = models.CharField(
        verbose_name=_('your job title'),
        max_length=128,
    )
    starting_salary = models.CharField(
        verbose_name=_('starting salary'),
        max_length=128,
    )
    years_worked = models.CharField(
        verbose_name=_('years worked'),
        max_length=128,
        help_text='What years did you spend working at your previous job? HINT: if you worked between \
                   2010 to 2015, you would enter 2010-2015.'
    )
    ending_salary = models.CharField(
        verbose_name=_('ending salary'),
        max_length=128,
    )
    responsibilities = models.TextField(
        verbose_name=_('responsibilities'),
    )
    reason_for_leaving = models.TextField(
        verbose_name=_('reason for leaving'),
    )
    contact_previous_supervisor = models.BooleanField(
        verbose_name=_('may we contact your previous supervisor for a reference?'),
    )

    resume = FileField(
        verbose_name=_('upload resume'),
        upload_to='employment_opportunities/resume',
    )
    user_date = models.DateTimeField(
        verbose_name=_('today\'s date'),
        blank=True,
        null=True,
    )
    date = models.DateTimeField(
        verbose_name=_('date sent'),
        default=now,
        editable=False,
    )

    class Meta:
        default_permissions = ('delete', )
        verbose_name = _('message')
        verbose_name_plural = _('messages')
        ordering = ('-date',)

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)


class EmploymentOpportunitiesSignature(models.Model):
    message = models.ForeignKey(EmploymentOpportunitiesMessage, related_name='signatures')
    file = FileField(
        verbose_name=_('signature'),
        upload_to='employment_opportunities/signatures',
    )

    created = models.DateTimeField(_('created'), default=now, editable=False)

    class Meta:
        ordering = ('-created',)
        default_permissions = ('delete',)
        verbose_name = _('Signature')
        verbose_name_plural = _('Signatures')
