from django.db import models
from enum import Enum

# Create your models here.
class SoftDeleteManager(models.Manager):

    def get_queryset(self):
        return super().get_queryset().filter(is_deleted=False)


class SoftDeleteModel(models.Model):
    
    is_deleted = models.BooleanField(default=False)
    objects = SoftDeleteManager()
    all_objects = models.Manager()

    def soft_delete(self):
        self.is_deleted = True
        self.save()

    def restore(self):
        self.is_deleted = False
        self.save()

    class Meta:
        abstract = True


class Currency(SoftDeleteModel):
    title = models.CharField(max_length=100);
    short_code = models.CharField(max_length=3);

    def __str__(self) -> str:
        return f"{self.title}"

    class Meta:
        verbose_name_plural = 'Currencies'


class Country(SoftDeleteModel):
    name = models.CharField(max_length=100)
    alpha_2_code = models.CharField(max_length=2)
    alpha_3_code = models.CharField(max_length=3)
    currencies = models.ManyToManyField('Currency', related_name='currencies', blank=True)

    def __str__(self) -> str:
        return f"{self.name}"

    class Meta:
        verbose_name_plural = 'Countries'


# class Currency(Enum):
#     USD = 'USD' #U.S. Dollar (USD)  
#     EUR = 'EUR' #European Euro (EUR)
#     JPY = 'JPY' #Japanese Yen (JPY)
#     GBP = 'GBP' #British Pound (GBP)
#     CHF = 'CHF' #Swiss Franc (CHF)
#     CAD = 'CAD' #Canadian Dollar (CAD)
#     AUD = 'AUD' #Australian (AUD)
#     NZD = 'NZD' #New Zealand Dollar (NZD)
#     ZAR = 'ZAR' #South African Rand (ZAR)

