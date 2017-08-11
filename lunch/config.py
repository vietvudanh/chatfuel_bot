import logging
import os

CURRENT = os.path.dirname(os.path.realpath(__file__))
APP_DIR = os.path.join(CURRENT, os.pardir)


class Config():
    DEBUG = False


class DevConfig(Config):
    DEBUG = True
