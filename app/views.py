from django.views.generic import ListView
from django_filters.views import FilterView

from app.filters import MedicalUnitFilter
from app.models import MedicalUnit


class MedicalUnitListView(FilterView):
    """
        Renders a list view with all verified MedicalUnits ordered desc by created_at field.
    """
    filterset_class = MedicalUnitFilter
    ordering = '-created_at'
    queryset = MedicalUnit.objects.filter(verified=True)
    paginate_by = 1
