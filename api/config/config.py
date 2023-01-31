import os
from decouple import config
class Config:
    SECRET_KEY = config('SECRET_KEY','secret')

class Devconfig(Config):
    DEBUG = config('DEBUG',cast=bool)

class Testconfig(Config):
    pass

class Prodconfig(Config):
    pass

config_dict = {
    'dev':Devconfig,
    'test':Testconfig,
    'prod':Prodconfig
}
