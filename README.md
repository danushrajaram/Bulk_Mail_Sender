# 📧 Bulk Mail Sender (SendGrid + Python)

A simple Python project to send **bulk personalized emails** (e.g., event invites, confirmations, newsletters) to participants using **SendGrid’s dynamic email templates**.  

---

## ✨ Features
- Send bulk emails from a **CSV/Excel list** of participants  
- Supports **dynamic template data** (e.g., Name, ID)  
- Configurable via `config.py`  
- Handles **500+ participants** with rate-limit safety  
- Lightweight & modular project structure  

---

## 📂 Project Structure
 ```bash
bulk_mailer/
│── config.py # Configurations (API key, template ID, etc.)
│── email_sender.py # Core email sending logic
│── data_loader.py # Loads CSV/Excel participant list
│── main.py # Entry point (loops over participants)
│── participants.csv # Example participants list
│── requirements.txt # Dependenc
```


## ⚙️ Setup & Installation
**Clone the repo**  
   ```bash
   git clone https://github.com/your-username/bulk-mailer.git
   cd bulk-mailer
```
Create a virtual environment (optional but recommended)
   ```bash
python -m venv venv
venv\Scripts\activate   # On Windows
source venv/bin/activate  # On Mac/Linux
```

Install dependencies
```bash
pip install -r requirements.txt
```

📑 Configuration
Edit config.py with your details:
```bash
SENDGRID_API_KEY = "YOUR_SENDGRID_API_KEY"
FROM_EMAIL = "your-verified-email@example.com"
TEMPLATE_ID = "your-template-id"
CSV_FILE = "participants.csv"
```

Get your API key from SendGrid Dashboard
Verify your sender email in Sender Authentication
Create a Dynamic Template in SendGrid and use its TEMPLATE_ID

📊 Participants CSV Format
Your participants.csv should look like this:
```bash
Name,Email,Id
John Doe,john@example.com,1
Jane Smith,jane@example.com,2
⚠️ Column names must match exactly (Name, Email, Id).
```

▶️ Usage
Run the bulk mail sender:
```bash
python main.py
```
Each participant will receive a personalized email using your SendGrid template.
