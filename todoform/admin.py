from django.contrib import admin
from .models import ModelForm


@admin.register(ModelForm)
class ModelFormAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'date', 'text') 
    empty_value_display = '-пусто-'
