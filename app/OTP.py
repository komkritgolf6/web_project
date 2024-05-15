import random
import string
import time

def generate_otp(length=6):
    # สร้างรหัส OTP จากตัวอักษรและตัวเลข
    characters = string.ascii_letters + string.digits
    otp = ''.join(random.choice(characters) for _ in range(length))
    return otp

# เรียกใช้ฟังก์ชันสร้าง OTP
OTP_Code = generate_otp()
print("Your OTP is:", OTP_Code)

# ตั้งเวลาให้ OTP หมดอายุภายใน 5 นาที
time.sleep(300)

# หลังจากผ่านไป 1 นาที ให้สร้าง OTP ใหม่
OTP_Code = generate_otp()
print("Your new OTP is:", OTP_Code)
