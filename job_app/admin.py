from django.contrib import admin
from job_app.models import Jobs,Category,Jobtype

# Register your models here.




@admin.register(Jobs)
class JobsAdmin(admin.ModelAdmin):
    list_display = ("title", "location","company_name","company_description","created_at")
    prepopulated_fields = {"slug": ("title",)}
    # readonly_fields = ("author",)
    # 
    # 
admin.site.register(Category)
admin.site.register(Jobtype)