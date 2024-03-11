from django.db import models

# Create your models here.



class Vendor(models.Model):
  name = models.CharField(max_length=200)
  user = models.ForeignKey('accounts.User', on_delete=models.CASCADE)


class Employee(models.Model):
  user = models.ForeignKey('accounts.User', on_delete=models.CASCADE)
  vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
