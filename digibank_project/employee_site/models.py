from django.db import models

# Create your models here.
class Employee(models.Model):

    #Employee Model included by <kashif> to utilize employee details
    firstName = models.CharField(max_length=50)
    middleName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zipCode = models.CharField(max_length=10)
    phoneNumber = models.CharField(max_length=15)
    emailAdd = models.CharField(max_length=70, unique=True)
    userid = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.firstName