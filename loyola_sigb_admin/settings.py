"""
Django settings for loyola_sigb project.

Generated by 'django-admin startproject' using Django 1.11.16.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os
import sys

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_ROOT = os.path.dirname(__file__)
sys.path.insert(0, os.path.join(BASE_DIR, 'apps'))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'xn$zgl@jlh-f1_oa6q-xgol@9h049^^pecu79@=l859g8ewt6e'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['biblioadmin.sjcuba.org','192.168.100.105']


# Application definition

INSTALLED_APPS = [
    'suit',
    'django.contrib.admin',
    'dal',
    'dal_select2',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    'corsheaders',
    'opac',
    'contabilidad',
    'novedades_bibliograficas',
    'registro_usuarios_biblioteca',
    'django_elasticsearch_dsl',
    'djoser',
    'rest_framework',
    'rest_framework.authtoken',
    'nested_admin',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',


    
]



ROOT_URLCONF = 'dedalos_loyola.urls'
LOGOUT_REDIRECT_URL = '/admin/login'
SUIT_CONFIG = {
'ADMIN_NAME': 'BIBLIOTECA DULCE MARÍA LOYNAZ'
}


ROOT_URLCONF = 'loyola_sigb_admin.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,"templates")],
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

WSGI_APPLICATION = 'loyola_sigb_admin.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'dedalos_loyola',
        'HOST' : '192.168.100.106' ,
        'USER' : 'edr' ,
        'PASSWORD' : 'H@bana2019*' ,
        'PORT' : '5432' ,
    }
}


CORS_ORIGIN_WHITELIST = (
    'biblioteca.sjcuba.org:3001',
    'biblioadmin-local.sjcuba.org:8085',
    'biblioadmin.sjcuba.org:8085',
    'biblioteca.sjcuba.org:9200',
)


CORS_ORIGIN_ALLOW_ALL = True 

DJOSER = {
    'SERIALIZERS': {
        
    },
}


REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
        
    ),

    'DEFAULT_FILTER_BACKENDS' : [
     'url_filter.integrations.drf.DjangoFilterBackend',
]

}

# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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

LANGUAGE_CODE = 'es-cu'

TIME_ZONE = 'America/Havana'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = '/uploads/'

STATICFILES_DIRS = [os.path.join(BASE_DIR,"static")]

#####################################
#CONFIG DE SERVIDORES DE BUSQUEDA   ################################################################
#####################################
ELASTICSEARCH_DSL={
'default': {
    'hosts': '192.168.100.106:9200',
    'sniff_on_start' : True   
  },
}

#Sincronizacion en Tiempo Real entre PostgreSQL y ElasticSearch
ELASTICSEARCH_DSL_SIGNAL_PROCESSOR = 'django_elasticsearch_dsl.signals.RealTimeSignalProcessor'

######################################################################################################
