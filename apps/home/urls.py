from django.urls import path

from .views import *

urlpatterns = [
    path("krystian/", PersonalInfoListView.as_view()),
    path("work/", SkillListView.as_view()),
]
