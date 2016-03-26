from common import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

FILE_SERVER_BASE_URL = "http://127.0.0.1:5000/nas_server/api/v1.0"
#FILE_SERVER_BASE_URL = "http://71.57.23.72:5000/nas_server/api/v1.0"

FILE_SERVER_URLS = {
    'BASE_DIR': "%s/directory/root" % FILE_SERVER_BASE_URL,
    'FILES': "%s/files" % FILE_SERVER_BASE_URL,
    'CONTENTS': "%s/directory" % FILE_SERVER_BASE_URL,
    'DELETES': "%s/files/deletes" % FILE_SERVER_BASE_URL,
    'CREATE': "%s/directory/create" % FILE_SERVER_BASE_URL,
    'DOWNLOADS': "%s/files/downloads" % FILE_SERVER_BASE_URL,

}