from django.db import models

# Create your models here.
class UserDetails(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/')

    # def __str__(self):
    #     return self.name

class UserMoreDetails(models.Model):
    user = models.OneToOneField(UserDetails, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15)
    address = models.CharField(max_length=100)
    date_of_birth = models.DateField()


class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)