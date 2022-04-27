from django.shortcuts import render
from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics, permissions
from rest_framework.permissions import IsAdminUser

from apps.home.models import Contact, PersonalInfo, Work
from apps.home.serializers import (
    ContactSerializer,
    PersonalInfoSerializer,
    WorkSerializer,
)


class PersonalInfoListView(generics.ListAPIView):
    queryset = PersonalInfo.objects.all()
    serializer_class = PersonalInfoSerializer
    permission_classes = [AllowAny]


class PersonalInfoRUDView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PersonalInfo.objects.all()
    serializer_class = PersonalInfoSerializer
    permission_classes = [IsAdminUser]


class WorkListView(generics.ListAPIView):
    queryset = Work.objects.all()
    serializer_class = WorkSerializer
    permission_classes = [AllowAny]


class ContactCreateView(generics.CreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = []
