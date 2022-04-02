from .base import *
import mimetypes

mimetypes.add_type("text/css", ".css", True)

SECRET_KEY = 'abc'

DEBUG = True

ALLOWED_HOSTS = ['*']

STATIC_URL = '/static/'

STATIC_ROOT = BASE_DIR / 'staticfiles'

STATICFILES_DIRS = [
    BASE_DIR / "static",
]

MEDIA_URL = '/media/'

MEDIA_ROOT = BASE_DIR / 'media'