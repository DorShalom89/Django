from django.db import models

# Create your models here.


class Car (models.Model):
    brand = models.CharField(max_length=20)
    color = models.CharField(max_length=10)
    license_number = models.IntegerField(primary_key=True)
    owner = models.ForeignKey('Owner', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'{self.brand}({self.license_number})'


class Owner (models.Model):
    name = models.CharField(max_length=20)
    id = models.IntegerField(primary_key=True)

    def __str__(self):
        return self.name


