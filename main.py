from fastapi import FastAPI

app: FastAPI = FastAPI(
    title="Cloud OTP Service",
    version="1.0",
)

otp_store = {}

class OTP:
    def __init__(self):
        self.id = None
        self.otp = None
        self.phone = None

    def generate_otp(self):
        import random
        self.otp = random.randint(100000, 999999)

        return self.otp

@app.get("/")
async def root():
    return {"message": f"Welcome to Cloud OTP Service! version {app.version}"}

@app.get("/get_otp")
async def get_otp(phone: str):
    otp = OTP()
    otp.generate_otp()
    otp_store[phone] = otp
    
    return {"message": f"Your OTP is {otp_store[phone].otp}"}

@app.get("/verify_otp")
async def verify_otp(phone: str, otp: int):
    if phone in otp_store and otp_store[phone].otp == otp:
        return {"message": "OTP Verified!"}
    else:
        return {"message": "Invalid OTP!"}