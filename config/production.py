from config.default import *

SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'villvill.db'))
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = b'n\x86=+N\xff\x7f\xf8\xfd\xb5\xfdN\xfc\xe6?\x13'