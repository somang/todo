# config.py
import os
from pathlib import Path

from dotenv import load_dotenv

env_path = Path(".") / ".env"
load_dotenv(dotenv_path=env_path)

import secrets


class Settings:
    PROJECT_NAME: str = "todopractice"
    PROJECT_VERSION: str = "0.0.1"

    ## potentially, all db credentials can be included here...
    # but I'm going to use SQLite3 for convinence

    TEST_USER_EMAIL = "test@example.com"  # new


settings = Settings()
