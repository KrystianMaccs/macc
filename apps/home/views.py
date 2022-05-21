from django.shortcuts import render
from drf_yasg.utils import swagger_auto_schema
from rest_framework import permissions, viewsets

from apps.home.models import PersonalInfo, Skill
from apps.home.serializers import PersonalInfoSerializer, SkillSerializer


class PersonalInfoView(viewsets.ModelViewset):
    queryset = PersonalInfo.objects.all()
    serializer_class = PersonalInfoSerializer
    permission_classes = [permissions.IsAccountAdminOrReadOnly]


class SkillView(viewsets.ModelViewset):
    queryset = PersonalInfo.objects.all()
    serializer_class = SkillSerializer
    permission_classes = [permissions.IsAccountAdminOrReadOnly]

