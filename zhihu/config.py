# -*- coding: utf-8 -*-
# Author: hkey
import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):   # 所有配置类的父类，通用的配置写在这里
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    FLASKY_MAIL_SUBJECT_PREFIX = '[Flasky]'
    FLASKY_MAIL_SENDER = 'Flasky Admin <xxx@126.com>'
    FLASKY_ADMIN = 'xxx@qq.com'

    @staticmethod
    def init_app(app):  # 静态方法作为配置的统一接口，暂时为空
        pass

class DevelopmentConfig(Config):    # 开发环境配置类
    DEBUG = True
    MAIL_SERVER = 'smtp.126.com'
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    MAIL_USERNAME = 'xxx@126.com'
    MAIL_PASSWORD = 'xxxxxx'
    SQLALCHEMY_DATABASE_URI = \
    'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')

class TestingConfig(Config):    # 测试环境配置类
    TESTING = True
    SQLALCHEMY_DATABASE_URI = \
        'sqlite:///' + os.path.join(basedir, 'data-test.sqlite')

class ProductionConfig(Config):     # 生产环境配置类
    SQLALCHEMY_DATABASE_URI = \
        'sqlite:///' + os.path.join(basedir, 'data.sqlite')

config = {  # config字典注册了不同的配置，默认配置为开发环境，本例使用开发环境
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
