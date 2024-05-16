import random
import string
import time
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def generate_otp(length=6):
    otp = ''.join(random.choice(string.digits) for _ in range(length))
    return otp

def send_email(receiver_email, otp):
    sender_email = "your_email@example.com"
    sender_password = "your_password"

    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = receiver_email
    message['Subject'] = "Your OTP"

    body = f"Your OTP is: {otp}"
    message.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP('smtp.example.com', 587)
        server.starttls()
        server.login(sender_email, sender_password)
        text = message.as_string()
        server.sendmail(sender_email, receiver_email, text)
        server.quit()
        print("OTP sent successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")

def reset_otp(receiver_email):
    OTP_Code = generate_otp()
    print("Your new OTP is:", OTP_Code)
    send_email(receiver_email, OTP_Code)

# ตั้งเวลาให้ OTP หมดอายุภายใน 5 นาที
# time.sleep(300)

# รีเซ็ต OTP ใหม่
# reset_otp(receiver_email)
# เปลี่ยนOTPจากตัวอักษรเป็นตัวเลข6ตัว