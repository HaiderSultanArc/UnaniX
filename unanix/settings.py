"""
Django settings for unanix project.

Generated by 'django-admin startproject' using Django 4.1.6.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

import os
from pathlib import Path

import dotenv

dotenv.load_dotenv()

UNANIXDB_URI              = os.getenv('UNANIXDB_URI', default="")
UNANIXDB_DB               = os.getenv('UNANIXDB_DB', default="")
UNANIXDB_HOST             = os.getenv('UNANIXDB_HOST', default="")
UNANIXDB_USER             = os.getenv('UNANIXDB_USER', default="")
UNANIXDB_PASSWORD         = os.getenv('UNANIXDB_PASSWORD', default="")
UNANIXDB_PORT             = os.getenv('UNANIXDB_PORT', default="")

UNANIDATABASE_URI         = os.getenv('UNANIDATABASE_URI', default="")
UNANIDATABASE_DB          = os.getenv('UNANIDATABASE_DB', default="")
UNANIDATABASE_HOST        = os.getenv('UNANIDATABASE_HOST', default="")
UNANIDATABASE_USER        = os.getenv('UNANIDATABASE_USER', default="")
UNANIDATABASE_PASSWORD    = os.getenv('UNANIDATABASE_PASSWORD', default="")
UNANIDATABASE_PORT        = os.getenv('UNANIDATABASE_PORT', default="")

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-d^4rqp789e4qnce86gu%#q*!4m-m7c3v9@k@iuv+$b$p#fj*@6'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'backend',
]

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'unanix.urls'

LOGIN_REDIRECT_URL = 'home'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'unanix.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME':     UNANIXDB_DB,
        'USER':     UNANIXDB_USER,
        'PASSWORD': UNANIXDB_PASSWORD,
        'HOST':     UNANIXDB_HOST,
        'PORT':     UNANIXDB_PORT,
    },
    'unani_db': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME':     UNANIDATABASE_DB,
        'USER':     UNANIDATABASE_USER,
        'PASSWORD': UNANIDATABASE_PASSWORD,
        'HOST':     UNANIDATABASE_HOST,
        'PORT':     UNANIDATABASE_PORT,
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# STATICFILES_DIRS = [
#     os.path.join(BASE_DIR, 'frontend', 'static'),
# ]

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
