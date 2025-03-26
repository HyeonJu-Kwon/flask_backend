import os
from dotenv import load_dotenv

DB_USER = "flask_user"
DB_PASSWORD = "Ghkdlxla1234!"
DB_HOST = "your-ec2-public-ip"  # 또는 EC2 내부 IP
DB_PORT = "3306"
DB_NAME = "club_database"

# .env 파일 로드
load_dotenv()

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "my_secret_key")
    SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
