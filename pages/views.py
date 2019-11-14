from django.shortcuts import render
from django.http import HttpResponse
from seafarers.models import SeafarerCertificate, Seafarer


def index(request):
    number_of_seafarers = Seafarer.objects.count()

    context = {
        'number_of_seafarers': number_of_seafarers
    }
    return render(request, 'pages/index.html', context)
