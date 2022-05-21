from django.urls import path
from rest_framework.routers import DefaultRouter

from apps.home import views

home_router = DefaultRouter()
home_router.register('personal_info', views.PersonalInfoView,basename="personal_info")
home_router.register('skill', views.SkillView,basename="skill")
