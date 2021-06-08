from config.default import *

SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'villvill.db'))
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = b'\xcfP\xd8\xe8\xe36]\x7f}F\x8f\xda\xabc\x95\xe3'