# ในไฟล์ models.py

from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(200), unique=True,nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=True)
    otp = db.Column(db.String(200), nullable=True)
    
    

def create_table():
    db.create_all()
