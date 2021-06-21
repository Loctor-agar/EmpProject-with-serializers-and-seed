from django.db import models

# Create your models here.


class Position(models.Model):
    name = models.CharField(max_length=50)


class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    position = models.ForeignKey(Position, on_delete=models.DO_NOTHING)