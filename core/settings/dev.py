from .base import *

STATICFILES_DIRS = [BASE_DIR / '../static/']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / '../db.sqlite3',
    }
}
