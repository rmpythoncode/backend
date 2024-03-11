from rest_framework.exceptions import AuthenticationFailed, APIException
from rest_framework.response import Response
from django.contrib.auth.hashers import check_password, make_password
from accounts.models import User
from vendors.models import Vendor, Employee
from customers.models import Customer



class Authentication:

  def signin(self, email=None, password=None):
    user_exists = User.objects.filter(email=email).exists()

    if not user_exists:
      raise AuthenticationFailed('Email e/ou senha incorretos')

    user = User.objects.filter(email=email).first()

    if not check_password(password, user.password):
      raise AuthenticationFailed('Email e/ou senha incorretos')

    return user

  def signup(self, email, password, role=None, vendor_id=False):
    print(email, password, role, vendor_id)
    if not email or email == '':
      raise APIException('É preciso de um email válido')
    if not password or password == '':
      raise APIException('É preciso de um password válido')

    if role == 'EMPLOYEE' and not vendor_id:
      raise APIException('o colaborador precisa estar vinculado a uma empresa')

    if User.objects.filter(email=email).exists():
      raise APIException('Este email já consta em nossa plataforma')

    password_hashed = make_password(password)

    created_user = User.objects.create(
      email=email,
      password=password_hashed,
      role=role,
    )

    if role == '1':
      created_vendor = Vendor.objects.create(
        name = "Nome da Empresa",
        user_id = created_user.id
      )

    if role == '2':
      Employee.objects.create(
        vendor_id = vendor_id or created_vendor.id,
        user_id = created_user.id
      )

    if role == '3':
      Customer.objects.create(
        user_id = created_user.id
      )


    return created_user


