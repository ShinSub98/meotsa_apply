from likelion10th.settings.base import *
from decouple import config

DEBUG = True
# 추후 ip 추가
ALLOWED_HOSTS = [config("ALLOWED_HOST"), "http://hufs-likelion12.site", "hufs-likelion12.site" "13.124.241.62", "43.203.57.7"]


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