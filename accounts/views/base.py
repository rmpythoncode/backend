from rest_framework.views import APIView
from rest_framework.exceptions import APIException
from accounts.models import UserGroups, GroupPermissions


from vendors.models import Vendor, Employee
from accounts.models import User
from django.shortcuts import get_object_or_404

class Base(APIView):

  def get_vendor_user(self, user_id):
    user = get_object_or_404(User, id=user_id)

    vendor = {
      'role': user.role,
      'permissions': []
    }


    if vendor['role']:
      return vendor


    # permissions

    employee = Employee.objects.filter(user_id=user_id).first()

    if not employee:
      raise APIException('Este usuãrio não é um colaborador')

    groups = UserGroups.objects.filter(user_id=user_id).all()

    for g in groups:
      group = g.group
      permissions = GroupPermissions.objects.filter(group_id=group.id).all()

      for p in permissions:
        vendor['permissions'].append({
          "id": p.permissions.id,
          'label': p.permission.name,
          'codename': p.permission.codename
        })
    return vendor







