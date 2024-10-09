from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your models here.
ROLE_CHOICES = (
    ('recruiter', 'Recruiter'),
    ('job_seeker', 'Job Seeker'),
)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    role = models.CharField(max_length=30, choices=ROLE_CHOICES)  # Use choices for predefined options
    company_name = models.CharField(max_length=100, blank=True, null=True)  # Recruiters' company
    resume = models.FileField(upload_to='resumes/', blank=True, null=True)  # Job seekers' resume

    def __str__(self):
        return self.user.username
    
class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    slug = models.SlugField(unique=True)


    def __str__(self):
        return self.name

class Job(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    location = models.CharField(max_length=30)
    company_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    recruiter = models.ForeignKey(Profile, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    featured = models.BooleanField(default=False)
    views_count = models.IntegerField(default=0)
  

    def __str__(self):
        return self.title
    

class JobApplication(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)  # Assuming you have a Job model
    full_name = models.CharField(max_length=255)
    email = models.EmailField()
    cv_file = models.FileField(upload_to='resumes/')
    cover_letter = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} - {self.job.title}"
