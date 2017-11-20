from .base import *

SECRET_KEY = env('DJANGO_SECRET_KEY', default='!ol93fhqyec!5l9e32jc84_rj0)$!3fe22ghzz77)9i&m-wb3o')

DEFAULT_FILE_STORAGE = 'config.s3utils.MediaS3BotoStorage'
STATICFILES_STORAGE = 'config.s3utils.StaticS3BotoStorage'

ALLOWED_HOSTS = ['dj-connpass.herokuapp.com']


# AWS S3 Storage settings
AWS_ACCESS_KEY_ID = env('AWS_ACCESS_KEY_ID', default='AKIAIRAXS5Z6FXBNW2OQ')
AWS_SECRET_ACCESS_KEY = env('AWS_SECRET_ACCESS_KEY', default='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')
AWS_STORAGE_BUCKET_NAME = 'djconnpass-static'

AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME

STATIC_DIRECTORY = '/static/'
MEDIA_DIRECTORY = '/media/'
STATIC_URL = AWS_S3_CUSTOM_DOMAIN + STATIC_DIRECTORY
MEDIA_URL = AWS_S3_CUSTOM_DOMAIN + MEDIA_DIRECTORY

AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=86400',
}

AWS_LOCATION = 'static'

# Refer to this site regarding settings.
# https://simpleisbetterthancomplex.com/tutorial/2017/08/01/how-to-setup-amazon-s3-in-a-django-project.html
