import os
from re import DEBUG
from flask import Flask

class Config(object):
    # ...
    DEBUG = True

    SECRET_KEY=os.environ.get("SECRET_KEY", "dev")
    SECURITY_PASSWORD_HASH = "pbkdf2_sha512"
    SECURITY_PASSWORD_SALT = "fsdfdfsdfdfsdafds"


    SQLALCHEMY_DATABASE_URI= "postgresql://alan:3571@localhost:5432/fias"
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    # SQLALCHEMY_ECHO = True