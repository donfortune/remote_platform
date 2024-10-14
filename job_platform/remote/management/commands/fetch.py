from django.core.management.base import BaseCommand
import requests
from remote.models import Job, Category, Profile

class Command(BaseCommand):
    help = 'Fetch jobs from a remote API'

    def handle(self, *args, **kwargs):
        url = 'https://remoteok.com/api'  # External API endpoint
        response = requests.get(url)

        if response.status_code == 200:
            jobs = response.json()
            default_recruiter = Profile.objects.first()  # You can set this to any default recruiter
            default_category = Category.objects.get(id=1)  # Or any category you wish to default to

            for job_data in jobs:
                location = job_data.get('location', 'Remote')  # Default to 'Remote' if no location provided
                if 'remote' in location.lower():
                    title = job_data.get('position', 'N/A')
                    company_name = job_data.get('company', 'N/A')
                    description = job_data.get('description', 'N/A')
                    apply_url = job_data.get('apply_url', None)  # Get the apply URL from API response

                    # Check if the job already exists in the database
                    if not Job.objects.filter(title=title, company_name=company_name).exists():
                        # Save the job to the database
                        Job.objects.create(
                            title=title,
                            description=description,
                            location=location,
                            company_name=company_name,
                            recruiter=default_recruiter,  # Assign to default recruiter
                            category=default_category,  # Assign to default category
                            featured=False,  # Set default value for featured
                            views_count=0,  # Set default value for views count
                            status='open',  # Set default status to 'open'
                            apply_url=apply_url  # Save apply URL
                        )

            self.stdout.write(self.style.SUCCESS('Jobs fetched and saved successfully!'))
        else:
            self.stdout.write(self.style.ERROR('Failed to fetch jobs from the API.'))
