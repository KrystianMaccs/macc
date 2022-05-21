from django.shortcuts import render
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from apps.home.models import PersonalInfo, Skill
from apps.home.serializers import PersonalInfoSerializer, SkillSerializer


class PersonalInfoView(viewsets.ModelViewSet):
    queryset = PersonalInfo.objects.all()
    serializer_class = PersonalInfoSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class SkillView(viewsets.ModelViewSet):
    queryset = PersonalInfo.objects.all()
    serializer_class = SkillSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

