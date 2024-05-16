import random
import string
# import time
from email.mime.text import MIMEText
import smtplib

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
        