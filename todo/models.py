from django.db import models

# Create your models here.

class todolist(models.Model):
    title=models.CharField(max_length=250)
    check_status=models.BooleanField(default=False)


class imag(models.Model):
    nameimg=models.CharField(max_length=250)
    type=models.BooleanField()
    date=models.DateTimeField()
   