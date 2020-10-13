from django.contrib import admin
from .models import Shelter, Pet
from . import models

# Register your models here.
admin.site.register(models.Breed)
admin.site.register(Shelter)
admin.site.register(Pet) 