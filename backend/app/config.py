# app/config.py

import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "default_secret_key")
    RATELIMIT_DEFAULT = "100 per minute"
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite:///ops_control.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
