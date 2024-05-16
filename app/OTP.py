import random
import string
from email.mime.text import MIMEText
import smtplib

def generate_otp(length=6):
    otp = ''.join(random.choice(string.digits) for _ in range(length))
    print("OTP:", otp)
    return otp

def send_otp_email(email, otp):
    sender_email = "komkritgolf6@gmail.com"
    sender_password = "pmto zwmm yptk mxbr"  # รหัสผ่านแอพลิเคชันที่คุณสร้างขึ้นเอง
    smtp_server = "smtp.gmail.com"  # เซิร์ฟเวอร์ SMTP ของ Gmail
    smtp_port = 587  # พอร์ต SMTP ของ Gmail
    print("test1",otp)
    message = MIMEText(f"OTP สำหรับการยืนยันของคุณคือ: {otp}")
    print("test2",otp)
    message['From'] = sender_email
    message['To'] = email
    message['Subject'] = "การยืนยัน OTP"
    print("test3",otp)
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, [email], message.as_string())
        server.quit()
        print("OTP sent successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")

# เมื่อต้องการสร้าง OTP ใหม่
new_otp = generate_otp()
print("Your new OTP is:", new_otp)

# ตรวจสอบว่าผู้ใช้ในฐานข้อมูลส่งคำขอเปลี่ยนรหัสผ่านหรือไม่
# หากมีคำขอ ให้ส่ง OTP ใหม่ไปยังอีเมลของผู้ใช้
user_email = "user@example.com"  # เปลี่ยนเป็นอีเมลของผู้ใช้จริง
send_otp_email(user_email, new_otp)
