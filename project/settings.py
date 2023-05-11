import os
import dj_database_url
from environs import Env

env = Env()
env.read_env()

DATABASES = {
    'default': dj_database_url.config
    (conn_max_age=600,
     conn_health_checks=True,
     )
}

INSTALLED_APPS = ['datacenter']

SECRET_KEY = env('SECRET_KEY')

DEBUG = env.bool('DEBUG', False)

ROOT_URLCONF = 'project.urls'

allowed_hosts_default = ['[::1]', '.localhost', '127.0.0.1']

ALLOWED_HOSTS = env.list('ALLOWED_HOSTS', allowed_hosts_default)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
    },
]


USE_L10N = True

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'Europe/Moscow'

USE_TZ = True

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'
