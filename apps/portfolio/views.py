from drf_yasg.utils import swagger_auto_schema
from rest_framework import permissions, viewsets

from .models import Category, Project
from .serializers import CategorySerializer, ProjectSerializer


class CategoryView(viewsets.ModelViewset):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAccountAdminOrReadOnly]


class ProjectView(viewsets.ModelViewset):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAccountAdminUser]
