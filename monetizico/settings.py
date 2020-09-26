"""
Django settings for monetizico project.

Generated by 'django-admin startproject' using Django 3.1.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path
import environ

env = environ.Env()
environ.Env.read_env()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve(strict=True).parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '&6do#34%@9g9l0ki3v5%^9tbnnjbz9m+xh8)m^b9u5bw_@z&n='

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# environ stuff


ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django_s3_storage',
    'main_app',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_sass_compiler',
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

ROOT_URLCONF = 'monetizico.urls'

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
            'libraries': {
                'custom_tags': 'main_app.templatetags.custom_tags',
            }
        },
    },
]

WSGI_APPLICATION = 'monetizico.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'monetizico',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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

PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
    'django.contrib.auth.hashers.BCryptPasswordHasher',
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
    'django.contrib.auth.hashers.Argon2PasswordHasher',
]


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
LOGIN_REDIRECT_URL = '/' #fix me
LOGOUT_REDIRECT_URL = '/' #fix me

STRIPE_PUBLISHABLE_KEY = 'pk_test_51HRSLCLOlRhWszAlat6npafXudcrNO1N0R9HYd495xBtLBDn1i13mANYb3JLWOa4DHwxk5DS4YNCct1gMZ9sdiIt001CKJMdUz'
STRIPE_SECRET_KEY = 'sk_test_51HRSLCLOlRhWszAlwKUgBAeqsEzqsH4p3pAo5CF3tipwvCyuiMxfUFNKJ9QE0lbUHxEzVlybNrriTdpqfbS7QHK100fA7kexcw'
STRIPE_ENDPOINT_SECRET = env("STRIPE_ENDPOINT_SECRET")

# AWS Stuff django-s3-storage
AWS_REGION = "us-east-2"
AWS_ACCESS_KEY_ID = env("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = env("AWS_SECRET_ACCESS_KEY")
AWS_S3_BUCKET_NAME = "exchange-2"
DEFAULT_FILE_STORAGE = "django_s3_storage.storage.S3Storage"
AWS_S3_BUCKET_NAME_STATIC = "exchange-2"
AWS_S3_BUCKET_AUTH_STATIC = False
AWS_S3_BUCKET_AUTH = False
AWS_S3_MAX_AGE_SECONDS = 60 * 60 * 24 * 365
AWS_S3_MAX_AGE_SECONDS_CACHED_STATIC = 60 * 60 * 24 * 265