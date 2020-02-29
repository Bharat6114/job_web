from django.urls import path
from job_app import views

urlpatterns = [

path("create/", views.JobsCreateView.as_view(), name="create_jobs"),
path("update/<pk>", views.JobsUpdateView.as_view(), name="update_jobs"),
path("delete/<pk>", views.JobsDeleteView.as_view(), name="delete_jobs"),
path("<category_id>/", views.CategoryJobsView.as_view(), name="category_jobs"),
path("<jobtype_id>/", views.JobtypeJobsView.as_view(), name="jobtype"),
path("<pk>/<slug>", views.JobsDetail.as_view(), name="single_jobs"),
]
