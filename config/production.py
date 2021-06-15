from logging.config import dictConfig

from config.default import *

SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://{user}:{pw}@{url}/{db}'.format(
    user='dbmasteruser',
    pw='7gfXY&haEj7CBZ1t8Z*.lM5#K;_>M.so',
    url='ls-c8544688aa3f6ec9c9ee7b69ca4b561f5d31c28a.culcdf0budht.ap-northeast-2.rds.amazonaws.com',
    db='flask_villvill2')
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = b'n\x86=+N\xff\x7f\xf8\xfd\xb5\xfdN\xfc\xe6?\x13'

dictConfig({
    'version': 1,
    'formatters': {
        'default': {
            'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
        }
    },
    'handlers': {
        'file': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(BASE_DIR, 'logs/villvill.log'),
            'maxBytes': 1024 * 1024 * 5,  # 5 MB
            'backupCount': 5,
            'formatter': 'default',
        },
    },
    'root': {
        'level': 'INFO',
        'handlers': ['file']
    }
})