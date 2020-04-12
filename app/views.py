from django_filters.views import FilterView

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
