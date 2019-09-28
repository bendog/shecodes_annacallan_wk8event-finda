from rest_framework import viewsets
from eventFinderApp.models import Event
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import CustomUser
from .serializers import CustomUserSerializer
from rest_framework import serializers
from .models import CustomUser


class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = (IsAuthenticated,)

def get_queryset(self):
        user = self.request.user
        return CustomUser.objects.filter(pk=user.id)




