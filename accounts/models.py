from django.db import models
from django.contrib.auth.models import AbstractBaseUser, Permission
from vendors.models import Vendor

# Create your models here.


class User(AbstractBaseUser):
  VENDOR = 1
  EMPLOYEE = 2
  CUSTOMER = 3


  ROLE_CHOICE = (
    (VENDOR, 'Vendedor'),
    (EMPLOYEE, 'Colaborador'),
    (CUSTOMER, 'Cliente'),
  )

  email = models.EmailField(unique=True)
  role = models.PositiveSmallIntegerField(choices=ROLE_CHOICE, blank=True, null=True,
                                           verbose_name='Tipo')


  USERNAME_FIELD = 'email'


  def __str__(self):
    return self.email


class Group(models.Model):
  name = models.CharField(max_length=200)
  vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)



class GroupPermissions(models.Model):
  group = models.ForeignKey(Group, on_delete=models.CASCADE)
  permission = models.ForeignKey(Permission, on_delete=models.CASCADE)


class UserGroups(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  group = models.ForeignKey(Group, on_delete=models.CASCADE)
