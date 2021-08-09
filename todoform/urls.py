from django.urls import path

from . import views

urlpatterns = [
    path('get_form/', views.index, name='index'),
]
