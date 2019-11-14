from django.shortcuts import get_object_or_404, render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator


from seafarers.models import Seafarer
from seafarers.models import SeafarerCertificate


def search(request):

    queryset_list = SeafarerCertificate.objects.order_by('-date_created')

    # Full Name
    if 'full_name' in request.GET:
        full_name = request.GET['full_name']
        if full_name:
            queryset_list = queryset_list.filter(
                seafarer_name__name__icontains=full_name)

    if 'date_of_birth' in request.GET:
        date_of_birth = request.GET['date_of_birth']
        if date_of_birth:
            # queryset_list = queryset_list.pub_date__date__gt = datetime.date(
            #     2005, 1, 1)
            queryset_list = queryset_list.filter(
                seafarer_name__birth_date__contains=date_of_birth)

    if 'certificate_code' in request.GET:
        certificate_code = request.GET['certificate_code']
        if certificate_code:
            queryset_list = queryset_list.filter(
                certificate_code__iexact=certificate_code)

    context = {
        'SeafarerCertificates': queryset_list,

    }

    return render(request, 'seafarers/search.html', context)
