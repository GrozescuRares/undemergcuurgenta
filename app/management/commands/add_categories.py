from django.core.management.base import BaseCommand, CommandError

from app.constants import CATEGORIES
from app.models import ServiceUnitCategory


class Command(BaseCommand):
    help = 'Populate ServiceCategory table'

    def handle(self, *args, **options):
        for category_name in CATEGORIES:
            service_category_unit = ServiceUnitCategory(name=category_name)
            service_category_unit.save()

        self.stdout.write(self.style.SUCCESS('Successfully added categories'))
