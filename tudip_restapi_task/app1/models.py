from django.db import models

# Create your models here.
class Candidate(models.Model):
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    phone = models.CharField(max_length=10)
    address = models.CharField(max_length=100)