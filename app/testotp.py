import random
import string
import time
import smtplib
import sqlite3
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def generate_otp(length=6):
    otp = ''.join(random.choice(string.digits) for _ in range(length))
    return otp

def send_email(receiver_email, sender_email, sender_password, otp):
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

def reset_otp(receiver_email, sender_email, sender_password):
    OTP_Code = generate_otp()
    print("Your new OTP is:", OTP_Code)
    send_email(receiver_email, sender_email, sender_password, OTP_Code)

# การเชื่อมต่อกับฐานข้อมูล SQLite
conn = sqlite3.connect('app4.db')
cursor = conn.cursor()

# ดึงข้อมูลอีเมลผู้รับ
cursor.execute("SELECT email FROM recipients WHERE id = 1")  # เรียกใช้ ID ของผู้รับ
receiver_email = cursor.fetchone()[0]

# ดึงข้อมูลการตั้งค่าอีเมลผู้ส่ง
cursor.execute("SELECT email, password FROM sender_emails WHERE id = 1")  # เรียกใช้ ID ของผู้ส่ง
sender_email, sender_password = cursor.fetchone()

# ส่ง OTP
send_email(receiver_email, sender_email, sender_password, generate_otp())

# รอ 5 นาที
time.sleep(300)

# รีเซ็ต OTP ใหม่
reset_otp(receiver_email, sender_email, sender_password)

# ปิดการเชื่อมต่อกับฐานข้อมูล
conn.close()
