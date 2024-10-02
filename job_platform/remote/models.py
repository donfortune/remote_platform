from django.db import models
from django.contrib.auth.models import User

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
