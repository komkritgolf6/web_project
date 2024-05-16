import random
import string
from email.mime.text import MIMEText
import smtplib

def generateotp(length=6):
    otp = ''.join(random.choice(string.digits) for  in range(length))
    print(otp)
    return otp

def send_email(email, otp):
    sender_email = "komkritgolf6@gmail.com"
    sender_password = "pmto zwmm yptk mxbr"  # รหัสผ่านแอพลิเคชันที่คุณสร้างขึ้นเอง
    smtp_server = "smtp.gmail.com"  # เซิร์ฟเวอร์ SMTP ของ Gmail
    smtp_port = 587  # พอร์ต SMTP ของ Gmail

    otp_str = str(otp)  # แปลงค่า otp เป็น string
    print("kuy", otp_str)
    message = MIMEText(f"Your OTP is: {otp_str}")

    message['From'] = sender_email
    message['To'] = email
    message['Subject'] = "Your OTP Code"

    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, [email], message.as_string())
        server.quit()
        print("OTP sent successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")

def send_otp_to_email(email, otp):
    send_email(email, otp)
    print("OTP sent to email:", email)
new_otp = generate_otp()
print("Your new OTP is:", new_otp)
user_email = "user@example.com"  # เปลี่ยนเป็นอีเมลของผู้ใช้จริง
send_otp_to_email(user_email, new_otp)