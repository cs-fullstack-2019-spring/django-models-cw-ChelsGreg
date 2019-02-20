from django.db import models

# Create your models here.

# Dog Class with: name, breed, color, gender
class Dog(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)


# Account Model with: username, realname, accountnumber, balance

class Account(models.Model):
    userName = models.CharField(max_length=20)
    realName = models.CharField(max_length=100)
    accountNumber = models.IntegerField()
    balance = models.DecimalField(decimal_places=10, max_digits=19)


