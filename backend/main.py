import os
import smtplib
from email.message import EmailMessage

from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel


load_dotenv()

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Contact(BaseModel):
    name: str
    email: str
    message: str


EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")


@app.get("/")
def home():
    return {"message": "Backend is working"}


@app.post("/contact")
def contact(data: Contact):
    if not EMAIL_ADDRESS or not EMAIL_PASSWORD:
        raise HTTPException(
            status_code=500,
            detail="Email settings are not configured on the server.",
        )

    try:
        msg = EmailMessage()
        msg["Subject"] = f"Portfolio Message from {data.name}"
        msg["From"] = EMAIL_ADDRESS
        msg["To"] = EMAIL_ADDRESS
        msg["Reply-To"] = data.email

        msg.set_content(
            f"""
Name: {data.name}
Email: {data.email}
Message:
{data.message}
"""
        )

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            smtp.send_message(msg)

        return {"status": "success", "message": "Message sent successfully."}

    except smtplib.SMTPAuthenticationError as exc:
        raise HTTPException(
            status_code=500,
            detail="Email authentication failed. Check your Gmail app password.",
        ) from exc

    except smtplib.SMTPException as exc:
        raise HTTPException(
            status_code=502,
            detail="Could not send the email right now. Please try again later.",
        ) from exc
