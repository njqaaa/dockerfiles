"""
    jumpserver.config
    ~~~~~~~~~~~~~~~~~

    Jumpserver project setting file

    :copyright: (c) 2014-2016 by Jumpserver Team.
    :license: GPL v2, see LICENSE for more details.
"""
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LOG_DIR = os.path.join(BASE_DIR, 'logs')


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or '2vym+ky!997d5kkcc64mnz06y1mmui3lut#(^wd=%s_qj$1%x'

    DISPLAY_PER_PAGE = 25
    SITE_URL = os.environ.get('SITE_URL') or 'http://localhost'
    DOMAIN_NAME = os.environ.get('DOMAIN_NAME') or 'jumpserver.org'
    # Django security setting, if your disable debug model, you should setting that
    ALLOWED_HOSTS = ['*']
    DEBUG = os.environ.get('DEBUG') or True
    LOG_LEVEL = 'DEBUG'
    HTTP_BIND_HOST = '0.0.0.0'
    HTTP_LISTEN_PORT = 80

    REDIS_HOST = os.environ.get('REDIS_HOST') or '127.0.0.1'
    REDIS_PORT = os.environ.get('REDIS_PORT') or '6379'
    REDIS_PASSWORD = os.environ.get('REDIS_PASSWORD') or ''
    BROKER_URL = 'redis://%(password)s%(host)s:%(port)s/3' % {
        'password': REDIS_PASSWORD,
        'host': REDIS_HOST,
        'port': REDIS_PORT,
    }

    TOKEN_EXPIRATION = 3600
    SESSION_COOKIE_AGE = 3600*24
    CAPTCHA_TEST_MODE = False

    USER_GUIDE_URL = ''

    def __init__(self):
        pass

    def __getattr__(self, item):
        return None


class ProductionConfig(Config):
    DEBUG = True
    DB_ENGINE = 'mysql'
    DB_HOST = os.environ.get('DB_HOST') or '127.0.0.1'
    DB_PORT = os.environ.get('DB_PORT') or '3306'
    DB_USER = os.environ.get('DB_USER') or 'root'
    DB_PASSWORD = os.environ.get('DB_PASSWORD') or 'root'
    DB_NAME = os.environ.get('DB_NAME') or 'jumpserver_db'
    EMAIL_HOST = os.environ.get('EMAIL_HOST') or 'smtp.qq.com'
    EMAIL_PORT = int(os.environ.get('EMAIL_PORT', 465))
    EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER') or 'admin'
    EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD') or 'somepasswrd'
    EMAIL_USE_SSL = True if EMAIL_PORT == 465 else False
    EMAIL_USE_TLS = True if EMAIL_PORT == 587 else False
    EMAIL_SUBJECT_PREFIX = os.environ.get('EMAIL_SUBJECT_PREFIX') or '[Jumpserver] '


config = {
    'production': ProductionConfig,
    'default': ProductionConfig,
}

env = 'production'
