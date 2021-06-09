from config.default import *

SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://{user}:{pw}@{url}/{db}'.format(
    user='dbmasteruser',
    pw='-^gQ!rTSQnjSpiw00gpY<cSR,a.(dIRR',
    url='ls-74b32ab5c29f834d698aad3735e1b597d4622a74.culcdf0budht.ap-northeast-2.rds.amazonaws.com',
    db='flask_villvill')

SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = b'\xcfP\xd8\xe8\xe36]\x7f}F\x8f\xda\xabc\x95\xe3'