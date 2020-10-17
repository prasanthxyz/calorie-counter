from .settings import *

SECRET_KEY = os.getenv('SECRET_KEY')
DEBUG = os.getenv('DEBUG_MODE') == 'True'
ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS').split()

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'ccdb',
        'USER': 'dbadmin@calorie-counter-db',
        'PASSWORD': os.getenv('DB_PASS'),
        'HOST': 'calorie-counter-db.mysql.database.azure.com',
        'PORT': '3306',
    }
}
