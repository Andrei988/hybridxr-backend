from ..settings.common import *

# SECURITY WARNING: update this when you have the production host
ALLOWED_HOSTS = ['0.0.0.0', 'localhost']

CORS_ORIGIN_ALLOW_ALL = True
SECURE_SSL_REDIRECT = True

ALLOWED_HOSTS = [
    "localhost",
    "snurfer98.pythonanywhere.com",
    '127.0.0.1'
]

print("production")
print(SECURE_SSL_REDIRECT)
