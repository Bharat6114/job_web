
from django.shortcuts import render, get_object_or_404
from job_app.models import Category
from job_app.models import Jobs
from job_app.models import Jobtype
from job_app.models import Applicants
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.utils.text import slugify
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from django.views import View
from django.views.generic import (
    TemplateView,
    DeleteView,
    UpdateView,
    CreateView,
    ListView,
    DetailView,
)

from job_app.forms import JobsCreateForm
from job_app.forms import JobApplyForm
# Create your views here.
class JobtypeJobsView(View):
    def get(self, request,jobtype_id,*args, **kwargs):
    
        template_name = "job/catejories.html"
        jobtype = get_object_or_404(Jobtype, pk=jobtype_id)
        jobtype_Jobs_list = Jobs.objects.filter(jobtype=jobtype)
        return render(
            request, template_name, {"jobtype_jobs_list": jobtype_Jobs_list, "jobtype": jobtype}
        )
    
class CategoryJobsView(View):
    def get(self, request, category_id, *args, **kwargs):
        template_name  = "index.html"
        template_name = "job/categories.html"
        # category = Category.objects.get(pk=category_id)
        category = get_object_or_404(Category, pk=category_id)
        category_Jobs_list = Jobs.objects.filter(category=category)
        return render(
            request, template_name, {"category_jobs_list": category_Jobs_list, "category": category}
        )
class JobsTemplateView(TemplateView):
    template_name = "index.html"
     
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        catagories = Category.objects.all()
        category_jobs_list = {}
        jobtype_jobs_list = {}
        for category in catagories:
            category_jobs_list[category] = Jobs.objects.filter(category=category)
        context["jobs_list"] = Jobs.objects.all().order_by("-created_at")[:6]
        context["trending_job"] = Jobs.objects.order_by("-count")
        context["category_jobs_list"] = category_jobs_list
        context["jobtype_jobs_list"] = jobtype_jobs_list
        #print(context)
        return context
class JobsDetail(DetailView):
    model = Jobs
    template_name = "job/single_jobs.html"
    context_object_name = "detail_jobs"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        self.object.count = self.object.count + 1
        self.object.save()
        context["popular_jobs"] = Jobs.objects.order_by("-count")[:4]
        return context


class JobsCreateView(LoginRequiredMixin, CreateView):
    model = Jobs
    template_name = "job/create.html"
    login_url = reverse_lazy("login")
    success_url = reverse_lazy("home")
    form_class = JobsCreateForm

    def form_valid(self, form):
        Jobs = form.save(commit=False)
        title = form.cleaned_data["title"]
        slug = slugify(title)
        Jobs.slug = slug
        Jobs.author = self.request.user
        Jobs.save()

        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)


class JobsUpdateView(LoginRequiredMixin, UpdateView):
    model = Jobs
    template_name = "job/update.html"
    fields = "title", "description","job_requirements","location", "category","required_no","jobtype","company_name","company_description","website","created_at","last_date","filled","salary"
    login_url = reverse_lazy("login")
    success_url = reverse_lazy("home")


class JobsDeleteView(LoginRequiredMixin, DeleteView):
    model = Jobs
    login_url = reverse_lazy("login")
    success_url = reverse_lazy("home")

    def get(self, request, *args, **kwargs):
        return self.post(self, request, *args, **kwargs)
class JobsApplyView(LoginRequiredMixin,CreateView):
    model = Applicants
    template_name = "job/single_jobs.html.html"
    login_url = reverse_lazy("login")
    success_url = reverse_lazy("home")
    form_class = JobApplyForm

    def form_valid(self, form):
        Applicants = form.save(commit=False)
        Applicants.save()

        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)