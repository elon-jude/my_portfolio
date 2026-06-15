import smtplib
import os 
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv 
from email.message import EmailMessage 
load_dotenv()
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
class Contact(BaseModel):
    name: str
    email: str
    message: str
@app.get("/")
def home():
    return {"message": "Backend is working"}
@app.post("/contact")
def contact(data: Contact):
    print("CONTACT REQUEST RECEIVED")
    print(data)
    try:
        msg = EmailMessage()
        msg["Subject"] = f"Portfolio Message from {data.name}"
        msg["From"] = os.getenv("EMAIL_ADDRESS")
        msg["To"] = os.getenv("EMAIL_ADDRESS")
        msg.set_content(
            f"""
Name: {data.name}
Email: {data.email}
Message:
{data.message}
"""
        )
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(
                os.getenv("EMAIL_ADDRESS"),
                os.getenv("EMAIL_PASSWORD")
            )
            smtp.send_message(msg)
        print("EMAIL SENT")
        return {"status": "success"}
    except Exception as e:
        print("EMAIL ERROR:", e)
        return {"status": "error", "message": str(e)}