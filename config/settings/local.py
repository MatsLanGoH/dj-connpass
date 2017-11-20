from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('DJANGO_SECRET_KEY', default='!ol93fhqyec!5l9e32jc84_rj0)$!3fe22ghzz77)9i&m-wb3o')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env.bool('DJANGO_DEBUG', default=True)

ALLOWED_HOSTS = ['localhost', '0.0.0.0', '10.0.1.41', '172.31.9.114']