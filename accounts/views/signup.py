from accounts.views.base import Base
from accounts.auth import Authentication
from accounts.serializers import UserSerializer
from rest_framework.response import Response

class Signup(Base):
  def post(self, request):
    email = request.data.get('email')
    password = request.data.get('password')
    role = request.data.get('role')

    user = Authentication.signup(self, email=email, password=password, role=role)

    serializer = UserSerializer(user)

    return Response({'user': serializer.data})




