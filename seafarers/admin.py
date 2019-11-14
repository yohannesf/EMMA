from django.contrib import admin

from .models import Seafarer, SeafarerCertificate


class SeafarerAdmin(admin.ModelAdmin):
    list_display = ('name', 'gender', 'phone', 'birth_date', 'nationality')


class SeafarerCertificateAdmin(admin.ModelAdmin):

    list_display = ('seafarer_name', 'certificate_type', 'certificate_code', 'certificate_status', 'date_of_issue',
                    'date_of_expiry', 'name_issuing_institute', 'name_issuing_country', 'certificate_barcode', 'certificate_scanned_copy')


admin.site.register(Seafarer, SeafarerAdmin)
admin.site.register(SeafarerCertificate, SeafarerCertificateAdmin)
