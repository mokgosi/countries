from django.db import models
from enum import Enum
from django.utils import timezone

# https://dev.to/bikramjeetsingh/soft-deletes-in-django-a9j
# https://medium.com/hackernoon/using-enum-as-model-field-choice-in-django-92d8b97aaa63

# Create your models here.
class SoftDeleteManager(models.Manager):

    def get_queryset(self):
        return super().get_queryset().filter(is_deleted=False)


class SoftDeleteModel(models.Model):
    
    is_deleted = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(null=True, default=None)
    objects = SoftDeleteManager()
    all_objects = models.Manager()

    def soft_delete(self):
        self.is_deleted = True
        self.deleted_at = timezone.now()
        self.save()

    def restore(self):
        self.is_deleted = False
        self.deleted_at = None
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
    currencies = models.ManyToManyField(Currency, related_name='currencies', blank=True)

    def get_currencies(self):
        return self.currencies.all()

    def __str__(self) -> str:
        return f"{self.name}"

    class Meta:
        verbose_name_plural = 'Countries'




# class LanguageChoice(Enum):   # A subclass of Enum
#     DE = "German"
#     EN = "English"
#     CN = "Chinese"
#     ES = "Spanish"

# class Book(models.Model):
#     title = models.CharField(max_length=255)
#     language = models.CharField(
#       max_length=5,
#       choices=[(tag, tag.value) for tag in LanguageChoice]  # Choices is a list of Tuple
#     )


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

