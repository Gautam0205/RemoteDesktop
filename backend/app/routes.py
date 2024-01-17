from flask import jsonify, request
from app import app, db
from app.models import User


@app.route("/", methods=["GET"])
def index():
    return jsonify("Hello, Remote Desktop App!")


@app.route("/add_test_data", methods=["POST"])
def add_test_data():
    """Endpoint to add test data to the User model."""
    data = request.json
    new_user = User(
        ip_address=data["ip_address"],
        name=data["name"],
        desk_id=data["desk_id"],
        password=data["password"],
        is_online=data.get("is_online", True),
        contacts=data.get("contacts", {}),
    )

    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "Test data added successfully"}), 201
