import random
import string
# import time
from email.mime.text import MIMEText
import smtplib

def generate_otp(length=6):
    # สร้างรหัส OTP จากตัวอักษรและตัวเลข
    characters = string.ascii_letters + string.digits
    otp = ''.join(random.choice(characters) for _ in range(length))
    return otp

# เรียกใช้ฟังก์ชันสร้าง OTP
OTP_Code = generate_otp()
print("Your OTP is:", OTP_Code)

# ตั้งเวลาให้ OTP หมดอายุภายใน 5 นาที
# time.sleep(300)

# หลังจากผ่านไป 1 นาที ให้สร้าง OTP ใหม่
OTP_Code = generate_otp()
print("Your new OTP is:", OTP_Code)

def send_otp_to_email(email, otp):
    msg = MIMEText(f"Your OTP is: {otp}")
    msg['Subject'] = 'Your OTP Code'
    msg['From'] = 'komkritgolf6@gmail.com'
    msg['To'] = email
    print("otp email:", otp)
    with smtplib.SMTP('smtp.example.com') as server:
        server.login('your-email@example.com', 'your-password')
        server.sendmail('your-email@example.com', [email], msg.as_string())
        