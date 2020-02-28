from django import forms
from job_app.models import Jobs 
from job_app.models import Category


class JobsCreateForm(forms.ModelForm):
    CATEGORY_CHOICES = [(category.id, category.title) for category in Category.objects.all()]
    category = forms.MultipleChoiceField(
        required=True, widget=forms.CheckboxSelectMultiple, choices=CATEGORY_CHOICES,
    )

    class Meta:
        model = Jobs
        fields = "title","qualifications","job_requirements","location", "category","jobtype","company_name","company_description","website","created_at","last_date","filled","salary"