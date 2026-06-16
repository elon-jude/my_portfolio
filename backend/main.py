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
@app.post("/contact")
def contact(data: Contact):
    print("CONTACT REQUEST RECEIVED")
    print(data)

    try:
        msg = EmailMessage()
        msg["Subject"] = f"Portfolio Message from {data.name}"
        msg["From"] = os.getenv("EMAIL_ADDRESS")
        msg["To"] = os.getenv("EMAIL_ADDRESS")
        msg["Reply-To"] = data.email

        msg.set_content(
            f"""
Name: {data.name}
Email: {data.email}

Message:
{data.message}
"""
        )

        with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
            smtp.ehlo()
            smtp.starttls()
            smtp.ehlo()

            smtp.login(
                os.getenv("EMAIL_ADDRESS"),
                os.getenv("EMAIL_PASSWORD")
            )

            smtp.send_message(msg)

        print("EMAIL SENT")
        return {"status": "success"}

    except Exception as e:
     import traceback
    print(traceback.format_exc())
    return {"status": "error", "message": str(e)}