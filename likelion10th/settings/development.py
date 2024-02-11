from likelion10th.settings.base import *

DEBUG = True

ALLOWED_HOSTS = ["*"]

# LOGGING = {
#     'version' : 1,
#     'disable_existing_loggers': False,
#     'handlers' : {
#         'console': {
#             'level': 'DEBUG',
#             'class': 'logging.StreamHandler',
#         }
#     },
#     'loggers': {
#         'django.db.backends': {
#             'handlers': ['console'],
#             'level': 'DEBUG',
#         },
#     }
# }
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOW_CREDENTIALS = True

import pymysql
pymysql.install_as_MySQLdb()

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', 
        'NAME': 'meotsa_apply',
        'USER': 'root',
        'PASSWORD': config('MYSQL_ROOT_PASSWORD'),
        'HOST': 'mysql_db',
        'PORT': '3306'
    }
}