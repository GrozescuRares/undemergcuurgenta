from django.core.management.base import BaseCommand, CommandError

from app.constants import LOCATIONS
from app.models import ServiceUnitLocation


class Command(BaseCommand):
    help = 'Populate ServiceLocation table'

    def handle(self, *args, **options):
        for location_name in LOCATIONS:
            service_location_unit = ServiceUnitLocation(name=location_name)
            service_location_unit.save()

        self.stdout.write(self.style.SUCCESS('Successfully added locations'))
