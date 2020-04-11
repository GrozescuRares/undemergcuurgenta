from django_filters.views import FilterView

from app.filters import MedicalUnitFilter
from app.models import MedicalUnit


class MedicalUnitListView(FilterView):
    """
        Renders a list view with all verified MedicalUnits ordered desc by created_at field.
    """
    template_name = 'medical'
    template_name_suffix = '_list'
    filterset_class = MedicalUnitFilter
    ordering = '-created_at'
    queryset = MedicalUnit.objects.filter(verified=True)
