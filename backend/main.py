from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from pydantic import BaseModel

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
    print("New Message Received")
    print(f"Name: {data.name}")
    print(f"Email: {data.email}")
    print(f"Message: {data.message}")

    return {"status": "success"}