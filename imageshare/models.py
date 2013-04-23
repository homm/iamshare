from pyuploadcare.dj import ImageField
from django.db import models


class Image(models.Model):
    slug = models.SlugField(max_length=10, primary_key=True, blank=False)
    image = ImageField(manual_crop="")
