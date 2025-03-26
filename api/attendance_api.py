 
from flask import request, Blueprint
from flask_restful import Resource, Api
from db import db

attendance_blueprint = Blueprint('attendance_api', __name__)
attendance_api = Api(attendance_blueprint)

class MarkAttendance(Resource):
    def post(self):
        data = request.get_json()
        user_id = data.get("user_id")
        status = data.get("status")  # 출석, 지각, 결석

        if not user_id or status not in ["출석", "지각", "결석"]:
            return {"message": "Invalid data"}, 400

        new_attendance = Attendance(user_id=user_id, status=status)
        db.session.add(new_attendance)
        db.session.commit()

        return {"message": "Attendance marked successfully"}, 201

attendance_api.add_resource(MarkAttendance, '/attendance')
