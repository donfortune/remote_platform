from django.shortcuts import render, redirect
from .models import Profile, User, Job, Category
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import CustomUserCreationForm, RecruiterEditForm, UserEditForm
from django.http import HttpResponse



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

def recruiter_dashboard(request):
    return render(request, 'recruiters.html')



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
    category = Category.objects.all()
    context = {
        'category': category
    }
    return render(request, 'job_listing.html', context)

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
    print(f'Jobs retrieved: {jobs}') 
    return render(request, 'index.html', {'jobs': jobs})

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
