from rest_framework import serializers
from .models import Country

class CountrySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Country
        fields = ['id', 'name', 'alpha_2_code', 'alpha_3_code', 'currencies']
        extra_kwargs = {'currencies': {'required': False}}
        depth = 1