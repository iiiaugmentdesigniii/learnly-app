from django.shortcuts import render

def about(request):
    return render(request, "learnlyapp/about.html")

def base(request):
    return render(request, "learnlyapp/base.html")

def course_info(request):
    return render(request, "learnlyapp/course_info.html")

def creation_training(request):
    return render(request, "learnlyapp/creation_training.html")


def creation_user(request):
    return render(request, "learnlyapp/creation_user.html")
def dashboard(request):
    return render(request, "learnlyapp/dashboard.html")
def home(request):
    return render(request, "learnlyapp/home.html")
def login(request):
    return render(request, "learnlyapp/login.html")
def password_forgot(request):
    return render(request, "learnlyapp/password_forgot.html")
def user_management(request):
    return render(request, "learnlyapp/user_management.html")