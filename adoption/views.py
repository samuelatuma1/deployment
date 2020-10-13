from django.shortcuts import render
from django.views.generic import ListView
from . import models

# Create your views here.

class IndexView(ListView):
    context_object_name = 'pets'
    def get_queryset(self):
        return models.Pet.objects.all()

