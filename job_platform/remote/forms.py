from django import forms
from django.contrib.auth.models import User
from .models import Profile, Job, JobApplication

#modified UserCreationForm
class CustomUserCreationForm(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)
    role = forms.ChoiceField(choices=[('job_seeker', 'Job Seeker'), ('recruiter', 'Recruiter')])

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'role']

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user

class RecruiterEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'

        widgets = {
            'birth_date': forms.SelectDateWidget(years=range(1900, 2020)),
        }

class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'
        exclude = ['password', 'last_login', 'is_superuser', 'groups', 'user_permissions', 'is_staff', 'is_active', 'date_joined']


class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['title', 'description', 'location', 'company_name', 'category', 'recruiter', 'status']  # Or specify fields explicitly

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Filter the recruiters to only include those with the 'recruiter' role
        # self.fields['recruiter'].queryset = Profile.objects.filter(role='recruiter')

class ApplicationForm(forms.ModelForm):
    class Meta:
        model = JobApplication
        fields = ['full_name', 'email', 'cv_file', 'cover_letter']   # Or specify fields explicitly
    

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Filter the jobs to only include those that are not yet applied to by the current user
        self.fields['job'].queryset = Job.objects.exclude(jobapplication__user=self.request.user)