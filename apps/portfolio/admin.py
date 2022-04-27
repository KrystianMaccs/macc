from django.contrib import admin

from apps.portfolio.models import Category, Project


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("title", "description", "url", "img")


class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "description", "url", "img")


admin.site.register(Category, CategoryAdmin)
admin.site.register(Project, ProjectAdmin)
