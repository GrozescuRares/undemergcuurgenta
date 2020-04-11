from django.db import models
from django.utils import timezone


class BaseModel(models.Model):
    class Meta:
        abstract = True

    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name


class MedicalUnitLocation(BaseModel):
    pass


class MedicalUnitCategory(BaseModel):
    pass


class MedicalUnit(BaseModel):
    location = models.ForeignKey(MedicalUnitLocation, on_delete=models.CASCADE)
    category = models.ForeignKey(MedicalUnitCategory, on_delete=models.CASCADE)
    schedule = models.CharField(max_length=250)
    link = models.CharField(max_length=100)
    verified = models.BooleanField(default=False)

    def __str__(self):
        return f"Medical unit {self.name}: category {self.category.name}; location {self.location.name}; verified {self.verified}."
