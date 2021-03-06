from .settings_common import *

DEBUG = False

ALLOWED_HOSTS = [os.environ.get('ALLOWED_HOSTS')]

STATIC_ROOT = '/usr/share/nginx/html/static'
MEDIA_ROOT = '/usr/share/nginx/html/media'

AWS_SES_ACCESS_KEY_ID = os.environ.get('AWS_SES_ACCESS_KEY_ID')
AWS_SES_SECRET_ACCESS_KEY = os.environ.get('AWS_SES_SEACRET_ACCESS_KEY')
EMAIL_BACKEND = 'django_ses.SESBackend'

LOGGING = {
     'version': 1,
     'disable_existing_logger': False,

     'loggers': {
         'django':{
             'handlers':['file'],
             'level':'INFO',
         },
         'diary': {
             'handlers':['file'],
             'level': 'INFO',
         },
     },

     'handlers': {
         'file': {
             'level': 'INFO',
             'class': 'logging.handlers.TimedRotatingFileHandler',
             'filename': os.path.join(BASE_DIR, 'logs/django.log'),
             'formatter': 'prod',
             'when': 'D',
             'interval': 1,
             'backupCount': 7,
         },
     },

     'formatters': {
         'prod': {
             'format': '\t'.join([
                 '%(asctime)s',
                 '[%(levelname)s]',
                 '%(pathname)s(Line:%(lineo)d)',
                 '%(message)s'
             ])
         },
     }
 }

#セキュリティ設定
SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True

SECURE_CONTENT_TYPE_NOSNIFF = True

SECURE_BROWSER_XSS_FILTER = True

SECURE_SSL_REDIRECT = True

SESSION_COOKIE_SECURE = True

CSRF_COOKIE_SECURE = True

X_FRAME_OPTIONS = 'DENY'

SECURE_HSTS_PRELOAD = True