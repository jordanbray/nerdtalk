"""
Django settings for nerdtalk project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

import ldap
from django_auth_ldap.config import LDAPSearch

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

##
## CHANGE ALL THESE SETTINGS
##

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'generate_a_new_secret_key_at_some_point_please_or_you_will_get_hacked'


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

# The LDAP host.  Leave blank for localhost (or type it in)
AUTH_LDAP_SERVER_URI = 'ldap://10.8.0.14/'

# The user to use to search the ldap server.  Leave blank to do so anoymously
AUTH_LDAP_BIND_DN = ""
# The password to use to search te ldap server
AUTH_LDAP_BIND_PASSWORD = ""

# Where in the tree are the users?
AUTH_LDAP_USER_SEARCH = LDAPSearch("ou=People,dc=nerdtalk,dc=org", ldap.SCOPE_SUBTREE, "(uid=%(user)s)")

# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases
# https://django-mongodb-engine.readthedocs.org/en/latest/

DATABASES = {
    'default': {
        'ENGINE': 'django_mongodb_engine',
        'NAME': 'nerdtalk',
    }
}

##
## DONE CHANGING SETTINGS (hopefully...)
##

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'menu',
    'nerdtalk',
    'auth',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'nerdtalk.urls'

WSGI_APPLICATION = 'nerdtalk.wsgi.application'


# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

AUTHENTICATION_BACKENDS = ( 'django_auth_ldap.backend.LDAPBackend',
                            'django.contrib.auth.backends.ModelBackend')

