from django.db import models

# Create your models here.
class Shelter(models.Model):
    name = models.CharField(max_length=50, blank=False)
    address = models.TextField(max_length=1000, blank=False)


class Breed(models.Model):
    name = models.CharField(max_length=50, blank=False)
    description = models.TextField(max_length=1000, blank=False)


class Pet(models.Model):
    name = models.CharField(max_length=50, blank=False)
    breed = models.ManyToManyField(Breed, related_name='pets')
    shelter = models.ForeignKey(Shelter, on_delete=models.PROTECT, related_name='shelteredpets')
