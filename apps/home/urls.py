from django.urls import path
from rest_framework.routers import DefaultRouter

from apps.home import views

home = DefaultRouter()
home.register('personal_info', views.PersonalInfoView,basename="personal_info")
home.register('skill', views.SkillView,basename="skill")
