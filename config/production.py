from logging.config import dictConfig

from config.default import *

SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://{user}:{pw}@{url}/{db}'.format(
    user='dbmasteruser',
    pw='-^gQ!rTSQnjSpiw00gpY<cSR,a.(dIRR',
    url='ls-74b32ab5c29f834d698aad3735e1b597d4622a74.culcdf0budht.ap-northeast-2.rds.amazonaws.com',
    db='flask_villvill')
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