from rest_framework import viewsets
from .serializers import CountrySerializer
from .models import Country


# Create your views here.

class CountryViewSet(viewsets.ModelViewSet):

    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    filterset_fields = ['alpha_2_code', 'alpha_3_code']

