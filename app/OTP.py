import random
import string
from email.mime.text import MIMEText
import smtplib
from email.mime.multipart import MIMEMultipart

def generate_otp(length=6):
    otp_code = ''.join(random.choice(string.digits) for _ in range(length))
    print("OTP:", otp_code)
    return otp_code

def send_otp_email(email, otp_code):
    sender_email = "komkritgolf6@gmail.com"
    sender_password = "pmto zwmm yptk mxbr"  # รหัสผ่านแอพลิเคชันที่คุณสร้างขึ้นเอง
    smtp_server = "smtp.gmail.com"  # เซิร์ฟเวอร์ SMTP ของ Gmail
    smtp_port = 587  # พอร์ต SMTP ของ Gmail

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = email
    msg['Subject'] = "การยืนยัน OTP"

    print("test1", otp_code)
    body = f"OTP สำหรับการยืนยันของคุณคือ: {otp_code}"
    msg.attach(MIMEText(body, 'plain'))


    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()


    server.login(sender_email, sender_password)


    server.sendmail(sender_email, email, msg.as_string())


    server.quit()

