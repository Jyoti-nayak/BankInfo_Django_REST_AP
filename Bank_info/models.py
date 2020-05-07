from django.db import models

# Create your models here.

class Bank_info(models.Model):
    address = models.CharField(max_length=200)
    bank_name = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    ifsc = models.CharField(max_length=50)
    office = models.CharField(max_length=50)


    def __str__(self):
        return f"{self.bank_name} - {self.ifsc}"






