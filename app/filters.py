from django_filters import FilterSet

from app.models import MedicalUnit


class MedicalUnitFilter(FilterSet):
    class Meta:
        model = MedicalUnit
        fields = ['category', 'location']
