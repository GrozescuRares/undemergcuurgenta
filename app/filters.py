from django_filters import FilterSet, CharFilter

from app.models import ServiceUnit


class ServiceUnitFilter(FilterSet):
    class Meta:
        model = ServiceUnit
        fields = {
            'category': ['exact'],
            'location': ['exact'],
            'tags': ['contains'],
        }

    def __init__(self, *args, **kwargs):
        super(ServiceUnitFilter, self).__init__(*args, **kwargs)
        self.filters['category'].label = "Categorie"
        self.filters['category'].label = "Categorie"
        self.filters['location'].label = "Locatie"
        self.filters['tags__contains'].label = "Servicii/Produse cautate"
