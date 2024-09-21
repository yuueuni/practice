from django.conf import settings
from rest_framework import viewsets

from accounts.serializers import UserSerializer


User = settings.AUTH_USER_MODEL

class AccountViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
