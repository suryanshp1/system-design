import smtplib, os
from email.message import EmailMessage
import json

def notification(message):
    try:
        message = json.loads(message)
        mp3_fid = message["mp3_fid"]
        sender_address = os.environ.get("GMAIL_ADDRESS")
        sender_password = os.environ.get("GMAIL_PASSWORD")
        receivers_address = message["username"]

        msg = EmailMessage()
        msg.set_content(f"mp3_file_id: {mp3_fid} is now ready to receive")
        msg["Subject"] = "MP# Download"
        msg["From"] = sender_address
        msg["To"] = receivers_address

        session = smtplib.SMTP("smtp.gmail.com", 587)
        session.starttls()
        session.login(sender_address, sender_password)
        session.send_message(msg, sender_address, receivers_address)
        session.quit()
        print("Mail Sent")
    except Exception as err:
        print(err)
        return err