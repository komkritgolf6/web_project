from flask import Blueprint, render_template, jsonify
from flask_jwt_extended import jwt_required

bp = Blueprint('routes', __name__)

@bp.route('/')
def home():
    print("ok")
    return render_template('login.html')

@bp.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    return jsonify(message="This is a protected route")

@bp.route('/register')
def regis():
    print("ok")
    return render_template('Register.html')


