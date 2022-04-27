from django.db import models
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField

from apps.common.models import TimeStampedUUIDModel

# from django.contrib.auth import get_user_model

# User = get_user_model()


class PersonalInfo(TimeStampedUUIDModel):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = PhoneNumberField(default=+2348037286666)
    email = models.EmailField(max_length=80)
    address = models.CharField(max_length=180)
    image = models.ImageField(upload_to="mediafiles/", null=False, blank=False)
    resume = models.FileField(upload_to="mediafiles/", null=False, blank=False)

    def fullname(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.fullname()


class Skill(TimeStampedUUIDModel):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=150)
    image_banner = models.ImageField(null=False, blank=False)

    def __str__(self):
        return self.title
