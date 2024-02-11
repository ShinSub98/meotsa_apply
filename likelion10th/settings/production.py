from likelion10th.settings.base import *
from decouple import config

DEBUG = False
# 추후 ip 추가
ALLOWED_HOSTS = [ config("ALLOWED_HOST"), "www.likelion-hufs-seoul.com", "likelion-hufs-seoul.com" ]


import pymysql
pymysql.install_as_MySQLdb()

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', 
        'NAME': 'meotsa',
        'USER': 'root',
        'PASSWORD': config('.env에서 설정한 DB 패스워드'),
        'HOST': 'mysql_db',
        'PORT': '3306'
    }
}