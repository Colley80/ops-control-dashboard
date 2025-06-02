# backend/app/config.py

import os
from dotenv import load_dotenv

# Load .env variables
load_dotenv()

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "defaultsecret")
    RATE_LIMIT_DEFAULT = os.getenv("RATE_LIMIT_DEFAULT", "5 per minute")
