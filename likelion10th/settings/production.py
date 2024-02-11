from likelion10th.settings.base import *
from decouple import config

DEBUG = True
# 추후 ip 추가
ALLOWED_HOSTS = [config("ALLOWED_HOST"), "www.likelion-hufs-seoul.com", "likelion-hufs-seoul.com", "13.124.241.62"]


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