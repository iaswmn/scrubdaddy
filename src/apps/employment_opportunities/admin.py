from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from solo.admin import SingletonModelAdmin

from project.admin import ModelAdminInlineMixin
from project.admin import ModelAdminMixin
from std_page.admin import StdPageAdmin
from .models import EmploymentOpportunitiesConfig, EmploymentOpportunitiesMessage, EmploymentOpportunitiesSignature


@admin.register(EmploymentOpportunitiesConfig)
class SupportConfigAdmin(StdPageAdmin, SingletonModelAdmin):
    fieldsets = StdPageAdmin.fieldsets + (
        (None, {
            'classes': ('suit-tab', 'suit-tab-general'),
            'fields': (
            ),
        }),
    )


class EmploymentOpportunitiesSignatureInline(ModelAdminInlineMixin, admin.TabularInline):
    model = EmploymentOpportunitiesSignature
    extra = 0
    suit_classes = 'suit-tab suit-tab-general'
    readonly_fields = (
        'file',
    )

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(EmploymentOpportunitiesMessage)
class BusinessAccountMessageAdmin(ModelAdminMixin, admin.ModelAdmin):
    fieldsets = (
        (None, {
            'classes': ('suit-tab', 'suit-tab-general'),
            'fields': (
                'first_name', 'last_name', 'street_address', 'street_address_2', 'city',
                'state', 'zip_code', 'phone', 'date_available', 'desired_salary',
                'email', 'position', 'about', 'citizen', 'worked', 'felony',
            ),
        }),
        ('Education', {
            'classes': ('suit-tab', 'suit-tab-general'),
            'fields': (
                'education', 'school_name', 'school_street_address', 'school_city',
                'school_state', 'school_zip_code', 'years_attended',
            ),
        }),
        ('Previous Employment', {
            'classes': ('suit-tab', 'suit-tab-general'),
            'fields': (
                'company_name', 'company_phone', 'company_street_address', 'company_street_address_2',
                'company_city', 'company_state', 'company_zip_code', 'company_country',
                'supervisor_first_name', 'supervisor_last_name', 'job_title',
                'starting_salary', 'years_worked', 'ending_salary', 'responsibilities',
                'reason_for_leaving', 'contact_previous_supervisor', 'resume', 'user_date',
            ),
        }),
    )
    readonly_fields = (
        'first_name', 'last_name', 'street_address', 'street_address_2', 'city',
        'state', 'zip_code', 'phone', 'date_available', 'desired_salary',
        'email', 'position', 'about', 'citizen', 'worked', 'felony',
        'education', 'school_name', 'school_street_address', 'school_city',
        'school_state', 'school_zip_code', 'years_attended',
        'company_name', 'company_phone', 'company_street_address',
        'company_street_address_2', 'company_city', 'company_state', 'company_country', 'company_zip_code',
        'supervisor_first_name', 'supervisor_last_name', 'job_title',
        'starting_salary', 'years_worked', 'ending_salary', 'responsibilities',
        'reason_for_leaving', 'contact_previous_supervisor', 'resume', 'user_date',
    )
    inlines = (
        EmploymentOpportunitiesSignatureInline,
    )
    suit_form_tabs = (
        ('general', _('General')),
    )
