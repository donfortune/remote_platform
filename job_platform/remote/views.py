from django.shortcuts import render, redirect
from .models import Profile, User, Job, Category, JobApplication
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import CustomUserCreationForm, RecruiterEditForm, UserEditForm, JobForm
from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.contrib import messages




# Create your views here.
# def index(request):
#     featured_jobs = Job.objects.filter(featured=True) 
#     return render(request, 'index.html', {'jobs': featured_jobs})

def index(request):
    jobs = Job.objects.all()
    featured_jobs = Job.objects.filter(featured=True)
    context = {
        'jobs': jobs,
        'featured_jobs': featured_jobs
    }
    return render(request, 'index.html', context)

# def signup_view(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             return render(request, 'login.html')    
#     else:
#         form = UserCreationForm()
#     return render(request, 'signup.html', {'form': form})

def signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            profile = Profile.objects.create(
                user=user,
                role=form.cleaned_data['role'],
                bio=form.cleaned_data.get('bio', ''),
                location=form.cleaned_data.get('location', ''),
                company_name=form.cleaned_data.get('company_name', ''),
                resume=form.cleaned_data.get('resume', None),
            )
            login(request, user)
            
              

            # Check the role and redirect to the appropriate dashboard
            if profile.role == 'job_seeker':
                return redirect('login')  
            elif profile.role == 'recruiter':
                return redirect('login')
                
             

    else:
        form = CustomUserCreationForm()

    return render(request, 'signup.html', {'form': form})

def signup_recruiter_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            profile = Profile.objects.create(
                user=user,
                role=form.cleaned_data['role'],
                bio=form.cleaned_data.get('bio', ''),
                location=form.cleaned_data.get('location', ''),
                company_name=form.cleaned_data.get('company_name', ''),
                resume=form.cleaned_data.get('resume', None),
            )
            login(request, user)
            return redirect('recruiter_dashboard')
    else:
        form = CustomUserCreationForm()

    return render(request, 'signup_recruiter.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)

            # Get the user's profile to check their role
            profile = Profile.objects.get(user=user)

            # Redirect based on the user's role
            if profile.role == 'job_seeker':
                return redirect('job_listing')  # Job seeker dashboard URL
            elif profile.role == 'recruiter':
                return redirect('recruiter_dashboard')  # Recruiter dashboard URL
            else:
                return redirect('default_dashboard')  # Default or fallback dashboard
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})


def login_recruiter_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return render(request, 'recruiters.html')
    else:
        form = AuthenticationForm()
    return render(request, 'login_recruiter.html', {'form': form})

def logout_view(request):
    logout(request)
    return render(request, 'index.html')

# def recruiter_dashboard(request):
#     category = Category.objects.all()
#     recruiter = Category.objects.get(slug='recruiters')
#     print(category)
#     context = {
#         'category': category,
#         'recruiter': recruiter
#     }
#     return render(request, 'recruiters.html', context)

# def recruiter_dashboard(request):
#     category = Category.objects.all()  # Fetch all categories
#     profile = None

#     # Check if a Profile exists for the current user
#     try:
#         profile = Profile.objects.get(user=request.user)

#         # Ensure the user is a recruiter
#         if profile.role != 'recruiter':
#             return render(request, 'error.html', {'message': 'You do not have permission to access this page.'})

#     except Profile.DoesNotExist:
#         return render(request, 'error.html', {'message': 'Profile does not exist.'})

#     # Pass the categories and profile to the template
#     context = {
#         'category': category,
#         'profile': profile
#     }

#     return render(request, 'recruiters.html', context)

def recruiter_dashboard(request):
    category = Category.objects.all()
    applicants = JobApplication.objects.all()
    profile = None
    jobs = []

    profile = Profile.objects.get(user=request.user)
    jobs = Job.objects.filter(recruiter=profile)
    if profile.role == 'recruiter':
        context = {
            'category': category,
            'profile': profile,
            'jobs': jobs,
            'applicants': applicants
        }
        return render(request, 'recruiters.html', context)
    
    



@login_required
def jobs_dashboard(request):
    profile = Profile.objects.get(user=request.user)
    return render(request, 'jobs.html', {'profile': profile})

def get_profiles(request):
    profiles = Profile.objects.all()
    return render(request, 'profiles.html', {'profiles': profiles})

@login_required
def get_profile(request, id):
    profile = Profile.objects.get(id=id)
    return render(request, 'profile.html', {'profile': profile})

def job_listing(request):
    category = Category.objects.all()  # Get all categories
    jobs = Job.objects.all()  # Get all jobs
    
    context = {
        'category': category,  # Updated variable name
        'jobs': jobs
    }
    return render(request, 'job_listing.html', context)


# def job_listing(request):
#     category = Category.objects.all()
#     software_job = Category.objects.get(slug='software-development')
#     context = {
#         'category': category,
#         'software_job': software_job,
#     }
#     return render(request, 'job_listing.html', context)

def edit_recruiter_profile(request, id):
    profile = Profile.objects.get(id=id)
    if request.method == 'POST':
        form = RecruiterEditForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('get_profile', id=id)
    else:
        form = RecruiterEditForm(instance=profile)

    return render(request, 'edit_profile.html', {'form': form}) 
    
def edit_user_profile(request, id):
    user = User.objects.get(id=id)
    if request.method == 'POST':
        form = UserEditForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('get_profile', id=id)
    else:
        form = UserEditForm(instance=user)

    return render(request, 'edit_profile.html', {'form': form})

def view_cv(request, id):
    profile = Profile.objects.get(id=id)
    if profile.resume:
        # Serve the file as an attachment
        response = HttpResponse(profile.resume, content_type='application/pdf')
        response['Content-Disposition'] = f'inline; filename="{profile.resume.name}"'
        return response
    else:
        return HttpResponse("No CV found.", status=404)


def add_cv(request, id):
    profile = Profile.objects.get(id=id)
    if request.method == 'POST':
        profile.resume = request.FILES['resume']
        profile.save()
        return redirect('get_profile', id=id)
    return render(request, 'add_cv.html', {'profile': profile})

def get_jobs(request):
    jobs = Job.objects.all()
    category = Category.objects.get(slug='software-development')
    context = {
        'jobs': jobs,
        'category': category
    }
    return render(request, 'job_listing.html', context)

def get_job(request, id):
    job = Job.objects.get(id=id) 
    print(job)
    return render(request, 'index.html', {'job': job})

def about_us(request):
    return render(request, 'about_us.html')

def contact_us(request):
    return render(request, 'contact_us.html')

def terms(request):
    return render(request, 'terms.html')

# def job_listing_by_category(request, slug):
#     category = Category.objects.get(slug=slug)
#     jobs = Job.objects.filter(category=category)
#     context = {
#         'category': category,
#         'jobs': jobs
#     }
#     return render(request, 'job_listing.html', context)

def job_details(request, id):
    job = Job.objects.get(id=id)
    job.views_count += 1
    job.save()
    context = {
        'job': job
    }
    return render(request, 'job_details.html', context)


        
def create_job(request):
    if request.method == 'POST':
        form = JobForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('recruiter_dashboard')  # Redirect to a job listing page or wherever appropriate
        else: 
            print(form.errors)
    else:
        form = JobForm()
    return render(request, 'recruiters.html', {'form': form})

def application(request, id):
    job = Job.objects.get(id=id)
    context = {
        'job': job
    }
    return render(request, 'application.html', context)

# def submitted_application(request, id):
#     if request.method == 'POST':
#         data = request.POST
#         job = Job.objects.get(id, id=data['job_id'])
#         application = JobApplication.objects.create(
#             user=request.user,
#             job=job,
#             full_name=data['full_name'],
#             email=data['email'],
#             cv_file=request.FILES['cv_file'],
#             cover_letter=data['cover_letter']
#         )
#         context = {
#             'application': application
#         }
#         return render(request, 'application.html', context)

def submitted_application(request, id):
    job = get_object_or_404(Job, id=id)  # Ensure the job exists

    if request.method == 'POST':
        data = request.POST
        # Ensure job_id is coming from the request
        if 'job_id' not in data or int(data['job_id']) != job.id:
            messages.error(request, "Invalid job ID.")
            return render(request, 'application.html', {'job': job})

        # Ensure cv_file is provided
        cv_file = request.FILES.get('cv_file')
        if not cv_file:
            messages.error(request, "Please upload a CV file.")
            return render(request, 'application.html', {'job': job})

        # Create the job application
        application = JobApplication.objects.create(
            user=request.user,
            job=job,
            full_name=data['full_name'],
            email=data['email'],
            cv_file=cv_file,
            cover_letter=data['cover_letter']
        )

        messages.success(request, "Your application has been submitted successfully!")
        context = {
            'application': application
        }
        return render(request, 'application.html', context)

    # If the request method is not POST, render the application form
    return render(request, 'application.html', {'job': job})

def view_applicants(request, id):
    job = Job.objects.get(id=id)
    applications = JobApplication.objects.filter(job=job)
    print(applications)
    context = {
        'job': job,
        'applications': applications
    }
    return render(request, 'view_applicant.html', context)

    

