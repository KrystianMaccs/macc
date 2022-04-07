from .models import Category, Project
from .serializers import CategorySerializer, ProjectSerializer
from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from drf_yasg.utils import swagger_auto_schema


class CategoryCreateView(generics.CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminUser]
class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminUser]

class CategoryEditView(generics.RetrieveUpdateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminUser]

class CategoryDeleteView(generics.DestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminUser]

class ProjectCreateView(generics.CreateAPIView):
    queryset = Project.objects.get()
    serializer_class = ProjectSerializer
    permission_classes = [IsAdminUser]

class ProjectListView(generics.ListAPIView):
    queryset = Project.objects.get()
    serializer_class = ProjectSerializer
    permission_classes = [IsAdminUser]

class ProjectEditView(generics.RetrieveUpdateAPIView):
    queryset = Project.objects.get()
    serializer_class = ProjectSerializer
    permission_classes = [IsAdminUser]

class ProjectDeleteView(generics.DestroyAPIView):
    queryset = Project.objects.get()
    serializer_class = ProjectSerializer
    permission_classes = [IsAdminUser]