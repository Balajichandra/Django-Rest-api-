from django.db import models

# Create your models here.
class Book(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=128)
    author = models.CharField(max_length=64)