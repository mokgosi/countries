from django.contrib import admin
from django.db import models
from .models import Country 

# Register your models here.
#admin.site.register(Country)

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_filter = ('name', 'alpha_2_code', 'alpha_3_code')