from activcar.settings import *

import dj_database_url

DATABASES['default'] = dj_database_url.config()

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

ALLOWED_HOSTS = ['*',]

DEBUG = False

STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'

ADMINS = (
    ('Délita', 'delita.makanda@gmail.com'),
)

SEND_BROKEN_LINK_EMAILS=True

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

EMAIL_PORT = 587
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_USE_TLS = True
SERVER_EMAIL = ''
EMAIL_HOST = ''
SERVER_EMAIL = EMAIL_HOST_USER
