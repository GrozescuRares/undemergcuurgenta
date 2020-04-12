from django.db import models
from django.utils import timezone
from PIL import Image


class BaseModel(models.Model):
    class Meta:
        abstract = True

    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name


class ServiceUnitLocation(BaseModel):
    pass


class ServiceUnitCategory(BaseModel):
    pass


class ServiceUnit(BaseModel):
    location = models.ForeignKey(ServiceUnitLocation, on_delete=models.CASCADE, verbose_name='Locatie')
    category = models.ForeignKey(ServiceUnitCategory, on_delete=models.CASCADE, verbose_name='Categoria')
    tags = models.TextField(verbose_name='Ce se gaseste acolo')
    image = models.ImageField(default='default.jpg', upload_to='pictures')
    schedule = models.CharField(max_length=250, verbose_name='Program de functionare')
    link = models.URLField(max_length=100)
    verified = models.BooleanField(default=False)

    def __str__(self):
        return f"Medical unit {self.name}: category {self.category.name}; location {self.location.name}; verified {self.verified}."
