from django.db import models

# Create your models here.
class Trainee(models.Model):
    Name = models.CharField(max_length=20, blank=False)
    Age = models.IntegerField(blank=False)