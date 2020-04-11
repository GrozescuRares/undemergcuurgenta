from django.contrib import admin

from app.models import MedicalUnitLocation, MedicalUnitCategory, MedicalUnit


admin.site.register(MedicalUnitLocation)
admin.site.register(MedicalUnitCategory)
admin.site.register(MedicalUnit)
