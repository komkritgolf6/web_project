import random
import string

def generate_otp(length=6):
    # สร้างรหัส OTP จากตัวอักษรและตัวเลข
    characters = string.ascii_letters + string.digits
    otp = ''.join(random.choice(characters) for _ in range(length))
    return otp

# เรียกใช้ฟังก์ชันสร้าง OTP
OTP_Code = generate_otp()
print("Your OTP is:", OTP_Code)
