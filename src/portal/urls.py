from django.urls import path
from .views import CountryListView

app_name='portal'

urlpatterns = [
    path('', CountryListView.as_view(), name='list')
]
