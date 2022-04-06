from .models import Category, Project
from .serializers import CategorySerializer, ProjectSerializer
from rest_framework import generics
from rest_framework.permissions import IsAdminUser

class CategoryView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminUser]


class ProjectDetailView(generics.RetrieveAPIView):
    queryset = Project.objects.get()
    serializer_class = ProjectSerializer
    permission_classes = [IsAdminUser]