from .base import *

import dj_database_url

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Farhan Syed', 'nearhan@gmail.com'),
)

MANAGERS = ADMINS
DATABASES = {}
DATABASES['default'] = dj_database_url.config()

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

#grab secert key from env variable
SECRET_KEY = os.environ['SECRET_KEY']
