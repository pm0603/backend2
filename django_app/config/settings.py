"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 1.11.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""
import json
import os

# 환경 변수 값 - 최영민
DEBUG = os.environ.get('MODE') == 'DEBUG'
STORAGE_S3 = os.environ.get('STORAGE') == 'S3' or DEBUG is False
DB_RDS = os.environ.get('DB') == 'RDS' or DEBUG is False

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ROOT_DIR = os.path.dirname(BASE_DIR)

TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates')
# 사용자가 업로드한 파일들을 관리할 폴더의 경로를 지정
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
# 정적파일을 관리할 폴더 경로 지정
STATIC_DIR = os.path.join(BASE_DIR, 'static')
# 정적 파일을 모아서 서빙할 폴더 경로 지정 테스트시 serve관련 에러 날 경우 반드시 추가해야 함
STATIC_ROOT = os.path.join(BASE_DIR, 'static_root')

# Config files
CONF_DIR = os.path.join(ROOT_DIR, '.conf-secret')
CONFIG_FILE_COMMON = os.path.join(CONF_DIR, 'settings_common.json')

if DEBUG:
    CONFIG_FILE = os.path.join(CONF_DIR, 'settings_local.json')
else:
    CONFIG_FILE = os.path.join(CONF_DIR, 'settings_deploy.json')
config_common = json.loads(open(CONFIG_FILE_COMMON).read())
config = json.loads(open(CONFIG_FILE).read())

# common과 현재 사용설정(local or deploy)를 합쳐줌 - 최영민
for key, key_dict in config_common.items():
    if not config.get(key):
        config[key] = {}
    for inner_key, inner_key_dict in key_dict.items():
        config[key][inner_key] = inner_key_dict

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config['django']['secret_key']

# AWS 관련 설정(django-storages) - 최영민
AWS_ACCESS_KEY_ID = config['aws']['access_key_id']
AWS_SECRET_ACCESS_KEY = config['aws']['secret_access_key']
AWS_STORAGE_BUCKET_NAME = config['aws']['s3_storage_bucket_name']
AWS_S3_SIGNATURE_VERSION = config['aws']['s3_signature_version']
AWS_S3_HOST = 's3.{}.amazonaws.com'.format(config['aws']['s3_region'])
AWS_S3_CUSTOM_DOMAIN = '{}.s3.amazonaws.com'.format(AWS_STORAGE_BUCKET_NAME)

# S3 관련 설정 - 최영민
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
STATICFILES_LOCATION = 'static'
# https://s3.ap-northeast-2.amazonaws.com/elasticbeanstalk-ap-northeast-2-013847878072/admin/css/base.css
STATIC_URL = "https://%s/%s/" % (AWS_S3_HOST, config['aws']['s3_storage_bucket_name'])

ALLOWED_HOSTS = ["*"]

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'member.apps.MemberConfig',

    'rest_framework',
    'rest_framework.authtoken',

    # S3를 쓰기 위한 앱 - 최영민
    'storages',

    # CORS설정 - 최영민
    'corsheaders',

    # Content api - 김도경
    'content_api',
]

# REST 기본설정에 토큰 추가 - 최영민
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
    )
}


MIDDLEWARE = [

    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',

    # CORS 설정 - 최영민
    'corsheaders.middleware.CorsMiddleware',

    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

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

WSGI_APPLICATION = 'config.wsgi.application'

# CORS 설정 - 최영민
CORS_ORIGIN_WHITELIST = (
    'localhost:8080',
    'localhost:8000',
    'front.localhost:8000',
    'front.localhost:8000/*',
    'front.pm0603.com',
    'pm0603.com',
    'www.pm0603.com',
    'front.localhost/*',
    'pm0603.com/*',
    'www.pm0603.com',
    '*',
    'api.pm0603.com',
    'api.pm0603.com/*',
)

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

# DB관련 설정 - 최영민


if DB_RDS or DEBUG is False:
    db_config = config['db_rds']
    DATABASES = {
        'default': {
            'ENGINE': db_config['engine'],
            'NAME': db_config['name'],
            'USER': db_config['user'],
            'PASSWORD': db_config['password'],
            'HOST': db_config['host'],
            'PORT': db_config['port'],
        }
    }
# 로컬에서도 AWS RDS작동여부를 확인하고 에러 시 DEBUG를 확인하기 위해 주석처리 - 최영민

else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }

AUTH_USER_MODEL = 'member.MyUser'
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
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/


# Facebook
FB_APP_ID = config['facebook']['app_id']
FB_SECRET_CODE = config['facebook']['secret_code']
FB_APP_ACCESS_TOKEN = FB_APP_ID + '|' + FB_SECRET_CODE

SOCIAL_AUTH_FACEBOOK_SCOPE = ['email']
SOCIAL_AUTH_FACEBOOK_PROFILE_EXTRA_PARAMS = {
    'fields': 'id, name, email'
}

# Email
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = config['email']['EMAIL_HOST_USER']
EMAIL_HOST_PASSWORD = config['email']['EMAIL_HOST_PASSWORD']
SERVER_EMAIL = config['email']['EMAIL_HOST_USER']
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
