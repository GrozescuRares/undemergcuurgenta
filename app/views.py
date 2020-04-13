from django.contrib import messages
from django.urls import reverse
from django.views.generic import CreateView
from django_filters.views import FilterView

from app.constants import THANK_YOU_MESSAGE
from app.filters import ServiceUnitFilter
from app.models import ServiceUnit


class ServiceUnitListView(FilterView):
    """
        Renders a list view with all verified MedicalUnits ordered desc by created_at field.
    """
    template_name_suffix = '_list'
    filterset_class = ServiceUnitFilter
    ordering = '-created_at'
    queryset = ServiceUnit.objects.filter(verified=True)


class ServiceUnitCreateView(CreateView):
    model = ServiceUnit
    fields = ['name', 'location', 'category', 'tags', 'schedule', 'link']

    def get_success_url(self):
        return reverse('service-units')

    def form_valid(self, form):
        messages.success(self.request, THANK_YOU_MESSAGE.format(form.cleaned_data['name'], form.cleaned_data['location'].name))

        return super().form_valid(form)
