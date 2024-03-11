from django.db import models

# Create your models here.


class Customer(models.Model):
  user = models.ForeignKey('accounts.User', on_delete=models.CASCADE)