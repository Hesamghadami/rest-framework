from config.settings import *
import os
import dotenv
dotenv.load_dotenv("/home/hesamblo/project/env/env.env")


CSRF_COOKIE_SECURE = True
CSRF_COOKIE_SAMESITE = 'Strict'
SESSION_COOKIE_SECURE = True
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_SSL_REDIRECT = True
X_FRAME_OPTIONS = 'DENY'
SECURE_HSTS_SECONDS = 15768000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
CSP_DEFAULT_SRC = ("'none'",)
CSP_STYLE_SRC = ("'self'",)
CSP_SCRIPT_SRC = ("'self'",)
CSP_FONT_SRC = ("'self'",)
CSP_IMG_SRC = ("'self'",)

SECRET_KEY = os.environ.get("SECRET_KEY")

DEBUG = False
ALLOWED_HOSTS = ['hesamblog.ir', 'www.hesamblog.ir']

SITE_ID = 1

STATIC_ROOT = '/home/hesamblo/public_html/static'
MEDIA_ROOT = '/home/hesamblo/public_html/media'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

EMAIL_HOST = 'mail.hesamblog.ir'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = os.environ.get('EMAIL_SMTP_USER')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_SMTP_PASSWORD')
DEFAULT_FROM_EMAIL = os.environ.get('EMAIL_SMTP_USER')



DATABASES = {
   'default': {
     'ENGINE': 'django.db.backends.mysql',
        'NAME': os.getenv("DATABASE_NAME"),
        'USER': os.getenv("DATABASE_USERNAME"),
        'PASSWORD': os.getenv("DATABASE_PASSWORD"),
        'HOST': '127.0.0.1',
        'PORT': '3306',
        }
    }

