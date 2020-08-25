"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 3.1.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve(strict=True).parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "rn49+8-k!e5aj6=$-qa7w5++a1o8=57%dx8vu$6eyq(12=)4+q"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Django에서 기본으로 제공해주는 App들
DJANGO_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

# startapp 명령어로 추가해준 App들
PROJECT_APPS = [
    "map.apps.MapConfig",
    "bakeries.apps.BakeriesConfig",
    "posts.apps.PostsConfig",
    "users.apps.UsersConfig",
]

# 외부에서 기능을 미리 만들어놓은 App들
THIRD_PARTY_APPS = [
    "phonenumber_field",
    "storages",
]

INSTALLED_APPS = DJANGO_APPS + PROJECT_APPS + THIRD_PARTY_APPS

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
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

WSGI_APPLICATION = "config.wsgi.application"


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

"""
장고 기본 DB셋팅
"""
# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.sqlite3",
#         "NAME": BASE_DIR / "db.sqlite3",
#     }
# }

"""
AWS RDS 셋팅
"""
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "HOST": "realbroaddb.cmahcmtbzlbw.ap-northeast-2.rds.amazonaws.com",
        "PORT": "5432",
        "NAME": "broad",
        "USER": "eunchae",
        "PASSWORD": "ajttk8rl",
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",},
]


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "Asia/Seoul"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

# """
# Static 관련 설정
# """
# 웹 페이지에서 사용할 정적 파일의 최상위 URL 경로
STATIC_URL = "/static/"
# 개발단계에서 사용하는 정적파일들이 위치한 경로
STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]
# collectstatic명령어를 통해 Django 프로젝트에서 사용하는 모든 정적 파일을 한 곳에 모아넣는 경로(배포시 사용하기 위해)
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")


# """
# Media 관련 설정
# """
# # 사용자에 의해 업로드되는 미디어 파일을 저장할 경로
# MEDIA_ROOT = os.path.join(BASE_DIR, "uploads")
# # 웹 페이지에서 사용할 미디어 파일의 최상위 URL 경로
# MEDIA_URL = "/media/"
AWS_REGION = "ap-northeast-2"
AWS_STORAGE_BUCKET_NAME = "broadbucket"
AWS_QUERYSTRING_AUTH = False
AWS_S3_HOST = "s3.%s.amazonaws.com" % AWS_REGION
AWS_ACCESS_KEY_ID = "AKIARCO3S5EAYX2D6BCS"
AWS_SECRET_ACCESS_KEY = "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"
AWS_S3_CUSTOM_DOMAIN = "%s.s3.amazonaws.com" % AWS_STORAGE_BUCKET_NAME

# # Static Setting
# STATIC_URL = "https://%s/" % AWS_S3_CUSTOM_DOMAIN
# STATICFILES_STORAGE = "storages.backends.s3boto.S3BotoStorage"

# Media Setting
MEDIA_URL = "https://%s/" % AWS_S3_CUSTOM_DOMAIN
DEFAULT_FILE_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"

# User 모델 커스터마이징
AUTH_USER_MODEL = "users.User"

