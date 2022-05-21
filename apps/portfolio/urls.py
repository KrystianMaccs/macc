from django.urls import path
from rest_framework.routers import DefaultRouter

from apps.portfolio import views

portfolio = DefaultRouter()
portfolio.register('projects', views.ProjectView,basename="projects")
portfolio.register('category', views.CategoryView,basename="category")
