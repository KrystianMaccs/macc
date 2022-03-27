from django.urls import path
from apps.portfolio.views import CategoryView, ProjectDetailView

urlpatterns = [
    path('list/', CategoryView.as_view()),
    path('list/<int:pkid>/', ProjectDetailView.as_view()),
]