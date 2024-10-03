from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('signup_recruiter/', views.signup_recruiter_view, name='signup_recruiter'),
    path('jobs_dashboard/', views.jobs_dashboard, name='jobs_dashboard'),
    path('logout/', views.logout_view, name='logout'),
    path('recruiter_dashboard/', views.recruiter_dashboard, name='recruiter_dashboard'),
]