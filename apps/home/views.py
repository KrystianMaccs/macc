from django.shortcuts import render
from rest_framework import generics 
from rest_framework.permissions import IsAdminUser
from drf_yasg.utils import swagger_auto_schema
from apps.home.serializers import (
    PersonalInfoSerializer,
    WorkSerializer,
    ContactSerializer,
    MyContactSerializer,
    )
from apps.home.models import PersonalInfo, Work, Contact, MyContact


class PersonalInfoCreateView(generics.CreateAPIView):
    queryset = PersonalInfo.objects.all()
    serializer_class = PersonalInfoSerializer
    permission_classes = [IsAdminUser]

class PersonalInfoListView(generics.ListAPIView):
    queryset = PersonalInfo.objects.all()
    serializer_class = PersonalInfoSerializer
    permission_classes = [IsAdminUser]


class PersonalInfoEditView(generics.RetrieveUpdateAPIView):
    queryset = PersonalInfo.objects.all()
    serializer_class = PersonalInfoSerializer
    permission_classes = [IsAdminUser]

class PersonalInfoDeleteView(generics.DestroyAPIView):
    queryset = PersonalInfo.objects.all()
    serializer_class = PersonalInfoSerializer
    permission_classes = [IsAdminUser]


class WorkCreateView(generics.CreateAPIView):
    queryset = Work.objects.all()
    serializer_class = WorkSerializer
    permission_classes = [IsAdminUser]

class WorkListView(generics.ListAPIView):
    queryset = Work.objects.all()
    serializer_class = WorkSerializer
    permission_classes = [IsAdminUser]

class WorkEditView(generics.RetrieveUpdateAPIView):
    queryset = Work.objects.all()
    serializer_class = WorkSerializer
    permission_classes = [IsAdminUser]

class WorkDeleteView(generics.DestroyAPIView):
    queryset = Work.objects.all()
    serializer_class = WorkSerializer
    permission_classes = [IsAdminUser]

class ContactCreateView(generics.CreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = []
