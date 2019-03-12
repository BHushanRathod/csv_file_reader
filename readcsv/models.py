from django.db import models


# Create your models here.
class Employee(models.Model):
    emp_name = models.CharField(max_length=100, null=True)
    type_code = models.CharField(max_length=100, null=True)
    image_url = models.CharField(max_length=200, null=True)
    local_url = models.CharField(max_length=200, null=True)
