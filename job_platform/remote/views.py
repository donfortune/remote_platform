from django.shortcuts import render, redirect
from .models import Profile
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import CustomUserCreationForm


# Create your views here.
def index(request):
    return render(request, 'index.html')

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
                return redirect('jobs_dashboard')  # URL name for the job seeker dashboard
            elif profile.role == 'recruiter':
                return redirect('recruiter_dashboard')  # URL name for the recruiter dashboard
             

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
                return redirect('jobs_dashboard')  # Job seeker dashboard URL
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
    return render(request, 'jobs.html')

def get_profiles(request):
    profiles = Profile.objects.all()
    return render(request, 'profiles.html', {'profiles': profiles})

@login_required
def get_profile(request, id):
    profile = Profile.objects.get(id=id)
    return render(request, 'profile.html', {'profile': profile})
    