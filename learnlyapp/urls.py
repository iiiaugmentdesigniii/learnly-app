from django.urls import path
from . import views

urlpatterns = [
path('about/', views.about, name='about'),


path('', views.base, name='base'),

path('course_info/', views.course_info, name='course_info'),
path('creation_training/', views.creation_training, name='creation_training'),
path('creation_user/', views.creation_user, name='creation_user'),
path('dashboard', views.dashboard, name='dashboard'),
path('home/', views.home, name='home'),
path('login/', views.login, name='login'),
path('password_forgot/', views.password_forgot, name='password_forgot'),
path('user_management/', views.user_management, name='user_management'),
]