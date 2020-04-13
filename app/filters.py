from django_filters import FilterSet, CharFilter

from app.models import ServiceUnit


class ServiceUnitFilter(FilterSet):
    class Meta:
        model = ServiceUnit
        fields = {
            'category': ['exact'],
            'location': ['exact'],
        }
