from django.contrib import admin

from app.models import ServiceUnitLocation, ServiceUnitCategory, ServiceUnit


admin.site.register(ServiceUnitLocation)
admin.site.register(ServiceUnitCategory)
admin.site.register(ServiceUnit)
