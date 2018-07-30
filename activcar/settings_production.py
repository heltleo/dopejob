from activcar.settings import *

import dj_database_url

DATABASES['default'] = dj_database_url.config()

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

ALLOWED_HOSTS = ['*',]

DEBUG = config('DEBUG', cast=bool)

STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'

ADMINS = (
    ('Délita', 'delita.makanda@gmail.com'),
)

SEND_BROKEN_LINK_EMAILS=True

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

EMAIL_HOST = config('EMAIL_HOST')
EMAIL_HOST_USER = config('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')
EMAIL_PORT = config('EMAIL_PORT')
EMAIL_USE_TLS = config('EMAIL_USE_TLS')

SERVER_EMAIL = config('SERVER_EMAIL')


# Static files deploy in S3 AWS
AWS_ACCESS_KEY_ID = config('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = config('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = config('AWS_STORAGE_BUCKET_NAME')
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=86400',
}

# AWS_LOCATION = 'static'

# STATIC_URL = 'https://%s/%s/' % (AWS_S3_CUSTOM_DOMAIN, AWS_LOCATION)
# STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

# media upload files on S3 AWS

DEFAULT_FILE_STORAGE = 'activcar.storage_backends.MediaStorage'

# Memcache

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.PyLibMCCache',
        'TIMEOUT': None,
        'LOCATION': config('MEMCACHIER_SERVERS'),
        'OPTIONS': {
            'binary': True,
            'username': config('MEMCACHIER_USERNAME'),
            'password': config('MEMCACHIER_PASSWORD'),
            'behaviors': {
                # Enable faster IO
                'no_block': True,
                'tcp_nodelay': True,
                # Keep connection alive
                'tcp_keepalive': True,
                # Timeout settings
                'connect_timeout': 2000, # ms
                'send_timeout': 750 * 1000, # us
                'receive_timeout': 750 * 1000, # us
                '_poll_timeout': 2000, # ms
                # Better failover
                'ketama': True,
                'remove_failed': 1,
                'retry_timeout': 2,
                'dead_timeout': 30,
            }
        }
    }
}

# Cron task redis

CELERY_BROKER_URL = 'redis://redis:6379'
CELERY_RESULT_BACKEND = 'redis://redis:6379'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
