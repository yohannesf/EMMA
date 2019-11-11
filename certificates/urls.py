from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='certificates'),
    path('<int:certificate_id>', views.certificate, name='certificate'),
    path('search', views.search, name='search'),
]
