from common import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Database
# https://docs.djangoproject.com/en/dev/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'd74a06uicjnde7',
        'USER': 'yucbnanslssylr',
        'PASSWORD': 'afpV3ppm_8REP4X2tDakxr_z0H',
        'HOST': 'ec2-23-21-96-129.compute-1.amazonaws.com',
        'PORT': '5432',
    }
}

FILE_SERVER_BASE_URL = "http://71.57.23.72:5000/nas_server/api/v1.0"

FILE_SERVER_URLS = {
    'BASE_DIR': "%s/directory/root" % FILE_SERVER_BASE_URL,
    'FILES': "%s/files" % FILE_SERVER_BASE_URL,
    'CONTENTS': "%s/directory" % FILE_SERVER_BASE_URL,
    'DELETES': "%s/files/deletes" % FILE_SERVER_BASE_URL,
    'CREATE': "%s/directory/create" % FILE_SERVER_BASE_URL,
    'DOWNLOADS': "%s/files/downloads" % FILE_SERVER_BASE_URL,

}

