from flask import Blueprint, jsonify

attendance_bp = Blueprint("attendance", __name__)

@attendance_bp.route("/test", methods=["GET"])
def test_route():
    return jsonify({"message": "Routes are working!"})
