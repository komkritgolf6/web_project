from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token
from werkzeug.security import check_password_hash, generate_password_hash
from app.models import User
from app import db

bp = Blueprint('auth', __name__)

@bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    user = User.query.filter_by(username=username).first()
    if user and check_password_hash(user.password, password):
        access_token = create_access_token(identity=username)
        print("Received username:", username)  # สั่งปริ้น username ที่รับมา
        print("Received password:", password)  # สั่งปริ้น password ที่รับมา
        print("ok")  # สั่งปริ้น password ที่รับมา
        return jsonify({"msg": "Login successful", "access_token": access_token})
    print("Invalid username or password")  # สั่งปริ้นถ้าชื่อผู้ใช้หรือรหัสผ่านไม่ถูกต้อง
    return jsonify({"msg": "Bad username or password"}), 401




@bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = generate_password_hash(data.get('password'))
    user = User(username=username, password=password)
    db.session.add(user)
    db.session.commit()
    return jsonify({"msg": "User registered"}), 201
