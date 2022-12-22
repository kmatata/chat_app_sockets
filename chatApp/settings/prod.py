from .base import *
import os

DEBUG = False   

ADMINS = [
    ('matata', '254khoi@gmail.com'),
]

ALLOWED_HOSTS = ['*']



DATABASES = {
    'default':{
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('POSTGRES_DB'),
        'USER': os.environ.get('POSTGRES_USER'),
        'PASSWORD': 'bernie101',
        'HOST': 'localhost',
        'PORT': 5432, 
    }
}