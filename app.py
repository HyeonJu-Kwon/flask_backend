import os
import sys
from flask import Flask
from flask_migrate import Migrate
from db import db  # 데이터베이스 설정
from config import Config
from api.member_api import member_blueprint
from api.attendance_api import attendance_blueprint

# 현재 디렉토리를 Python 경로에 추가
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

app = Flask(__name__)
app.config.from_object(Config)  # ✅ config.py 적용

from dotenv import load_dotenv
load_dotenv()

# DB 및 Migrate 초기화 (한 번만 실행)
db.init_app(app)  # db 객체 초기화
migrate = Migrate(app, db)  # ✅ Flask-Migrate 설정 추가

# API 블루프린트 등록
app.register_blueprint(member_blueprint, url_prefix="/api")
app.register_blueprint(attendance_blueprint, url_prefix="/api")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)

@app.route("/", methods=["GET"])
def home():
    return "Flask 서버가 정상적으로 실행 중입니다!", 200
