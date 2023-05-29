import os

from dotenv import load_dotenv

load_dotenv()

MY_SQL_ADDON_URI            = os.getenv('MYSQL_ADDON_URI', default="")
MONGODB_ADDON_URI           = os.getenv('MONGODB_ADDON_URI', default="")
MONGODB_ADDON_DB            = os.getenv('MONGODB_ADDON_DB', default="")
ALGORITHM                   = os.getenv("ALGORITHM", default="")
SECRET_KEY                  = os.getenv("SECRET_KEY", default="")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", default=""))