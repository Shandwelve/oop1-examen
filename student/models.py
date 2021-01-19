from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=50)
    discipline = models.CharField(max_length=20)
    mark = models.PositiveIntegerField()
