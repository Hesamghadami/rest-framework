from config.settings import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

SECRET_KEY = 'django-insecure-^_0vkqce_!lzxkdic72%$c1i=r2(e2(bt#+bu&y_i^fttxrr@e'

DEBUG = True

ALLOWED_HOSTS = []






STATIC_ROOT = BASE_DIR.joinpath('/static')
MEDIA_ROOT = BASE_DIR.joinpath('media/')

STATICFILES_DIRS = [
    BASE_DIR/'static',
    BASE_DIR/'media',
]


EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'