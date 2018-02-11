from .base import *

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
      'ENGINE': 'django.db.backends.postgresql_psycopg2',
      'NAME': 'cryptobot',
      'USER': env('POSTGRES_USER'),
      'PASSWORD': env('POSTGRES_PASSWORD'),
      'HOST': env('POSTGRES_HOST'),
      'PORT': '',
    }
}
