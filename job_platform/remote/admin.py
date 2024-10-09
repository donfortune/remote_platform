from django.contrib import admin
from .models import Profile,Job,Category, JobApplication
from .forms import JobForm

class JobAdmin(admin.ModelAdmin):
    form = JobForm

# Register your models here.
admin.site.register(Profile)
admin.site.register(Job, JobAdmin)
admin.site.register(Category)
admin.site.register(JobApplication)