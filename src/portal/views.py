from django.shortcuts import render
from api.models import Country
from django.views.generic import ListView

# Create your views here.

class CountryListView(ListView):

    model = Country
    template_name = 'portal/index.html'
    context_object_name = 'countries'

    


