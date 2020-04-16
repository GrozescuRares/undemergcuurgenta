from smtplib import SMTPException

from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views.generic import CreateView, DetailView, TemplateView
from django.views.generic.base import ContextMixin
from django_filters.views import FilterView

from app.constants import (
    THANK_YOU_MESSAGE,
    DEFAULT_ORDER_BY,
    SERVICE_UNIT_CREATE_MAIL_SUBJECT,
    SERVICE_UNIT_CREATE_MAIL_MESSAGE,
    MAIL_SENT_TO_SEPARATOR,
    PAGINATION_MAX_PAGES_TO_LEFT,
    PAGINATION_MAX_PAGES_TO_RIGHT,
)
from app.filters import ServiceUnitFilter
from app.helpers import BaseHelper
from app.models import ServiceUnit
from django_project.settings import EMAIL_HOST_USER, PAGINATED_BY, EMAIL_SEND_TO


class ServiceUnitListView(FilterView):
    """
        Renders a list view with all verified MedicalUnits ordered desc by created_at field.
    """
    template_name_suffix = '_list'
    filterset_class = ServiceUnitFilter
    ordering = DEFAULT_ORDER_BY
    queryset = ServiceUnit.objects.filter(verified=True)
    paginate_by = PAGINATED_BY

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ServiceUnitListView, self).get_context_data(**kwargs)
        context.update({
            'unique_locations': BaseHelper.get_unique_count(object_list, 'location', 'name'),
            'unique_categories': BaseHelper.get_unique_count(object_list, 'category', 'name'),
            'max_pages_to_left': PAGINATION_MAX_PAGES_TO_LEFT,
            'max_pages_to_right': PAGINATION_MAX_PAGES_TO_RIGHT,
        })

        return context


class PreviousPageMixin(ContextMixin):
    def get_context_data(self, **kwargs):
        context = super(PreviousPageMixin, self).get_context_data(**kwargs)
        context.update({
            'previous_url': self.request.META.get('HTTP_REFERER', reverse('service-units'))
        })

        return context


class ServiceUnitCreateView(CreateView, PreviousPageMixin):
    model = ServiceUnit
    fields = ['name', 'location', 'address', 'category', 'tags', 'schedule', 'link', 'image']

    def get_success_url(self):
        return reverse('service-units')

    def form_valid(self, form):
        messages.success(self.request, THANK_YOU_MESSAGE.format(form.cleaned_data['name'], form.cleaned_data['location'].name))
        try:
            send_mail(
                SERVICE_UNIT_CREATE_MAIL_SUBJECT,
                SERVICE_UNIT_CREATE_MAIL_MESSAGE.format(form.cleaned_data['name'], form.cleaned_data['location'].name),
                EMAIL_HOST_USER,
                EMAIL_SEND_TO.split(MAIL_SENT_TO_SEPARATOR),
            )
        except SMTPException:
            pass

        return super().form_valid(form)


class ServiceUnitDetailView(DetailView, PreviousPageMixin):
    model = ServiceUnit

    def get_object(self, queryset=None):
        return get_object_or_404(ServiceUnit, pk=self.kwargs['pk'], verified=True)
