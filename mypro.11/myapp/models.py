from __future__ import unicode_literals
from django.db import models

class Student(models.Model):
    name=models.CharField(max_length=26,unique=True,default='raghavendra')
    phone = models.IntegerField(default='91')
    mail = models.EmailField(max_length=254,default='raghav.shetty100@gmail.com')
    message=models.CharField(max_length=26,unique=True,default='hi')

    class Meta:
        db_table = "Student"
