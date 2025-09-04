# email_sender.py
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail, To
from config import SENDGRID_API_KEY, FROM_EMAIL, TEMPLATE_ID

sg = SendGridAPIClient(SENDGRID_API_KEY)

def send_email(name, email, user_id):
    """Send one email using SendGrid template"""
    message = Mail(
        from_email=FROM_EMAIL,
        to_emails=To(email, name=name),
    )

    message.template_id = TEMPLATE_ID
    message.dynamic_template_data = {
        "Name": name,
        "Id": user_id
    }

    try:
        response = sg.send(message)
        print(f"✅ Sent to {email} | Status: {response.status_code}")
    except Exception as e:
        print(f"❌ Failed for {email}: {e}")
