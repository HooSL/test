from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
import json

#SQLALCHEMY_DATABASE_URL = "mysql+pymysql://testuser:1026@dbfoot.cnsfwt1k1yag.ap-northeast-2.rds.amazonaws.com:3306/test"
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SECRET_FILE = os.path.join(BASE_DIR, 'secrets.json')
secrets = json.loads(open(SECRET_FILE).read())
DB = secrets["DB"]

SQLALCHEMY_DATABASE_URL = f"mysql+pymysql://{DB['user']}:{DB['password']}@{DB['host']}:{DB['port']}/{DB['database']}?charset=utf8"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

#dbfoot.cnsfwt1k1yag.ap-northeast-2.rds.amazonaws.com