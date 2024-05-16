from flask import Blueprint, request, jsonify, redirect, url_for, render_template
from flask_jwt_extended import create_access_token
from werkzeug.security import check_password_hash, generate_password_hash
from app.models import User
from app import db
from .OTP import generate_otp, send_otp_email
import redis

r = redis.Redis(host='localhost', port=6379, db=0)
bp = Blueprint('auth', __name__)

@bp.route('/login', methods=['POST'])
def login():
    # data = request.get_json()
    # username = data.get('username')
    # password = data.get('password')

    # username จะได้จาก form
    # password จะได้จาก form
    username = request.form.get("username")
    password = request.form.get("password")
    print(username)
    print(password)
    #select db ด้วย user
    user = User.query.filter_by(username=username).first()
    # 161145Golf
    #ถ้า user = true และ เช็คพาสเวิร์ดที่เข้ารหัส = true
    if user and check_password_hash(user.password, password):
        print("Received username:", username)
        print("Received password:", password)
        print("ok")
        #get otp และ send mail
        
        send_otp_email(user.email, generate_otp())
        
        # Redirect to otp.html upon successful login
        return redirect("/otp", code=302)
    
    # print("Invalid username or password")  
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

@bp.route('/otp')
def otp():
    return render_template('otp.html')


@bp.route('/verify_token')
def verify_token():
    print("verify_token")
    otp = request.args.get("otp")
    print(otp)
    
    # ตรวจสอบว่า OTP ที่รับมาตรงกับข้อมูลใดใน Redis หรือไม่
    for key in r.keys():
        if r.get(key).decode('utf-8') == otp:
            access_token = create_access_token(identity=key.decode('utf-8'))  # ใช้ key เป็น identity
            return jsonify({"msg": "Login Success", "access_token": access_token})
    
    # ถ้าไม่พบ OTP ที่ตรงกัน
    return jsonify({"msg": "Invalid OTP"})