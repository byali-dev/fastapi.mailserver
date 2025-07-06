from fastapi import FastAPI, Form
from fastapi.middleware.cors import CORSMiddleware
from email.message import EmailMessage
from dotenv import load_dotenv
import smtplib, os

app = FastAPI()

origins = [
    "https://byali.tech",       # Production site
    "https://www.byali.tech",       # Production site
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["POST"],
    allow_headers=["*"],  # Can be tightened later if needed
)

@app.post("/send-email")
async def send_email(
    name: str = Form(...),
    email: str = Form(...),
    message: str = Form(...)
):
    load_dotenv() 
    msg = EmailMessage()
    msg["Subject"] = f"New Contact from {name}"
    msg["From"] = os.getenv("EMAIL_FROM")
    msg["To"] = os.getenv("EMAIL_TO")
    msg.set_content(f"From: {name} <{email}>\n\n{message}")

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(os.getenv("EMAIL_USER"), os.getenv("EMAIL_PASS"))
        smtp.send_message(msg)

    return {"status": "success", "message": "Email sent."}
