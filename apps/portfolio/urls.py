from django.urls import path
from apps.portfolio.views import (
    CategoryCreateView,
    CategoryListView,
    CategoryEditView,
    CategoryDeleteView,
    ProjectCreateView,
    ProjectListView,
    ProjectEditView,
    ProjectDeleteView,
 )

urlpatterns = [
    path('category-create', CategoryCreateView.as_view()),
    path('category-list', CategoryListView.as_view()),
    path('<int:pk>', CategoryEditView.as_view()),
    path('<int:pk>/delete', CategoryDeleteView.as_view()),
    path('project-create', ProjectCreateView.as_view()),
    path('category-list/<int:pk>', ProjectListView.as_view()),
    path('category-list/<int:pk>/delete', ProjectDeleteView.as_view()),

]