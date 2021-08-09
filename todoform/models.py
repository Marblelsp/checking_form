from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class ModelForm(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(blank=True)
    phone = PhoneNumberField(region="RU", blank=True)
    date = models.DateField(null=True, blank=True)
    text = models.TextField(blank=True)

    def __str__(self):
        return self.name
