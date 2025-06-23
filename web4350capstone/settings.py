# Import environ for Windows-compatible .env file handling
import environ
import os
import sys
from pathlib import Path

# Initialize environment variables
env = environ.Env()
environ.Env.read_env(os.path.join(os.path.dirname(__file__), '..', '.env'))

# Build paths inside the project
BASE_DIR = Path(__file__).resolve().parent.parent

# Security settings
SECRET_KEY = env('DJANGO_SECRET_KEY', default='unsafe-secret-key')
# DEBUG = env.bool('DJANGO_DEBUG', default=False)
DEBUG = True  # Temporarily set this to True


# Allowed hosts for Render deployment
# ALLOWED_HOSTS = env.list('ALLOWED_HOSTS', default=['localhost', '127.0.0.1'])
ALLOWED_HOSTS = ['web4350capstone-dooc.onrender.com', 'localhost', '127.0.0.1']


# Adjust Render build command to avoid Poetry issues
if 'collectstatic' in sys.argv:
    try:
        sys.argv.remove('--noinput')
    except ValueError:
        pass  # Safely handle missing '--noinput' flag
    sys.argv.append('--no-input')

# Application definition
INSTALLED_APPS = [
    'learnlyapp',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # Add this line here
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'web4350capstone.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "learnlyapp/templates"],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'web4350capstone.wsgi.application'

# Database settings for SQLite or Render Postgres
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / "db.sqlite3",
    }
}

# Static files configuration for Render deployment
# STATIC_URL = '/static/'
# STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'
# Add this to tell Django where to find additional static files (like images, CSS, JS)
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'learnlyapp', 'static')
]
# STATIC_ROOT = BASE_DIR / 'staticfiles'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')


# Default auto field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = 'learnlyapp.User'