from django.db import models
from django.conf import settings

# Create your models here.

from django.urls import reverse
from django.contrib.auth.models import User

from django.db import models
from django.utils import timezone
class Jobtype(models.Model):
    title = models.CharField(max_length=40)
    class Meta:
        verbose_name_plural ="Jobtype"
    def __str__(self):
        return self.title
    

class Category(models.Model):
    title = models.CharField(max_length=30)

    class Meta:
        verbose_name_plural = "Categories"


    def __str__(self):
        return self.title

class Jobs(models.Model):
    title = models.CharField(max_length=300)
    required_no = models.CharField(max_length=20)
    job_requirements = models.TextField()
    qualifications = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)

    count = models.IntegerField(default=0)
    slug = models.SlugField(max_length=255, null=True)
    location = models.CharField(max_length=150)
    company_name = models.CharField(max_length=100)
    company_description = models.TextField()
    jobtype = models.ManyToManyField(Jobtype, related_name="job_types")
    category = models.ManyToManyField(Category, related_name="job_categoreis")
    last_date = models.DateTimeField()
    website = models.CharField(max_length=100)
    created_at = models.DateTimeField(default=timezone.now)
    last_date = models.DateTimeField()
    filled = models.BooleanField(default=False)
    salary = models.IntegerField(default=0, blank=True)
    
    def get_absolute_url(self):
        return reverse("single_jobs", kwargs={"pk": self.pk, "slug": self.slug})
class Applicants(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    created_at = models.DateTimeField(default=timezone.now)

    website = models.CharField(max_length=100)
    cv = models.FileField(("cyz.pdf"), upload_to='uploaded_files/',default='')
    coverletter = models.TextField()