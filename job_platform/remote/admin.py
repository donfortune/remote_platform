from django.contrib import admin
from .models import Profile,Job,Category

# Register your models here.
admin.site.register(Profile)
admin.site.register(Job)
admin.site.register(Category)