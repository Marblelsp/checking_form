from django.db.models.fields import NullBooleanField
from phonenumber_field.modelfields import PhoneNumberField
from django.db import models


class ModelForm(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(blank=True)
    phone = PhoneNumberField(region="RU", blank=True)
    date = models.DateField(null=True, blank=True)
    text = models.TextField(blank=True)

    def __str__(self):
        return self.name
