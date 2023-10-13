import django_filters
from .models import Booking

class ProductFilter(django_filters.FilterSet):
    class Meta:
        model = Booking
        fields = ['reservation_date']
