from django.urls import path

from .views import *

urlpatterns = [
    path("krystian", PersonalInfoListView.as_view()),
    path("<int:pk>", PersonalInfoEditView.as_view()),
    path("create", PersonalInfoCreateView.as_view()),
    path("<int:pk>/delete", PersonalInfoDeleteView.as_view()),
    path("work", WorkListView.as_view()),
    path("work-create", WorkCreateView.as_view()),
    path("work/<int:pk>", WorkEditView.as_view()),
    path("work/<int:pk>/delete", WorkDeleteView.as_view()),
    path("contact", ContactCreateView.as_view()),
]
