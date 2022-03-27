from django.contrib import admin

from apps.portfolio.models import Category, Project


admin.site.register(Category)
admin.site.register(Project)
