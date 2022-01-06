from django.urls import path
from django.urls.conf import include
from rest_framework import urlpatterns
from rest_framework.routers import DefaultRouter
from .views import CountryViewSet

router = DefaultRouter()
router.register('countries', CountryViewSet, basename='countries')

urlpatterns = [
    path('', include(router.urls)),
]

