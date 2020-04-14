import os

from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views.generic import CreateView, DetailView
from django_filters.views import FilterView

from app.constants import THANK_YOU_MESSAGE, DEFAULT_ORDER_BY, DEFAULT_PAGINATED_BY
from app.filters import ServiceUnitFilter
from app.helpers import BaseHelper
from app.models import ServiceUnit


class ServiceUnitListView(FilterView):
    """
        Renders a list view with all verified MedicalUnits ordered desc by created_at field.
    """
    template_name_suffix = '_list'
    filterset_class = ServiceUnitFilter
    ordering = DEFAULT_ORDER_BY
    queryset = ServiceUnit.objects.filter(verified=True)
    paginate_by = os.environ.get('PAGINATED_BY') or DEFAULT_PAGINATED_BY

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ServiceUnitListView, self).get_context_data(**kwargs)
        context.update({
            'unique_locations': BaseHelper.get_unique_count(object_list, 'location', 'name'),
            'unique_categories': BaseHelper.get_unique_count(object_list, 'category', 'name'),
        })

        return context


class ServiceUnitCreateView(CreateView):
    model = ServiceUnit
    fields = ['name', 'location', 'address', 'category', 'tags', 'schedule', 'link', 'image']

    def get_success_url(self):
        return reverse('service-units')

    def form_valid(self, form):
        messages.success(self.request, THANK_YOU_MESSAGE.format(form.cleaned_data['name'], form.cleaned_data['location'].name))

        return super().form_valid(form)


class ServiceUnitDetailView(DetailView):
    model = ServiceUnit

    def get_object(self, queryset=None):
        return get_object_or_404(ServiceUnit, pk=self.kwargs['pk'], verified=True)
