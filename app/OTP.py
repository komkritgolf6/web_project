import random
import string
from email.mime.text import MIMEText
import smtplib
import redis

# เชื่อมต่อ Redis Server
r = redis.Redis(host='localhost', port=6379, db=0)

def generate_otp(length=6):
    otp = ''.join(random.choice(string.digits) for _ in range(length))
    print("OTP finish :", otp)
    return otp

def send_otp_email(email, otp):
    sender_email = "komkritgolf6@gmail.com"
    sender_password = "pmto zwmm yptk mxbr"  # รหัสผ่านแอพลิเคชันที่คุณสร้างขึ้นเอง
    smtp_server = "smtp.gmail.com"  # เซิร์ฟเวอร์ SMTP ของ Gmail
    smtp_port = 587  # พอร์ต SMTP ของ Gmail
    message = MIMEText(f"OTP สำหรับการยืนยันของคุณคือ: {otp}")
    message['From'] = sender_email
    message['To'] = email
    message['Subject'] = "การยืนยัน OTP"
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, [email], message.as_string())
        server.quit()
        print("OTP sent successfully!")
        
        # เมื่อส่ง OTP สำเร็จ ให้เพิ่มข้อมูล email และ OTP ลงใน Redis
        add_data(email, otp)
    except Exception as e:
        print(f"An error occurred: {e}")

def add_data(email, otp):
    r.set(email, otp)
    print(f"Data added: email={email}, OTP={otp}")



