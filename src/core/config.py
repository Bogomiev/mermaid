import os
import pathlib

from starlette.datastructures import CommaSeparatedStrings, Secret

AUTH_SERVER = ''
JWT_TOKEN_PREFIX = "Token"
ACCESS_TOKEN_EXPIRE_MINUTES = 60  # one hour
REFRESH_TOKEN_EXPIRE_MINUTES = 60 * 24 * 3  # 3 days

SECRET_KEY = Secret(os.getenv("SECRET_KEY", "secret key for project"))

PROJECT_NAME = os.getenv("MERMAID", "auto-oreder 'Mermaid'")
ALLOWED_HOSTS = CommaSeparatedStrings(os.getenv("ALLOWED_HOSTS", ""))
DATABASE_URL = "postgresql://postgres:+-@192.168.1.144/mermaid"
ROOT_DIR = pathlib.Path(__file__).parent.absolute().parent.parent

DB_NAME = 'mermaid'
