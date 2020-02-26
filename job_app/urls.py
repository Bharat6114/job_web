from django.urls import path
from job_app import views

urlpatterns = [
path("<category_id>/", views.CategoryJobsView.as_view(), name="category_jobs"),
path("<jobtype_id>/", views.JobtypeJobsView.as_view(), name="jobtype"),

path("<pk>/<slug>", views.JobsDetail.as_view(), name="single_jobs"),
]