
from django.shortcuts import render
from job_app.models import Category
from job_app.models import Jobtype


def categories(request):
    category_list = Category.objects.all()
    return {"categories": category_list}
def jobtypes(request):
    jobtype_list =Jobtype.objects.all()
    return{"jobtypes":jobtype_list}