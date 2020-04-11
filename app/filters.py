from django_filters import FilterSet, CharFilter

from app.models import MedicalUnit


class MedicalUnitFilter(FilterSet):
    class Meta:
        model = MedicalUnit
        fields = ['category', 'location']
