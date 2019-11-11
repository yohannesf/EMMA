from django.db import models

# Create your models here.

from datetime import datetime


class Certificate(models.Model):
    certificate_name = models.CharField(max_length=200)
    certificate_sample = models.ImageField(
        upload_to='photos/%Y/%m/%d/', blank=True)
    description = models.TextField(blank=True)
    created_date = models.DateTimeField(
        default=datetime.now, blank=True)  # databse registreation date

    def __str__(self):
        return self.certificate_name
