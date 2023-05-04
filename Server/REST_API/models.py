from django.db import models

class City(models.Model):
    name = models.TextField(null=True)
    country = models.TextField(null=True)
    square = models.TextField(null=True)

class Religion(models.Model):
    name = models.TextField(null=True)

class Firm(models.Model):
    name = models.TextField(null=True)
    income = models.TextField(null=True)

class Human(models.Model):
    name = models.TextField(null=True)
    age = models.IntegerField(null=True)
    nationality = models.TextField(null=True)
    job = models.ForeignKey(Firm, on_delete=models.SET_NULL, null=True)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True)
    religion = models.ForeignKey(Religion, on_delete=models.SET_NULL, null=True)

