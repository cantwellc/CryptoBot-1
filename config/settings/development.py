from .base import *


DEBUG = env.bool('DJANGO_DEBUG', True)

DATABASES = {
    'default': {
      'ENGINE': 'django.db.backends.postgresql_psycopg2',
      'NAME': 'cryptobot',
      'USER': 'root',
      'HOST': 'localhost',
      'PORT': '',
    }
}
