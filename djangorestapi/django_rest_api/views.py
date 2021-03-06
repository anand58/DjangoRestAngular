from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets, permissions
from djangorestapi.django_rest_api.serializers import UserSerializer, GroupSerializer
# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    persmission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    persmission_classes = [permissions.IsAuthenticated]
