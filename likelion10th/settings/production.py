from likelion10th.settings.base import *
from decouple import config

DEBUG = False
# 추후 ip 추가
ALLOWED_HOSTS = [ config("ALLOWED_HOST"), "www.likelion-hufs-seoul.com", "likelion-hufs-seoul.com" ]


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        "NAME": config("DB_NAME"),
        "USER": config("DB_USER"),
        "PASSWORD": config("DB_PASSWORD"),
        "HOST": config("DB_HOST"),
        "PORT": config("DB_PORT"),
        "OPTIONS": {"init_command": "SET sql_mode='STRICT_TRANS_TABLES'"},
    }
}