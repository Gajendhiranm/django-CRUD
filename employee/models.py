from django.db import models

# Create your models here.

class Employee(models.Model):
    GENDER = [
        ('M','Male'),
        ('F','Female'),
        ('O','Other')
    ]
    first_name = models.CharField(max_length=30,blank=False)
    last_name = models.CharField(max_length=15,default='')
    gender = models.CharField(max_length=1,choices=GENDER)
    # company = models.CharField(max_length=30,default='')
    email = models.EmailField(max_length=50)



