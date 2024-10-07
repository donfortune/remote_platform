from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('signup_recruiter/', views.signup_recruiter_view, name='signup_recruiter'),
    path('jobs_dashboard/', views.jobs_dashboard, name='jobs_dashboard'),
    path('logout/', views.logout_view, name='logout'),
    path('recruiter_dashboard/', views.recruiter_dashboard, name='recruiter_dashboard'),\
    path('profile/<int:id>/', views.get_profile, name='get_profile'),
    path('profiles/', views.get_profiles, name='get_profiles'),
    path('job_listing/', views.job_listing, name='job_listing'),
    path('edit_recruiter_profile/<int:id>/', views.edit_recruiter_profile, name='edit_recruiter_profile'),
    path('edit_user_profile/<int:id>/', views.edit_user_profile, name='edit_user_profile'),
    path('view_cv/<int:id>/', views.view_cv, name='view_cv'),
    path('add_cv/<int:id>/', views.add_cv, name='add_cv'),
    path('get_job/', views.get_job, name='get_job'),
    path('get_jobs/<int:id>/', views.get_jobs, name='get_jobs'),
    path('about_us/', views.about_us, name='about_us'),
    path('contact_us/', views.contact_us, name='contact_us'),
    path('terms/', views.terms, name='terms'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)