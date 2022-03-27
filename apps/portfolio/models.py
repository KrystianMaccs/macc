from django.db import models
from apps.common.models import TimeStampedUUIDModel


class Category(TimeStampedUUIDModel):
    title = models.CharField(max_length=30, verbose_name="Title")
    description = models.TextField()
    url = models.URLField()
    img = models.ImageField(upload_to=None)

    def __str__(self):
        return f"{self.title.title()}"

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

class Project(TimeStampedUUIDModel):
    title = models.CharField(max_length=30, verbose_name="Title")
    description = models.TextField()
    url = models.URLField()
    project = models.ForeignKey(Category, on_delete=models.CASCADE)
    img = models.ImageField(upload_to=None)

    def __str__(self):
        return f"{self.title.title()}"

    class Meta:
        verbose_name = "Project"
        verbose_name_plural = "Projects"
