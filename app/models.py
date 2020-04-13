import io
from django.core.files.storage import default_storage as storage
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
    location = models.ForeignKey(ServiceUnitLocation, on_delete=models.CASCADE)
    category = models.ForeignKey(ServiceUnitCategory, on_delete=models.CASCADE)
    tags = models.TextField()
    image = models.ImageField(default='default.jpg', upload_to='pictures')
    schedule = models.CharField(max_length=250)
    link = models.URLField(max_length=500)
    verified = models.BooleanField(default=False)

    def __str__(self):
        return f"Medical unit {self.name}: category {self.category.name}; location {self.location.name}; verified {self.verified}."

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img_read = storage.open(self.image.name, 'rb')
        img = Image.open(img_read)

        if img.height > 300 or img.width > 300:
            output_size = (450, 450)
            img.thumbnail(output_size)
            in_mem_file = io.BytesIO()
            img.save(in_mem_file, format='PNG')
            img_write = storage.open(self.image.name, 'w+')
            img_write.write(in_mem_file.getvalue())
            img_write.close()

        img_read.close()
