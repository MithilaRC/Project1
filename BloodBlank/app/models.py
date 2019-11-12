from django.db import models

class AdminLogin(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)

class DonorLogin(models.Model):
    d_uname = models.CharField(max_length=30)
    d_pwd = models.CharField(max_length=30)

class DonorRegDetails(models.Model):
    choices = (("m", "Male"), ("f", "Female"))
    blood = (("a+", "A+"),("a-", "A-"),("b+", "B+"),("b-", "B-"),("o+", "O+"),("o-", "O-"),("ab+", "AB+"),("ab-", "AB-") )
    name = models.CharField(max_length=30)
    gender = models.CharField(max_length=30, choices=choices, default="f")
    email = models.EmailField()
    contact = models.IntegerField()
    bloodgroup = models.CharField(max_length=30, choices=blood, default="a+")
    state = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    age = models.IntegerField()
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    lastdonationdate = models.DateTimeField()
