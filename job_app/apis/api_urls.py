from django.urls import path
from job_app.apis.api_views import (
    CategoryListAPIView,
    JobsListAPIView,
    JobsRetriveAPIView,
    JobsCreateAPIView,
    jobsDestroyAPIView,
)

# urls
urlpatterns = [
    path("categories/", CategoryListAPIView.as_view(), name="list_category"),
    path("list/", JobsListAPIView.as_view(), name="list_jobs"),
    path("list/<pk>/", JobsRetriveAPIView.as_view()),
    path("list/<pk>/remove/", JobsDestroyAPIView.as_view()),
    path("", JobsCreateAPIView.as_view()),
]