from django.urls import path
from rest_framework.routers import DefaultRouter

from apps.portfolio import views

portfolio_router = DefaultRouter()
portfolio_router.register('projects', views.ProjectView,basename="projects")
portfolio_router.register('category', views.CategoryView,basename="category")
