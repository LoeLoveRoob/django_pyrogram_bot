"""
Django settings for project_django_pyrogram_bot project_django_pyrogram_bot.
"""
from pathlib import Path

# Build paths inside the project_django_pyrogram_bot like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-d9efu82#^7)$54*nl4xj^y7zf(e3w9&jv_m-d6zspv))ue!ung"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Pyrogram BOT Settings
PYROGRAM_BOT = {
        "BOT_NAME": "Pyrogram Bot",  # This is only for reference, system will identify real name from get_me()
        "BOT_TOKEN": "5929067481:AAF3o5GUVg2p66U_9uDuipPOUwke4L8APz0",
        "BOT_PROXY": {"scheme": "socks5", "hostname": "localhost", "port": 9150, "username": "1", "password": "1"},
        "API_ID": "1167061",
        "API_HASH": "4de49642ae630ae385b6c10faa7155be",
        "ADMINS": (799041666,),
        "NOTIFY_STARTUP_ADMINS": True,
        "NOTIFY_SHUTDOWN_ADMINS": True,
        }

# Application definition

INSTALLED_APPS = [
        "django.contrib.admin",
        "django.contrib.auth",
        "django.contrib.contenttypes",
        "django.contrib.sessions",
        "django.contrib.messages",
        "django.contrib.staticfiles",

        # Pyrogram bot
        "bot.apps.BotConfig"
        ]

MIDDLEWARE = [
        "django.middleware.security.SecurityMiddleware",
        "django.contrib.sessions.middleware.SessionMiddleware",
        "django.middleware.common.CommonMiddleware",
        "django.middleware.csrf.CsrfViewMiddleware",
        "django.contrib.auth.middleware.AuthenticationMiddleware",
        "django.contrib.messages.middleware.MessageMiddleware",
        "django.middleware.clickjacking.XFrameOptionsMiddleware",
        ]

ROOT_URLCONF = "project_django_pyrogram_bot.urls"

TEMPLATES = [
        {
                "BACKEND": "django.template.backends.django.DjangoTemplates",
                "DIRS": [],
                "APP_DIRS": True,
                "OPTIONS": {
                        "context_processors": [
                                "django.template.context_processors.debug",
                                "django.template.context_processors.request",
                                "django.contrib.auth.context_processors.auth",
                                "django.contrib.messages.context_processors.messages",
                                ],
                        },
                },
        ]

WSGI_APPLICATION = "project_django_pyrogram_bot.wsgi.application"

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
        "default": {
                "ENGINE": "django.db.backends.sqlite3",
                "NAME": BASE_DIR / "db.sqlite3",
                }
        }

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
        {
                "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
                },
        {
                "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
                },
        {
                "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
                },
        {
                "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
                },
        ]

# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = "static/"

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# https://github.com/django/django/blob/main/django/utils/log.py
LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,

        'formatters': {
                'verbose': {
                        'format': '{levelname} {asctime} {module} {process:d} {thread:d} {message}',
                        'style': '{',
                        },
                'medium': {
                        'format': '[{module}]: {levelname} {asctime} {message}',
                        'style': '{',
                        },

                'simple': {
                        'format': '{levelname} {message}',
                        'style': '{',
                        },
                },

        'handlers': {
                'console': {
                        'level': 'DEBUG',
                        'class': 'logging.StreamHandler',
                        'formatter': 'simple'
                        },

                'console-medium': {
                        'level': 'DEBUG',
                        'class': 'logging.StreamHandler',
                        'formatter': 'medium'
                        },

                'console-verbose': {
                        'level': 'DEBUG',
                        'class': 'logging.StreamHandler',
                        'formatter': 'verbose'
                        },

                'file-medium': {
                        'level': 'DEBUG',
                        'class': 'logging.FileHandler',
                        'filename': '/'.join(
                                [f"{BASE_DIR.as_posix()}", "pyrogram_bot.log"]
                                ),
                        'formatter': 'medium'
                        },

                'file-verbose': {
                        'level': 'DEBUG',
                        'class': 'logging.FileHandler',
                        'filename': '/'.join(
                                [f"{BASE_DIR.as_posix()}", "pyrogram_bot.log"]
                                ),
                        'formatter': 'verbose'
                        },

                },

        'loggers': {
                'root': {
                        'handlers': ['console-medium', 'file-medium'],
                        'level': 'DEBUG',
                        },

                'pyrogram.session.session': {
                        'handlers': ['console-medium', 'file-medium'],
                        'level': 'WARNING',
                        },

                },

        }
