# main.py
import time
from data_loader import load_participants
from email_sender import send_email

def main():
    participants = load_participants()

    for person in participants:
        send_email(person["Name"], person["Email"], person["Id"])
        time.sleep(0.2)  # add delay to avoid hitting SendGrid limits

if __name__ == "__main__":
    main()
