from django.db import models

# Create your models here.

class Appointment(models.Model):
    when = models.DateTimeField(null=False)
    your_name = models.CharField(max_length=100)