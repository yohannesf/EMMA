from django.db import models
from datetime import datetime
from django.utils import timezone
from certificates.models import Certificate
from EMMA_aut import barcode_scanner
from django.db.models.signals import post_save
from django.dispatch import receiver
from .choices import countries, certificate_status


class Seafarer(models.Model):

    name = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    phone = models.CharField(max_length=20, blank=True)
    email = models.CharField(max_length=50, blank=True)
    birth_date = models.DateField()
    gender = models.CharField(max_length=6)
    nationality = models.CharField(max_length=50, choices=countries)
    created_date = models.DateTimeField(
        default=timezone.now, blank=True)  # databse registreation date

    def __str__(self):
        return self.name


class SeafarerCertificate(models.Model):
    certificate_code = models.CharField(max_length=50)
    certificate_barcode = models.CharField(
        max_length=100, blank=True, null=True)
    seafarer_name = models.ForeignKey(Seafarer, on_delete=models.CASCADE)
    certificate_type = models.ForeignKey(
        Certificate, on_delete=models.CASCADE)
    date_of_issue = models.DateField(default=timezone.now)
    date_of_expiry = models.DateField(default=timezone.now)
    name_issuing_institute = models.CharField(max_length=100)
    name_issuing_country = models.CharField(max_length=100)
    date_of_last_revalidation = models.DateField(default=timezone.now)
    dispensation_details = models.TextField()

    # Valid, Suspended, Cancelled, Reported lost, Destroyed
    certificate_status = models.CharField(
        max_length=10, choices=certificate_status)

    certificate_scanned_copy = models.ImageField(
        upload_to='photos/%Y/%m/%d/', blank=True)
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.certificate_code


@receiver(post_save, sender=SeafarerCertificate)
def import_barcode(sender, instance, **kwargs):

    if instance.certificate_scanned_copy:

        instance.certificate_barcode = barcode_scanner.Get_barcode(
            instance.certificate_scanned_copy.path)

        post_save.disconnect(import_barcode, sender=SeafarerCertificate)
        instance.save()
        post_save.connect(import_barcode, sender=SeafarerCertificate)
