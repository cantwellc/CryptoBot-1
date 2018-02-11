from django.contrib.auth.models import User
from rest_framework import viewsets
from cryptobot.serializers import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
  """
  API endpoint that allows Users to be viewed and edited
  """
  queryset = User.objects.all()
  serializer_class = UserSerializer
